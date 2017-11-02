from conans import ConanFile, tools
import os

class BoostTtiConan(ConanFile):
    name = "Boost.Tti"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-tti"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["tti"]
    requires =  "Boost.Config/1.65.1@bincrafters/testing", \
                      "Boost.Function_Types/1.65.1@bincrafters/testing", \
                      "Boost.Mpl/1.65.1@bincrafters/testing", \
                      "Boost.Optional/1.65.1@bincrafters/testing", \
                      "Boost.Preprocessor/1.65.1@bincrafters/testing", \
                      "Boost.Type_Traits/1.65.1@bincrafters/testing"

                      #config0 function_types5 mpl5 preprocessor0 type_traits3

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()