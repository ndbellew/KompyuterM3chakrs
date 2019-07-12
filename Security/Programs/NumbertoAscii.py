import sys
import string
import os
from optparse import OptionParser

VERSION = "Numbers to Ascii 0.1"
AsciiList= "".join([chr(i) for i in range(127)])

usage = "Usage: %prog [Numbers]"
parser = OptionParser(usage)
parser.add_option('-v', '--version', dest="version", action="store_true", help="Prints version")
(options, args) = parser.parse_args()

if len(args) < 1 or options.version:
    if options.version:
        print(VERSION)
        sys.exit(0)
    else:
        parser.print_help()
        sys.exit(0)

answer = ""
for i in args:
    answer+= AsciiList[int(i)]

print(answer)
