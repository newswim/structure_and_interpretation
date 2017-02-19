'''
is an import statement that loads functionality for accessing data on the
Internet. In particular, it makes available a function called urlopen, which
can access the content at a uniform resource locator (URL), a location of
something on the Internet.
'''
from urllib.request import urlopen

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

words = set(shakespeare.read().decode().split())

palindromes = {w for w in words if len(w) == 6 and w[::-1] in words}

print(palindromes)
