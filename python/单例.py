class Sb:

    __instance = None

    def __init__(self):
        self.name = 'jeff'
        self.age = 22

    @staticmethod
    def get_instance():
        if Sb.__instance:
            return Sb.__instance
        else:
            Sb.__instance = Sb()
            return Sb.__instance

    def sbmth(self):
        pass

obj1 = Sb.get_instance()
print(obj1)
obj2 = Sb.get_instance()
print(obj2)
obj3 = Sb.get_instance()
print(obj3)
