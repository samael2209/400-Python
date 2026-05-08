# Desarrolla una función que encuentre la subsecuencia más larga creciente en una lista 
# de números. 

nums = [10,9,2,5,3,7,101,18]

n = len(nums)

dp = [1] * n

prev = [-1] * n

max_index = 0

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            
            prev[i] = j 
    
    if dp[i] > dp[max_index]:
        max_index = i

lis = []

while max_index != -1:
    
    lis.append(nums[max_index])
    
    max_index = prev[max_index]

lis.reverse()

print("DP:", dp)
print("PREV:", prev)
print("LIS:", lis)


from bisect import bisect_left

nums = [10,9,2,5,3,7,101,18]

tails = []

for x in nums:

    # buscar posición
    i = bisect_left(tails, x)

    # si x es mayor que todos
    if i == len(tails):
        tails.append(x)

    # reemplazar
    else:
        tails[i] = x

print(tails)
print("LIS:", len(tails))