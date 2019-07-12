# Simple Alphabet decoder
# Author Nathan Bellew

import sys
import os
import string
from optparse import OptionParser

VERSION = "Simple Alphabet 0.1 Alpha"
alpha = list(string.ascii_lowercase)
offset = 0

usage = "Usage: %prog [-o | --offset N] [letters]"
parser = OptionParser(usage)
parser.add_option('-o','--offset', dest="offset", help="This cipher will use a simple offset, it will alwyas default to 0. simple add -o and then any number such as \n -o 4\n to set number 1 to 5 and then translate to letters")
parser.add_option('-v','--version', dest="version", action="store_true", help="if added will print the Version of the program")
(options, args)= parser.parse_args()

if len(args) < 1 or options.version:
    if options.version:
        print(VERSION)
        sys.exit(0)
    else:
        parser.print_help()
        sys.exit(0)

if options.offset:
    offset = options.offset
def FindLetter(letter):
    for i in range(0, len(alpha)-1):
        if letter == alpha[i]:
            return i
def main():
    EncryptedPhrase = " ".join(args)
    DecryptedPhrase = ""
    for i in EncryptedPhrase:
        if i != " ":
            DL = int(offset)+FindLetter(i)
            if DL>25:
                DL-=26
            DecryptedPhrase+= alpha[DL]
        else:
            DecryptedPhrase+= " "
    print(DecryptedPhrase)

main()
