from conan import ConanFile

class AutowarePlatform(ConanFile):
    name = "autoware_platform"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = (
        "gtest/1.14.0",
        "boost/1.83.0"
    )
<<<<<<< HEAD
    generators = "CMakeDeps", "CMakeToolchain"

=======
    #generators = "CMakeDeps", "CMakeToolchain"
    generators = "CMakeToolchain", "CMakeDeps"
>>>>>>> 606fd43b29655d060e6e03d03d2ed45fbdf1b21d
