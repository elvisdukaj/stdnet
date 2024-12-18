cmake_minimum_required(VERSION 3.17)
project(PackageTest)

find_package(stdnet REQUIRED)

add_executable(test_stdnet test.cpp)
target_link_libraries(test_stdnet stdnet::stdnet)
