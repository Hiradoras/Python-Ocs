a = input()
b = a.strip()
list_input = b.split(" ")

list_int = []

for i in range(len(list_input)):
    list_int.append(int(list_input[i]))

def sorted(numbers):
    numbers.sort()
    print(numbers)


sorted(list_int) 