import utils 
import re
import day3shared

grid = day3shared.Grid(utils.load_lines("day3.txt"))

grid.printnearbygrid()

total = 0
for (y,row) in enumerate(grid.lines):
    number_matches = list(re.finditer(r'\d+',row))
    for match in number_matches:
        if grid.israngenearsymbol(match.start(),match.end(),y):
            #print(match.group())
            total += int(match.group())
print(total)
