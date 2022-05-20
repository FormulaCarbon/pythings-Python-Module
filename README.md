# PyThings Python Module

![Version](https://img.shields.io/badge/Version-0.2.0-green)
![Status](https://img.shields.io/badge/Status-In%20Dev-green)
![Status](https://img.shields.io/badge/License-MIT-blue)

## Importing
```
import pythings
```
or (recommended)
```
import pythings as pt
```
## Commands
```
pythings.test() # prints a test message to shell
```
**class: PCTools**
```
import pythings as pt
pctools = pt.PCTools()

pctools.pypiinstall(modname, pysrc, modsrc='pypi') # installs a python module on the users end, without importing.
# modname: name of module. pysrc: use 'web' if user installed from python.org, or 'app' if user downloaded from store. modsrc: 'pypi' for download from pypi, and 'testpypi' for download from testpypi.

pctools.notify(title, desc, appname='pythings',icon=None, time='2', status=None, toast=False) # popup desc notification. see https://www.geeksforgeeks.org/python-desktop-notifier-using-plyer-module/ for documentation.
```
**class: Dict**
```
import pythings as pt
dtools = pt.Dict()

dtools.j2dict(obj, remove=None) # converts json to dictionary. dictionary is named the same as variable json is stored in.
# obj: variable of json to be converted. remove: specifies if any characters should be replaced in dict.

dtools.list2dict(key, content) # converts 2 lists into a dictionary. Shortens code.
# key: list with key values. content: list with content values that match key values.
```
**class: Images**
```
import pythings as pt
imgs = pt.Images()

imgs.getImage(link) # returns all image sources from a webpage as a list
# link: url of webpage to be scraped.

imgs.openImage(link, query) # opens an image in default image viewer
# link: direct link to image. query: name of image.
```

