# PyThings Python Module

![Version](https://img.shields.io/badge/Version-0.4.8-green?style=flat)
![Status](https://img.shields.io/badge/Status-In%20Dev-green?style=flat)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat)
![Stage](https://img.shields.io/badge/Stage-Beta%20Testing-orange?style=flat)
![IDE](https://img.shields.io/badge/-Python%20IDLE-%33776AB?style=for-the-badge&logo=python&logoColor=white)

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
6. [License](#license)
5. [Dev Info](#dev)
<a name='about'></a>
## About PyThings
PyThings is a python 3 package that expands the functionality of python. It expands the connectivity of an IDE to the PC, expands the ability of dictionaries, adds an image scraping, downloading, and opening functionality, adds more math functions, and adds an encryption/decryption feature.

**Currently Tested Platforms**
- Windows 11

**Dependencies**
- setuptools
- plyer
- bs4
- pillow
- cryptography

To contribute, go [here](https://github.com/FormulaCarbon/pythings-Python-Module/blob/main/CONTRIBUTING.md).

<a name='installation'></a>
## Installation
**Unix/MacOS:**
```powershell
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pythings==0.4.8
```
**Windows:**
```powershell
py -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pythings==0.4.8
```

<a name='importing'></a>
## Importing
```python
import pythings.DictTools
import pythings.Images
import pythings.MathTools
import pythings.PCTools
import pythings.Security
```
or (recommended)
```python
import pythings.PCTools as ptp
import pythings.DictTools as ptd
import pythings.Images as pti
import pythings.MathTools as ptm
import pythings.Security as pts
```
<a name='commands'></a>
## Commands
```python
test() # prints a test message to shell
```
<a name='pctools'></a>
**Module: PCTools**
```python
import pythings.PCTools as ptp

ptp.pypiinstall(modname, os, modsrc='pypi') # installs a python module on the users end, without importing.
# modname: name of module. os: operating system ('windows' or 'unix-mac'). modsrc: 'pypi' for download from pypi, and 'testpypi' for download from testpypi.

ptp.notify(title, desc, appname='pythings',icon=None, time='2', status=None, toast=False) # popup desc notification.
# See https://www.geeksforgeeks.org/python-desktop-notifier-using-plyer-module/ for documentation.

ptp.slice_mail(address) # slices an email into username and domain. Outputs a dict formatted like {'username":'pythings', 'domain':'example.com'}.
# address: email address to be sliced.

ptp.debug(filename, encodetype='utf_8') # debugs a file with same errors as the regular shell. Basically for debugging a file on the users device.
# filename: file to be debugged (must be a .py). encodetype: specifies encoding of the file (defaults to UTF 8)
```
<a name='dict'></a>
**Module: DictTools**
```python
import pythings.DictTools as ptd

ptd.j2dict(obj, remove=None) # converts json to dictionary. dictionary is named the same as variable json is stored in.
# obj: variable of json to be converted. remove: specifies if any characters should be replaced in dict.

ptd.list2dict(key, content) # converts 2 lists into a dictionary. Shortens code.
# key: list with key values. content: list with content values that correspond with key values.
```
<a name='imgs'></a>
**Module: Images**
```python
import pythings.Images as pti

pti.getImage(link) # returns all image sources from a webpage as a list
# link: url of webpage to be scraped.

pti.downloadImage(link, name) # downloads an image from the web
# link: direct URL link to the image. name: name pf the image.

pti.openImage(path, name = None) # opens an image in default image viewer
# path: direct path or URL link to image. name: name of image (unneeded if path is not a URL).
```
<a name='mtools'></a>
**Module: MathTools**
```python
import pythings.MathTools as ptm

ptm.fib(num, length='one') # returns the nth integer of the fibonnaci sequence.
# num: the nth integer. length: 'one' for the nth integer, 'all' for all fibonnaci numbers up to the nth value.
```
<a name='secure'></a>
**Class: Security**
```python
import pythings.Security as pts

pts.encrypt(text) # encrypts a string using Fernet from cryptography.fernet. Returns encoded string and key in a list, with the encoded text first.
# text: string to be encrypted.

pts.decrypt(enctext, enckey) # decodes text that was encoded with the above method. Returns decoded string.
# enctext: string of characters returned by pts.encrypt() in the first item of the list. enckey: the key in the second item of the list created by pts.encrypt()
```
<a name='license'></a>
## License
MIT License

Copyright (c) 2022 Siddharth Kakumanu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<a name='dev'></a>
## Dev Info (Ignore this if you are not a dev)
**File System: Unbuilt**
```graphql
.
└── App/
    ├── setup.py
    ├── Module/
    │   ├── __init__.py
    │   └── pythings/
    |       ├── PCTools.py
    |       ├── DictTools.py
    |       ├── Images.py
    |       ├── MathTools.py
    |       └── Security.py
    ├── README.md
    └── LICENSE
```
**File System: Built**
```graphql
.
├── App/
│   ├── setup.py
│   ├── pythings.egg-info/
│   │   ├── top_level.txt
│   │   ├── SOURCES.txt
│   │   ├── requires.txt
│   │   ├── PKG-INFO
│   │   └── dependency_links.txt
│   ├── Module/
│   │   ├── __init__.py
│   │   └── pythings/
|   |       ├── PCTools.py
|   |       ├── DictTools.py
|   |       ├── Images.py
|   |       ├── MathTools.py
|   |       └── Security.py
│   ├── README.md
│   └── LICENSE
└── dist/
    ├── pythings-0.4.8.tar.gz
    └── pything-0.4.8-none-any.whl
```
**Build Command**
```powershell
py Documents\Python_projects\pythings\App\setup.py sdist bdist_wheel
```
**Upload Command**
```powershell
py -m twine upload --repository testpypi dist/* -u▉▉▉▉▉ -p▉▉▉▉▉
```
**INFO**

Current Version: 0.4.8

Dev Stage: Beta Testing

Made On: Atom

Programming Language: Python 3

Natural Language: English (USA)

License: MIT

**Updates**
- v0.4.8: converted from a single module to a package.
