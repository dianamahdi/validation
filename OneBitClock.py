from Semantic import *

class OneBitClock(Semantic):
    def __init__(self):
        return [0]

    def actions(self,c):
        a=[]
        if c==1:
            a.append(lambda _:[0])
        elif c==0:
            a.append(lambda _:[1])

        def execute(self,a,c):
            return a(c)