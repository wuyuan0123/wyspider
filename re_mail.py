import re
re = re.compile(r'([\w]+)@([\w]+\.[\w]+)')
print re.match('wuyuan@youfu.com').groups()
