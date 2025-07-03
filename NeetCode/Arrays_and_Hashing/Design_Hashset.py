class MyHashSet:
    def __init__(self):
        self.list = [False] * 1000001

    def add(self, key):
        self.list[key] = True
        return

    def remove(self, key):
        self.list[key] = False
        return

    def contains(self, key):
        return self.list[key]