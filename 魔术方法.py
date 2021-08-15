class Entity:
    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def my(self):
        print(self.x)

    def __call__(self, x, y):
        '''改变实体的位置'''
        self.x, self.y = x, y

Entity(1, 2, 3).my()
