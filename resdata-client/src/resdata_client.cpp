#include "resdata_client.h"
#include <curl/curl.h>
#include <json/json.h>
#include <fstream>

ResDataClient::ResDataClient(const std::string &base_url) : base_url(base_url) {}

bool ResDataClient::upload_data(const std::string &file_path) {
    CURL *curl;
    CURLcode res;
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if (curl) {
        std::ifstream file(file_path, std::ios::binary);
        if (!file.is_open()) return false;

        std::string url = base_url + "/api/data";
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);
        curl_easy_setopt(curl, CURLOPT_READDATA, &file);

        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        file.close();
        return (res == CURLE_OK);
    }
    return false;
}

std::vector<std::string> ResDataClient::fetch_data(const std::string &project_id, const std::string &experiment_id) {
    CURL *curl;
    CURLcode res;
    std::vector<std::string> data;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if (curl) {
        std::string url = base_url + "/api/data?project_id=" + project_id;
        if (!experiment_id.empty()) {
            url += "&experiment_id=" + experiment_id;
        }

        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());

        std::string response_string;
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, +[](char *ptr, size_t size, size_t nmemb, std::string *data) {
            data->append(ptr, size * nmemb);
            return size * nmemb;
        });
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response_string);

        res = curl_easy_perform(curl);
        if (res == CURLE_OK) {
            Json::CharReaderBuilder readerBuilder;
            Json::Value root;
            std::string errs;
            std::istringstream s(response_string);
            if (Json::parseFromStream(readerBuilder, s, &root, &errs)) {
                for (const auto &item : root["data"]) {
                    data.push_back(item.asString());
                }
            }
        }
        curl_easy_cleanup(curl);
    }
    return data;
}

bool ResDataClient::sync_files(const std::string &local_dir, const std::string &remote_dir) {
    // Implement file synchronization logic here
    return true;
}
