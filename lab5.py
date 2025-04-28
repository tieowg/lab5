import random
arr = [random.randint(-10, 20) for _ in range(10)]
greater_than_10 = [x for x in arr if x > 10]
print(sum(greater_than_10) / len(greater_than_10) if greater_than_10 else "No elements greater than 10")
