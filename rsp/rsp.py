import random,json

class abc:
    jacch =["1","2","3"]

    def __init__(self):
        self.jacch=["1","2","3"]
        #pass

    def add(self):
        self.jacch.append("4")

    def dba(self):
        print("hello")
        print(self.jacch)
        


a=abc()
a.add()
a.add()
a.add()
a.dba()

b=abc()
b.add()
b.dba()


c=abc()
b.add()
c.dba()


b.dba()