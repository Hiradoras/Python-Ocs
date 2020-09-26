word = input()
letter= input()

def lettersIndex(word,letter):
    i = 0
    index = -1
    while i < len(word):
        if word[i]==letter:
            index = i
        i+=1
    print("Index: "+str(index))

lettersIndex(word,letter)