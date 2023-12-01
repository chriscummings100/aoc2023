

def load_text(name: str) -> str:
    with open(f"data/{name}","r") as f:
        return f.read()

def load_lines(name: str) -> str:
    with open(f"data/{name}","r") as f:
        return [x.strip() for x in f.readlines()]
    

