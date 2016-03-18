import sys
import re

def mapper():
    parts = [
        r'(?P<host>\S+)',  # host %h
        r'\S+',  # indent %l (unused)
        r'(?P<user>\S+)',  # user %u
        r'\[(?P<time>.+)\]',  # time %t
        r'"(?P<request>.+)"',  # request "%r"
        r'(?P<status>[0-9]+)',  # status %>s
        r'(?P<size>\S+)',  # size %b (careful, can be '-')
    ]
    log = '10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469'
    #pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
    pattern = re.compile('(?P<host>\S+)[\s\S]*(?P<user>\S+)[\s\S]*\[(?P<time>.+)\]\s"(?P<request>.+)"\s(?P<status>[0-9]+)\s(?P<size>\S+)')

    m = pattern.match(log)
    print(m)

    res = m.groupdict()
    print(type(res))

    if res["user"] == "-":
        res["user"] = None

    res["status"] = int(res["status"])

    if res["size"] == "-":
        res["size"] = 0
    else:
        res["size"] = int(res["size"])

    for i in res:
        print(i, res[i])


mapper()
