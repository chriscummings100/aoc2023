import day2shared

games = day2shared.load('day2.txt')

sum = 0
for x in games:
    print(x)
    maxes = x.maxes()
    print(maxes)
    if maxes['red'] <= 12 and maxes['green'] <= 13 and maxes['blue'] <= 14:
        sum += x.game

print(sum)
    