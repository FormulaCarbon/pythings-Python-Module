def test():
    print('Test Complete. Pythings Images working.')
    return 'Images Working'

def getImages(link):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    htmldata = urlopen('https://www.geeksforgeeks.org/')
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    for item in images:
        print(item['src'])

def downloadImage(link, name):
    import urllib.request
    query = urllib.request.urlretrieve(link, name)
    img = open(name, 'xw')
    img.write(query)
    img.close()

def openImage(path, name = None):
    import urllib.request
    from PIL import Image
    try:
        img = Image.open(path)
        img.show()
    except FileNotFoundError:
        query = urllib.request.urlretrieve(path, name)
        img = Image.open(path)
        img.show()
    except:
        raise FileNotFoundError('No file found in '+path)
