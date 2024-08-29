def square(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5]
# [1, 4, 9, 16, 25]
squares = list(map(square, numbers))
print(f"squares={squares}")

