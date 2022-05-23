# PyThings Python Module

![Version](https://img.shields.io/badge/Version-0.4.0-green?style=flat)
![Status](https://img.shields.io/badge/Status-In%20Dev-green?style=flat)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat)
![License](https://img.shields.io/badge/Stage-Beta%20Testing-blue?style=flat)
## About PyThings
PyThings is a python 3 module that expands the functionality of python. It expands the connectivity of an IDE to the PC, expands the ability of dictionaries, and adds an image scraping and opening functionality.

**Currently Tested Platforms**
- Windows 11

**Dependencies**
- urllib.request
- plyer
- bs4
- pillow
- cryptography

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

pctools.slice_mail(address) # slices an email into username and domain. Outputs a dict formatted like {'username":'pythings', 'domain':'example.com'}.
# address: email address to be sliced.

pctools.debug(filename, encodetype='utf_8') # debugs a file with same errors as the regular shell. Basically for debugging a file on the users device.
# filename: file to be debugged (must be a .py). encodetype: specifies encoding of the file (defaults to UTF 8)
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
**class: MathTools**
```
import pythings as pt
mtools = pt.MathTools()

mtools.fib(num, length='one') # returns the nth integer of the fibonnaci sequence.
# num: the nth integer. length: 'one' for the nth integer, 'all' for all fibonnaci numbers up to the nth value.
```
**class: Security**
```
import pythings as pt
stools = pt.Security()

stools.encrypt(text, filename) # encrypts a string using Fernet from cryptography.fernet. Returns encoded string and saves key to file.
# text: string to be encrypted. filename: file that the encoding key should be saved to (must be a .txt).

stools.decrypt(enctext, enckey) # decodes text that was encoded with the above method. Returns decoded string.
# enctext: string of characters returned by stools.encrypt(). enckey: the key saved to filename by stools.encrypt.

