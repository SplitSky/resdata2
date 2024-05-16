#include "resdata_client.h"
#include <iostream>

int main() {
    ResDataClient client("http://localhost:8000");

    // Example: Upload a data file
    if (client.upload_data("path/to/data/file.csv")) {
        std::cout << "Data upload successful" << std::endl;
    } else {
        std::cout << "Data upload failed" << std::endl;
    }

    // Example: Fetch data
    auto data = client.fetch_data("project_id");
    for (const auto &item : data) {
        std::cout << item << std::endl;
    }

    return 0;
}
