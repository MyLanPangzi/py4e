import urllib.request as req, urllib.parse as parse, urllib.error

img = req.urlopen('http://data.pr4e.org/cover3.jpg')
out = open('img.jpg', 'wb')
size = 0
while True:
    info = img.read(10000)
    if len(info) < 1:
        break
    size += size + len(info)
    out.write(info)

print('copy size ', size)
out.close()