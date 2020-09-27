a = input()
list_input = a.split(",")
nums = []
for i in range(len(list_input)):
    nums.append(int(list_input[i]))

def listOddEven(nums):
    odds = []
    evens = []

    for i in range(len(nums)):
        if nums[i]%2==0:
            evens.append(nums[i])
        else:
            odds.append(nums[i])

    odds.sort()
    evens.sort()
    print(odds)
    print(evens)


listOddEven(nums)
