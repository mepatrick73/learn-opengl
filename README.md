to run the project:

Release mode:
conan install . 
cmake --preset conan-release
cmake --build --preset conan-release


Debug mode:
conan install . -s build_type=Debug
cmake --preset conan-debug
cmake --build --preset conan-debug


