#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostTtiConan(base.BoostBaseConan):
    name = "boost_tti"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_tti"
    lib_short_names = ["tti"]
    header_only_libs = ["tti"]
    b2_requires = [
        "boost_config",
        "boost_function_types",
        "boost_mpl",
        "boost_preprocessor",
        "boost_type_traits"
    ]
