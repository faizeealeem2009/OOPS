class Points:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False

P1=Points(3,4)
P2=Points(3,4)
if P1==P2:
    print("Same Points")
else:
    print("Different Points")
