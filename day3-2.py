import utils 
import re
import day3shared

grid = day3shared.Grid(utils.load_lines("day3.txt"))
#grid.printgears()

for (y,row) in enumerate(grid.lines):
    number_matches = list(re.finditer(r'\d+',row))
    for match in number_matches:
        val = int(match.group())
        for cellx in range(match.start()-1,match.end()+1):        
            for yo in range(-1,2):
                celly = y+yo 
                if cellx >= 0 and cellx < grid.width and celly >= 0 and celly < grid.height and grid.gears[celly][cellx]!=None:
                    grid.gears[celly][cellx].append(val)

total = 0
for row in grid.gears:
    for cell in row:
        if cell and len(cell) >= 2:
            product = 1
            for val in cell:
                product *= val 
            total += product

print(total)