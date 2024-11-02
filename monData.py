class MonData:
    def __init__(self, name: str):
        self.name = name
        self.stats = [0, 0, 0, 0, 0, 0]
    
    def __str__(self):
        return self.name
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)