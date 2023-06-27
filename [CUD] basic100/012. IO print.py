num1 = int(input())
num2 = int(input())
print(num1)
print(num2)

# # Optional
num1, num2 = map(int, input().split())
print(f"{num1}\n{num2}")

# FYI
# 3, 5 > ['3,', '5']
# 3 5 > ['3', '5']
