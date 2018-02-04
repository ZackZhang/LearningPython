import urllib
import re

response = urllib.urlopen('https://www.pornhub.com/view_video.php?viewkey=ph592ef8731630a')
html = response.read()




# links = re.compile(r'.mp4')
# match = re.search(links, '.mp4')

#print (html.decode('utf-8'))

