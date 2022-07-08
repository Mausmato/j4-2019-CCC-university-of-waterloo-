n = input()

nums = [[1,2], [3,4]]

def HoriFlip(nums):
    nums[0],nums[1] = nums[1],nums[0]

def VertFlip(nums):
    top = [nums[0][1], nums[0][0] ]
    bot = [nums[1][1] , nums[1][0] ]
    nums[1] = bot
    nums[0] = top
    

for i in range(len(n)):
    if n[i] == "H":
        HoriFlip(nums)
    else:
        VertFlip(nums)


for i in nums:
    for x in i:
        print(x, end=" ")
    print(' ')
