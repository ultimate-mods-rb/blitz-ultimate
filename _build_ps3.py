#!/usr/bin/env python
import dependencies.buildark.buildark as buildark

buildark.build_ark(
	["./_ark"],
	"./_build/ps3/USRDIR/gen/",
	"./temp_ark_ps3",
	"patch_ps3",
	"rb3",
	[
		r".*\.bik$",
		r".*\..*_wii$",
		r".*\.xbvwii$",
		r".*\..*_xbox$",
		r".*_out\/.*",
		r".*_dbg\.milo.*",
		r".*_rt\.milo.*",
		r".*\.bak$",
		r".*\.png$",
		r".*\.jpg$",
		r".*\.dds$",
		r".*\.xcf$",
		r".*\.sh$",
		r".*\.py$"
	]
)
