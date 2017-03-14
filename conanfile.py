from conans import ConanFile, tools, AutoToolsBuildEnvironment
import zipfile
import os

class xercescConan(ConanFile):
	name = "xerces-c"
	version = "3.1.4"
	license = "http://www.apache.org/licenses/LICENSE-2.0.html"
	settings = {
		"os": ["Windows", "Linux"],
		"compiler": ["Visual Studio", "gcc"],
		"build_type": ["Debug", "Release"],
		"arch": ["x86", "x86_64"]
	}
	url = "https://github.com/Brunni/conan-xerces-c"
	options = {
        "with_icu": [True, False],
		"shared": [True, False]
	}
	default_options = "with_icu=False","shared=True"
	src_dir = "xerces-c-3.1.4"

	def source(self):
		tools.download("http://ftp.halifax.rwth-aachen.de/apache/xerces/c/3/sources/xerces-c-3.1.4.zip", "xerces.zip")
		zip_ref = zipfile.ZipFile("xerces.zip", 'r')
		zip_ref.extractall()
		zip_ref.close()
	
	def build(self):
		if self.settings.compiler == "Visual Studio":
			self.build_with_vs()
		else:
			self.build_with_make()

	def package(self):
		self.copy("*.hpp", dst="include", src="%s/src" % self.src_dir)
		self.copy("*.c", dst="include", src="%s/src" % self.src_dir)
		self.copy("*.lib", dst="lib", keep_path=False)
		self.copy("*.exp", dst="lib", keep_path=False)
		self.copy("*.dll", dst="bin", keep_path=False)
		self.copy("*.a", dst="lib", keep_path=False)
		self.copy("*.so", dst="lib", keep_path=False)
		
	def build_with_vs(self):
		solution_path = "{0}/{1}/projects/Win32/VC{2}/xerces-all/xerces-all.sln".format(self.conanfile_directory, self.src_dir, str(self.settings.compiler.version))
#		solution_path = os.path.join(os.path.dirname(__file__), solution_path)
		config_name = str(self.settings.build_type)	 # *TODO: other options 
		platform = "x64" if self.settings.arch == "x86_64" else "Win32"
		config_name = "Static %s" % str(self.settings.build_type) if self.options.shared == False else str(self.settings.build_type)
		config_name = "ICU %s" % str(self.settings.build_type) if self.options.with_icu == True else config_name
		vs_version = self.settings.compiler.version

		build_cmd = "msbuild \"{solution}\" \"/p:Configuration={config}\" \"/p:Platform={platform}\" \"/target:XercesLib\" \"/p:VisualStudioVersion={vs_version}\" /p:OutputPath={output_path} /p:OutDir={output_path} /m".format(
			solution=solution_path,
			config=config_name,
			platform=platform,
			vs_version=vs_version,
			output_path="%s/build" % self.conanfile_directory # shorter output path because of windows path length issue
		)
#		print (build_cmd)
		self.run(build_cmd)

	# *WARNING: untested!
	def build_with_make(self):
		if self.options.shared == True:
			sharedoption = "--disable-static"
		else:
			sharedoption = "--disable-shared"
		env_build = AutoToolsBuildEnvironment(self)
		self.run("cd %s && %s" % (self.src_dir, 'chmod u+x configure'))
		self.run("cd %s/config && %s" % (self.src_dir, 'chmod u+x pretty-make'))
	        with tools.environment_append(env_build.vars):
			self.run("cd %s && %s %s" % (self.src_dir, './configure', sharedoption))
			self.run("cd %s && %s " % (self.src_dir, 'make -j 8'))
		
	def package_info(self):
		if self.settings.os == "Linux":
			self.cpp_info.libs = ["xerces-c", "pthread"]
		else:
			if self.options.shared == True:
				self.cpp_info.libs = ["xerces-c_3"]
			else:
				self.cpp_info.libs = ["xerces-c_static_3"]
