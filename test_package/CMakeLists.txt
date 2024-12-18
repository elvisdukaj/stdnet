cmake_minimum_required(VERSION 3.17)
project(PackageTest)
enable_testing()

find_package(stdnet REQUIRED)

add_executable(test_stdexec test.cpp)
target_link_libraries(test_stdexec stdnet::stdnet)
add_test(test_stdexec test_stdexec)
