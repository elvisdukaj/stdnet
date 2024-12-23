from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy
from conan.errors import ConanInvalidConfiguration

class StdnetPackage(ConanFile):
  name = "stdnet"
  version = "0.1.0"
  description = "std::net"
  author = "Dietmar Kuehl"
  topics = ("WG21", "concurrency", "networking")
  homepage = ""
  url = "https://github.com/elvisdukaj/stdnet"
  license = "Apache 2.0"

  exports_sources = (
    "include/*",
    "CMakeLists.txt",
    "LICENSE.txt"
  )

  settings = "os", "arch", "compiler", "build_type"
  
  generators = "CMakeToolchain", "CMakeDeps"
  requires = "stdexec/0.11.0", "libevent/2.1.12"

  def layout(self):
    self.folders.build_folder_vars = [                                                                "settings.os",                                                                                "settings.arch",                                                                              "settings.compiler",                                                                          "settings.compiler.version"                                                               ]
    cmake_layout(self)

  def validate(self):
    if self.settings.os == "Windows":
      raise ConanInvalidConfiguration("Windows is not supported!")

  def build(self):
    cmake = CMake(self)
    cmake.configure()
    cmake.build()

  def package(self):
    cmake = CMake(self)
    cmake.install()
    copy(self, "*LICENSE*", src=self.source_folder, dst=self.package_folder)
  
  def package_id(self):
    self.info.clear()

  def package_info(self):
    self.cpp_info.set_property("cmake_file_name", "stdnet")
    self.cpp_info.set_property("cmake_target_name", "stdnet::stdnet")

    self.cpp_info.libdirs = []
    self.cpp_info.libs = []
    self.cpp_info.includedirs = ['include']

    self.cpp_info.requires.append("stdexec::stdexec")
    self.cpp_info.requires.append("libevent::libevent")

