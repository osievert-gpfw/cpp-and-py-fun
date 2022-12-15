cmake_minimum_required(VERSION 3.18.0)

project(cppfun)

add_executable(cppfun main.cpp)
set_target_properties(cppfun PROPERTIES
    XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++17"
    CXX_STANDARD 17
    )
