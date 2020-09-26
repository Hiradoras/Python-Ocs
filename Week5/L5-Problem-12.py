word = input()
letters = input()

letter_list = letters.split(",")

def avoids(words, list):
    forbidden = 0
    for i in range(len(list)):
        for z in range(len(words)):
            if words[z] == list[i]:
                forbidden+=1
    if forbidden==0:
        print("True")
    else:
        print("False")


avoids(word, letter_list)