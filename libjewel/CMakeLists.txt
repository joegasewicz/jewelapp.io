cmake_minimum_required(VERSION 3.30)
project(libjewel C)

set(CMAKE_C_STANDARD 11)

add_library(libjewel STATIC library.c)
