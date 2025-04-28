import random
n = int(input())
arr = [random.randint(4, 47) for _ in range(n)]
b = [x for x in arr if x % 3 == 1]
print(eval('*'.join(map(str, b))) if b else "Yoxdur")
