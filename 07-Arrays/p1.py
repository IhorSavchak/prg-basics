###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print(arr[-1])
print(arr[-2])
print(arr[-1] + arr[0])
print(arr[-3])

result = ""
for i in arr:
    result += str(i) + " "

print(result)