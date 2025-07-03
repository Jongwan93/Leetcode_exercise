class MyHashSet:

    def __init__(self):
        self.my_set = set()

    def add(self, int):
        self.my_set.add(int)

    def remove(self, int):
        self.my_set.remove(int)

    def contains(self, int):
        if int in self.my_set:
            return True
        return False