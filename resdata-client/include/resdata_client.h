#ifndef RESDATA_CLIENT_H
#define RESDATA_CLIENT_H

#include <string>
#include <vector>

class ResDataClient {
public:
    ResDataClient(const std::string &base_url);
    bool upload_data(const std::string &file_path);
    std::vector<std::string> fetch_data(const std::string &project_id, const std::string &experiment_id = "");
    bool sync_files(const std::string &local_dir, const std::string &remote_dir);
private:
    std::string base_url;
};

#endif // RESDATA_CLIENT_H
