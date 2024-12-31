from conan import ConanFile, tools
from conan.tools.cmake import cmake_layout


class LearnOpenGLConan(ConanFile):
    name = "learn-opengl"
    version = "1.0"
    # Make sure 'compiler' is included
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def requirements(self):
        self.requires("glfw/3.4")

    def generate(self):
        # Example to set cmake toolchain in the profile
        tc = tools.cmake.CMakeToolchain(self)
        tc.variables["CMAKE_C_COMPILER"] = "clang"
        tc.variables["CMAKE_CXX_COMPILER"] = "clang++"
        tc.cache_variables["CMAKE_EXPORT_COMPILE_COMMANDS"] = "ON"
        tc.generate()

    def layout(self):
        cmake_layout(self)
