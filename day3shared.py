def isnumeric(val: str|None)->bool:
    return val and val >= '0' and val <= '9'

def issymbol(val: str|None)->bool:
    return val and val != '.' and not isnumeric(val)

class Grid:

    lines: list[str]
    width: int 
    height: int
    gears: list[list[list|None]]

    def __init__(self, lines: list[str]) -> None:
        self.lines = lines
        self.width = len(lines[0])
        self.height = len(lines[1])
        self.gears = [self._loadgears(x) for x in lines]

    def _loadgears(self, line: str):
        return [([] if x=='*' else None) for x in line]

    def get(self, x: int, y: int) -> str | None: 
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            return self.lines[y][x]
        else:
            return None

    def issymbol(self, x: int, y: int):
        char = self.get(x,y)
        return issymbol(char) 
        
    def isnearsymbol(self, x: int, y: int) -> bool:
        for xo in range(-1,2):
            for yo in range(-1,2):
                if self.issymbol(x+xo,y+yo):
                    return True 
        return False
    
    def israngenearsymbol(self, xstart: int, xend: int, y: int) -> bool:
        for x in range(xstart, xend):
            if self.isnearsymbol(x,y):
                return True 
        return False

    def printnearbygrid(self):
        for (y,row) in enumerate(self.lines):
            print(row + '    ' + ''.join([('X' if self.isnearsymbol(x,y) else '.') for x in range(0,self.width)]))

    def printgears(self):
        for (y,row) in enumerate(self.lines):
            print(row + '    ' + ''.join([('X' if self.gears[y][x]!=None else '.') for x in range(0,self.width)]))

