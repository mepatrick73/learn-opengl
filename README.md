to run the project:

Release mode:
conan install . --build=missing
cmake --preset conan-release
cmake --build --preset conan-release


Debug mode:
conan install . -s build_type=Debug --build=missing
cmake --preset conan-debug
cmake --build --preset conan-debug


