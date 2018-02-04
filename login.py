import urllib2

response = urllib2.urlopen('http://www.voidspace.org.uk')
html = response.read()
print html