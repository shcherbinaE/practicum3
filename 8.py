import math

a = int(input())
b = int(input())
c = int(input())
print(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))
print(math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))))
print(math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * b * a))))