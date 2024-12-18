#  Copyright (c) 2023 Dietmar Kuehl http://www.dietmar-kuehl.de
# 
#  Licensed under the Apache License Version 2.0 with LLVM Exceptions
#  (the "License"); you may not use this file except in compliance with
#  the License. You may obtain a copy of the License at
# 
#    https://llvm.org/LICENSE.txt
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

cmake_minimum_required(VERSION 3.22.1)
project(STDNET LANGUAGES C CXX VERSION "0.1.0")

find_package(stdexec REQUIRED CONFIG)
find_package(Libevent REQUIRED CONFIG)

add_library(stdnet INTERFACE)

target_sources(stdnet INTERFACE FILE_SET HEADERS
  FILES  
    include/stdnet/basic_socket.hpp
    include/stdnet/basic_stream_socket.hpp
    include/stdnet/buffer.hpp
    include/stdnet/container.hpp
    include/stdnet/context_base.hpp
    include/stdnet/cpo.hpp
    include/stdnet/endpoint.hpp
    include/stdnet/internet.hpp
    include/stdnet/io_base.hpp
    include/stdnet/io_context_scheduler.hpp
    include/stdnet/io_context.hpp
    include/stdnet/libevent_context.hpp
    include/stdnet/netfwd.hpp
    include/stdnet/poll_context.hpp
    include/stdnet/socket_base.hpp
    include/stdnet/socket.hpp
    include/stdnet/timer.hpp
  BASE_DIRS include
)

target_link_libraries(stdnet INTERFACE stdexec::stdexec libevent::libevent)

include(GNUInstallDirs)
install(
  TARGETS stdnet
  FILE_SET HEADERS
)
