from conans import ConanFile, CMake, tools
import os

class SDLConan(ConanFile):
	name = "sdl2"
	version = "2.0.20"
	description = "Simple Direct Media Layer (SDL)"
	homepage = "https://www.libsdl.org"
	license = "Zlib https://www.libsdl.org/license.php"
	settings = "os", "compiler", "arch"
	generators = "cmake"
	exports_sources = ["CMakeLists.txt"]
	zip_folder_name = f"SDL2-{version}"
	zip_name = f"{zip_folder_name}.tar.gz"
	build_subfolder = "build"
	source_subfolder = "source"

	def source(self):
		tools.get(f"https://libsdl.org/release/{self.zip_name}")
		os.rename(self.zip_folder_name, self.source_subfolder)

	def build(self):
		cmake = CMake(self)
		cmake.configure(build_folder=self.build_subfolder)
		cmake.build()
