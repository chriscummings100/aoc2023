import day2shared

games = day2shared.load('day2.txt')

print(sum([x.power() for x in games]))