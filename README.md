# conan-xerces-c
Conan package of xerces-c

Inspired from https://github.com/SlideWave/conan-xerces-c but some improvements

* Building as shared lib works (Windows)
* Building as static lib works (Windows) but seems unusable
* Only building XercesLib now
* Download from Zip file
* Include path contains .c files as well

One major issue was the windows path length issue. Fixed by using custom "OutDir" for msbuild.

## TODO
* option with_icu is untested
* Linux untested (won't work)

Issue with static lib:
When trying to use static lib error is: 
`
Severity	Code	Description	Project	File	Line	Suppression State
Error	LNK2038	mismatch detected for 'RuntimeLibrary': value 'MT_StaticRelease' doesn't match value 'MD_DynamicRelease' in CalibrationXmlTest.obj	jazmodel_test	C:\Projects\jaz-3d-component\build\jazmodel\test\xerces-c_static_3.lib(XMLScanner.obj)	1
`	

Preprocessor macro XERCES_STATIC_LIBRARY defined manually as in  https://xerces.apache.org/xerces-c/build-3.html
But could probably be included in conan.