cmake_minimum_required(VERSION 3.10)
project(CruiseControl)

set(CMAKE_CXX_STANDARD 14)

include_directories(include)
add_executable(test_cruise src/cruise.cpp tests/test_cruise.cpp)