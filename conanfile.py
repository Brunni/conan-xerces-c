from conans import ConanFile, tools, CMake
import zipfile

class xercescConan(ConanFile):
    name = "xerces-c"
    version = "3.2.0"
    license = "http://www.apache.org/licenses/LICENSE-2.0.html"
    settings = {
        "os": ["Windows", "Linux"],
        "compiler": ["Visual Studio", "gcc"],
        "build_type": ["Debug", "Release"],
        "arch": ["x86", "x86_64"]
    }
    url = "https://github.com/stefan-titus-keysight/conan-xerces-c"
    options = {
        "with_icu": [True, False],
        "shared": [True, False]
    }
    default_options = "with_icu=False","shared=True"
    src_dir = "xerces-c-3.2.0"

    def source(self):
        tools.download("https://archive.apache.org/dist/xerces/c/3/sources/xerces-c-3.2.0.zip", "xerces.zip")
        zip_ref = zipfile.ZipFile("xerces.zip", 'r')
        zip_ref.extractall()
        zip_ref.close()
    
    def build(self):
        self.cmake = CMake(self)
        self.cmake.configure(source_dir=self.conanfile_directory + "/" + self.src_dir, build_dir="./build/")
        self.cmake.build()

    def package(self):
        # This is to get util/Xerces_autoconf_config.hpp
        self.copy("*.hpp", dst="include", src="%s/src" % self.cmake.build_dir)

        self.copy("*.hpp", dst="include", src="%s/src" % self.src_dir)
        self.copy("*.c", dst="include", src="%s/src" % self.src_dir)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.exp", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        
    def package_info(self):
        if self.settings.os == "Linux":
            self.cpp_info.libs = ["xerces-c", "pthread"]
        else:
            if self.options.shared == True:
                if self.settings.build_type == "Debug":
                    self.cpp_info.libs = ["xerces-c_3D"]
                else:
                    self.cpp_info.libs = ["xerces-c_3"]
            else:
                self.cpp_info.libs = ["xerces-c_static_3"]
