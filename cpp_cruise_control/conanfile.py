from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class CruiseControlConan(ConanFile):
    name = "cpp_cruise_control"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = "gtest/1.11.0"
    generators = "CMakeToolchain", "CMakeDeps"
    exports_sources = "CMakeLists.txt", "src/*", "tests/*"

    def layout(self):
        self.folders.source = "."
        self.folders.build = "build"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

