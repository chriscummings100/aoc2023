import utils
import re

class Draw:
    def __init__(self, match_tuple) -> None:
        self.count = int(match_tuple[0])
        self.color = match_tuple[1]
    def __str__(self) -> str:
        return f"{self.count} {self.color}"

class Round:
    def __init__(self, roundtext) -> None:
        self.draws = [Draw(x) for x in re.findall(r'(\d+)\s(\w+)',roundtext)]
        pass

    def __str__(self) -> str:
        return ','.join([str(x) for x in self.draws])
    
    def totals(self):
        res = {'red':0,'green':0,'blue':0}
        for x in self.draws:
            res[x.color] += x.count
        return res

class Game:
    def __init__(self, line) -> None:
        [gametext,roundstext] = [x.strip() for x in line.split(":")]
        self.game = int(re.findall(r'(\d+)', gametext )[0])
        self.rounds = [Round(x) for x in roundstext.split(";")]

    def __str__(self) -> str:
        return f"Game {self.game}: {';'.join([str(x) for x in self.rounds])}"
    
    def maxes(self):
        res = {'red':0,'green':0,'blue':0}
        for x in self.rounds:
            totals = x.totals()
            res['red'] = max(res['red'],totals['red'])
            res['green'] = max(res['green'],totals['green'])
            res['blue'] = max(res['blue'],totals['blue'])
        return res
    
    def power(self):
        m = self.maxes()
        return m['red']*m['green']*m['blue']

def load(fn: str):
    lines = utils.load_lines(fn)
    return [Game(x) for x in lines]
