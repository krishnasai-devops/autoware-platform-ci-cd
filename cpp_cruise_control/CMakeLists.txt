cmake_minimum_required(VERSION 3.15)
project(cruise_control)

set(CMAKE_CXX_STANDARD 17)

#include_directories(include)
#add_executable(test_cruise src/cruise.cpp tests/test_cruise.cpp)

# Conan setup (used when Conan 2.x + CMakeDeps is active)
include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)

# Add sources
add_executable(test_cruise tests/test_cruise.cpp)

# Find and link GTest
find_package(GTest REQUIRED)
target_link_libraries(test_cruise GTest::gtest GTest::gtest_main)

# (Optional) Add Google Test CTest
enable_testing()
add_test(NAME cruise_test COMMAND test_cruise)
