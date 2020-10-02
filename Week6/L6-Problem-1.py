a = str(input())

inputs = a.split(",")

def largest(nums):
    largest = 0
    current = 0
    for i in nums:
        current = int(i)
        if current>= largest:
            largest = current
    print(largest)

largest(inputs)
