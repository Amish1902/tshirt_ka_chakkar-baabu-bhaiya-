from urllib.request import urlopen 

def checkNetwork():
    try:
        urlopen('https://1.1.1.1', timeout=1)
        return True
    except urllib.error.URLError as err:
        return False
