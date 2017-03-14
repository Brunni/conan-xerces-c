# conan-xerces-c
Conan package of xerces-c
https://xerces.apache.org/xerces-c/
[![badge](https://img.shields.io/badge/conan.io-xerces--c%2F3.1.4-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/xerces-c/3.1.4/Brunni/testing)

Inspired from https://github.com/SlideWave/conan-xerces-c but some improvements

* Building as shared lib works (Windows)
* Building as static lib works (Windows) but seems unusable (see below)
* Building linux static and shared lib works
* test_package works on linux
* Only building XercesLib now
* Download from Zip file
* Include path contains .c files as well

One major issue was the windows path length issue. Fixed by using custom "OutDir" for msbuild.

## TODO
* option with_icu is untested
* Test and fix static windows lib

Issue with static lib:
When trying to use static lib error is: 
`
Severity	Code	Description	Project	File	Line	Suppression State
Error	LNK2038	mismatch detected for 'RuntimeLibrary': value 'MT_StaticRelease' doesn't match value 'MD_DynamicRelease' in SomeXmlTest.obj	stuff	C:\Projects\jaz-3d-component\build\jazmodel\test\xerces-c_static_3.lib(XMLScanner.obj)	1
`	

Preprocessor macro XERCES_STATIC_LIBRARY defined manually as in  https://xerces.apache.org/xerces-c/build-3.html
But could probably be included in conan.
