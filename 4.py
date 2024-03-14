x, y, n = map(int,input().split())
print(x * n + y * n // 100, 'рублей', y * n % 100, 'копеек')