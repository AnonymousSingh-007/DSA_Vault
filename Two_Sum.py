#Brute Force Approach
a = [2,7,11,15]
target = 9
for i in range (len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == target:
            print(i, j)
      
#optimized appraoch
num = [2, 7, 11, 15]
tar = 9
dict = {}
for i, num in enumerate(num):
    diff = target - num
    if diff in dict:
        print(dict[diff], i)
    dict[num] = i
        

            