import urllib.request

txt = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in txt:
    print(line.decode().strip())
