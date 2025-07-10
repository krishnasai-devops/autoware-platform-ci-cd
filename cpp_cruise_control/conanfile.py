from conan import ConanFile

class AutowarePlatform(ConanFile):
    name = "autoware_platform"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = (
        "gtest/1.14.0",
        "boost/1.83.0"
    )
    #generators = "CMakeDeps", "CMakeToolchain"
    generators = "CMakeToolchain", "CMakeDeps"