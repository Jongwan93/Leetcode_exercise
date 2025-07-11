class MyHashMap:

    def __init__(self):
        self.dict = {}

    def put(self, key, value):
        self.dict[key] = value

    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return -1

    def remove(self, key):
        if key in self.dict:
            del self.dict[key] # self.dict[key] = 0 will make key remain and return 0.
            # requirement is [null,null,null,1,-1,null,1,null,-1]