cmake_minimum_required(VERSION 3.10)
project(ResDataClient)

set(CMAKE_CXX_STANDARD 17)

# Find required libraries
find_package(PkgConfig REQUIRED)
pkg_check_modules(CURL REQUIRED libcurl)
pkg_check_modules(JSONCPP REQUIRED jsoncpp)
pkg_check_modules(WEBSOCKETPP REQUIRED websocketpp)

# Include directories
include_directories(${CURL_INCLUDE_DIRS})
include_directories(${JSONCPP_INCLUDE_DIRS})
include_directories(${WEBSOCKETPP_INCLUDE_DIRS})
include_directories(include)

# Source files
set(SOURCES
    src/resdata_client.cpp
    src/main.cpp)

# Add executable
add_executable(resdata_client ${SOURCES})

# Link libraries
target_link_libraries(resdata_client ${CURL_LIBRARIES} ${JSONCPP_LIBRARIES} ${WEBSOCKETPP_LIBRARIES})
