
vowel = ['a','e','i','o','u']

def DecodeWord(word):
    for i in range(0,len(word),1):
        if i < len(word):
            if word[i] in vowel:
                del word[i+1]
                del word[i]
    return ("".join(word))

def main():
    phrase = input()
    phrase = phrase.split(" ")
    DecodedPhrase = []
#    print(phrase)
    for i in range(0,len(phrase),1):
        DecodedPhrase.append(DecodeWord(list(phrase[i])))

    Newphrase = " ".join(DecodedPhrase)
    print(Newphrase)

if __name__ =="__main__":
    main()
