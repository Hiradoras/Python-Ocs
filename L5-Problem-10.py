def oddTuple(tup):
    new_list = []
    list_input = list(tup)
    for i in range(len(list_input)):
        if i%2==0:
            new_list.append(list_input[i])
    print(tuple(new_list))

input_list = []

line = input()

input_list = line.split(" ")

tup_input = tuple(input_list)

oddTuple(tup_input)
