seconds = int(input())
print(seconds // 3600, 'часов', (seconds - seconds // 3600 * 3600) // 60, 'минут', seconds - (seconds - seconds // 3600) // 60 * 60, 'секунд')