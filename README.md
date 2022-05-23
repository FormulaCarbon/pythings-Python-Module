# PyThings Python Module

![Version](https://img.shields.io/badge/Version-0.4.4-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Dev-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Stage](https://img.shields.io/badge/Stage-Beta%20Testing-orange?style=for-the-badge)
![IDE](https://img.shields.io/badge/Made%20With-Python%20IDLE-%33776AB?style=for-the-badge&logo=python&logoColor=%33776AB)

## Table of Contents
1. [About](#about)
2. [Installation](#installation)
3. [Importing](#importing)
4. [Commands](#commands)
   - [Class: PCTools](#pctools)
   - [Class: Dict](#dict)
   - [Class: Images](#imgs)
   - [Class: MathTools](#mtools)
   - [Class: Security](#secure)
<a name='about'></a> 
## About PyThings
PyThings is a python 3 module that expands the functionality of python. It expands the connectivity of an IDE to the PC, expands the ability of dictionaries, adds an image scraping and opening functionality, add more math functions, and add an ecryption/decryption feature.

**Currently Tested Platforms**
- Windows 11

**Dependencies**
- setuptools
- plyer
- bs4
- pillow
- cryptography

<a name='installation'></a>
## Installation
**Unix/MacOS:**
```python shell
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pythings==0.4.4
```
**Windows:**
```python shell
py -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pythings==0.4.4
```

<a name='importing'></a>
## Importing
```python
import pythings
```
or (recommended)
```python
import pythings as pt
```
<a name='commands'></a>
## Commands
```python
pythings.test() # prints a test message to shell
```
<a name='pctools'></a>
**Class: PCTools**
```python
import pythings as pt
pctools = pt.PCTools()

pctools.pypiinstall(modname, pysrc, modsrc='pypi') # installs a python module on the users end, without importing.
# modname: name of module. pysrc: use 'web' if user installed from python.org, or 'app' if user downloaded from store. modsrc: 'pypi' for download from pypi, and 'testpypi' for download from testpypi.

pctools.notify(title, desc, appname='pythings',icon=None, time='2', status=None, toast=False) # popup desc notification. 
# See https://www.geeksforgeeks.org/python-desktop-notifier-using-plyer-module/ for documentation.

pctools.slice_mail(address) # slices an email into username and domain. Outputs a dict formatted like {'username":'pythings', 'domain':'example.com'}.
# address: email address to be sliced.

pctools.debug(filename, encodetype='utf_8') # debugs a file with same errors as the regular shell. Basically for debugging a file on the users device.
# filename: file to be debugged (must be a .py). encodetype: specifies encoding of the file (defaults to UTF 8)
```
<a name='dict'></a>
**Class: Dict**
```python
import pythings as pt
dtools = pt.Dict()

dtools.j2dict(obj, remove=None) # converts json to dictionary. dictionary is named the same as variable json is stored in.
# obj: variable of json to be converted. remove: specifies if any characters should be replaced in dict.

dtools.list2dict(key, content) # converts 2 lists into a dictionary. Shortens code.
# key: list with key values. content: list with content values that match key values.
```
<a name='imgs'></a>
**Class: Images**
```python
import pythings as pt
imgs = pt.Images()

imgs.getImage(link) # returns all image sources from a webpage as a list
# link: url of webpage to be scraped.

imgs.openImage(link, query) # opens an image in default image viewer
# link: direct link to image. query: name of image.
```
<a name='mtools'></a>
**Class: MathTools**
```python
import pythings as pt
mtools = pt.MathTools()

mtools.fib(num, length='one') # returns the nth integer of the fibonnaci sequence.
# num: the nth integer. length: 'one' for the nth integer, 'all' for all fibonnaci numbers up to the nth value.
```
<a name='secure'></a>
**Class: Security**
```python
import pythings as pt
stools = pt.Security()

stools.encrypt(text, filename) # encrypts a string using Fernet from cryptography.fernet. Returns encoded string and saves key to file.
# text: string to be encrypted. filename: file that the encoding key should be saved to (must be a .txt).

stools.decrypt(enctext, enckey) # decodes text that was encoded with the above method. Returns decoded string.
# enctext: string of characters returned by stools.encrypt(). enckey: the key saved to filename by stools.encrypt.
```
