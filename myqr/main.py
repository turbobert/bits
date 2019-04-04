#!/usr/bin/env python3


import qrcode
import sys


#modes: [1] == gotomeeting ID
#       [1] == youtube ID

if len(sys.argv) < 3:
    print("no parameters")
    sys.exit(0)

if sys.argv[1] == "gotomeeting":
    url = "https://global.gotomeeting.com/join/%s" % sys.argv[2]
    print("url=%s" % url)
    img = qrcode.make(url)
    img.save("gotomeeting.png")
    sys.exit(0)

if sys.argv[1] == "text":
    img = qrcode.make(sys.argv[2].replace("\\n", "\n"))
    img.save("text.png")
    sys.exit(0)

if sys.argv[1] == "youtube":
    url = "https://www.youtube.com/watch?v=%s" % sys.argv[2]
    print("url=%s" % url)
    img = qrcode.make(url)
    img.save("youtube.png")
    sys.exit(0)

