class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self, other):
        return Vector(self.x*other.x,self.y*other.y)
    def __eq__(self, value):
        return self.x==value.x and self.y==value.y
    def __repr__(self):
        return f"Vector({self.x},{self.y})"

v1=Vector(2,3)
v2=Vector(3,4)
print(v1+v2)