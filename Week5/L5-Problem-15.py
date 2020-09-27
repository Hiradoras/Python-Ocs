a = input()
a= a.replace(" ","")
a= a.lower()
letters = list(a)
letters = sorted(letters)
list_to_print = []
for i in range(len(sorted(letters))):
    list_to_print.append(str(letters[i]+": "+str(letters.count(letters[i]))))
list_to_print = list(dict.fromkeys(list_to_print))
list_to_print = sorted(list_to_print)
for i in range(len(list_to_print)):
    print(list_to_print[i])