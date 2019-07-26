# Simple Alphabet decoder
# Author Nathan Bellew

import sys
import os
import string
from optparse import OptionParser

VERSION = "Simple Alphabet 0.3 Alpha"
alpha = list(string.ascii_lowercase)
offset = 0

usage = "Usage: %prog [-o | --offset N] [letters]"
parser = OptionParser(usage)
parser.add_option('-o','--offset', dest="offset", help="This cipher will use a simple offset, it will alwyas default to 0. simple add -o and then any number such as \n -o 4\n to set number 1 to 5 and then translate to letters")
parser.add_option('-v','--version', dest="version", action="store_true", help="if added will print the Version of the program")
parser.add_option('-n', '--numbers', dest ="numbers", action="store_true", help="Works just like normal except if you are given the numbers of the alphabet instead of the letters.")
parser.add_option('-u', action="store_true", dest="uppercase",help="This will return the message in all uppercase.")
(options, args)= parser.parse_args()

if len(args) < 1 or options.version:
    if options.version:
        print(VERSION)
        sys.exit(0)
    else:
        parser.print_help()
        sys.exit(0)

if options.offset:
    offset = int(options.offset)
def FindLetter(letter):
    for i in range(0, len(alpha)):

        if letter.lower() == alpha[i]:
            return i
def Letters():
    EncryptedPhrase = " ".join(args)
    DecryptedPhrase = ""
    for i in EncryptedPhrase:
        if i != " ":

            DL = offset+int(FindLetter(i))
            while DL>25:
                DL-=26
            DecryptedPhrase+= alpha[DL]
        else:
            DecryptedPhrase+= " "
    PrintDecryptedPhrase(DecryptedPhrase)

def Numbers():
    EncryptedPhrase = args
    DecryptedPhrase = ""
    for i in EncryptedPhrase:
        if i!=" ":
            DL = int(offset)+int(i)-1
            while DL>25:
                DL-=26
            DecryptedPhrase+= alpha[DL]
    PrintDecryptedPhrase(DecryptedPhrase)

def PrintDecryptedPhrase(DP):
    if options.uppercase:
        print(DP.upper())
    else:
        print(DP.lower())

def main():
    if options.numbers:
        Numbers()
    else:
        Letters()

main()
