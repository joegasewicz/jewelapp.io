cmake_minimum_required(VERSION 3.30)
project(libjewel C)

set(CMAKE_C_STANDARD 11)

find_package(OpenGL REQUIRED)

add_library(jewel SHARED library.c)

target_include_directories(jewel PUBLIC ${OPENGL_INCLUDE_DIRS})
target_link_libraries(jewel ${OPENGL_LIBRARIES})
# macOS-specific: Link against the OpenGL framework
if(APPLE)
    target_compile_definitions(jewel PRIVATE GL_SILENCE_DEPRECATION)
    target_link_libraries(jewel "-framework OpenGL")
endif()
