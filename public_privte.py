class HasPrivate:
    def __init__(self):
        self.public = "Public."
        self.__private = "Private." # private 은 _ 밑줄 두개가 접두사  

    def Print_massge(self):
        print(self.public)
        print(self.__private)


obj = HasPrivate()
obj.Print_massge

print(obj.public)
print(obj._private) #private로 선언하면 클래스내에서만 사용가능