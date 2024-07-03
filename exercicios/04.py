import urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://github.com/Lucasvinipy')

except:
    print('deu erro')

else:
    print('deu certo')