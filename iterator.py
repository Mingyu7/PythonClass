class MyRange:
    def __init_(self,start,end):
        self.current=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<self.end:
            current = self.current
            self.current+=1
            return current
        else:
            raise StopIteration()

for i in MyRange(0,5): #0~5까지 출력
    print(i)