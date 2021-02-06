import re

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[\d.]+', x)
print(y)
