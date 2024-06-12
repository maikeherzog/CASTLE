class HeapElement:
    def __init__(self, dist, tuple):
        self.dist = dist
        self.tuple = tuple

    def __lt__(self, other):
        return self.dist < other.dist
