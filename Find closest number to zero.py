nums = [-9,-2,-2,-1,9,1]
minV = nums[0]

for num in nums:
    if abs(num) < abs(minV):
        minV = num
    elif abs(num) == abs(minV) and num > 0:
        minV = num
print(minV)