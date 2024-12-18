from conan import ConanFile
from conan.tools.build.cppstd import check_min_cppstd
from conan.tools.cmake import CMake

class StdnetPackage(ConanFile):
  name = "stdnet"
  version = "0.1.0"
  description = "std::net"
  author = ""
  topics = ("WG21", "concurrency", "networking")
  homepage = "https://github.com/NVIDIA/stdexec"
  url = "https://github.com/NVIDIA/stdexec"
  license = "Apache 2.0"

  exports_sources = (
    "include/*",
    "CMakeLists.txt"
  )

  settings = "os", "arch", "compiler", "build_type"
  
  generators = "CMakeToolchain", "CMakeDeps"
  requires = "stdexec/0.11.0"

  def build(self):
    cmake = CMake(self)
    cmake.configure()
    cmake.build()

  def package(self):
    cmake = CMake(self)
    cmake.install()
  
  def package_id(self):
    self.info.clear()

  def package_info(self):
    self.cpp_info.set_property("cmake_file_name", "stdnet")
    self.cpp_info.set_property("cmake_target_name", "stdnet::stdnet")
    self.cpp_info.requires.append("stdexec::stdexec")

