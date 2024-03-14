n = int(input())
c = int(input())
k = int(input())
print('страница', k // (n * c) + 1, 'столбец', (k - (k // (n * c)) * n * c) // n + 1, 'строка', (k - (k // (n * c)) * n * c) - (k - (k // (n * c)) * n * c) // n * n)