"""
pi=22/7
def circumference(radius):
    circum=2*pi*radius
    print(circum)
def area(radius):
    area=pi*radius**2
    print(area)
circumference(7)
area(7)"""


pi=3.141
def area(r):
    return(pi*r*r)
def circumference(r):
    return(2*pi*r)

r=float(input("Enter radius: "))
b=area(r)
print("Area: ",b)
print("Circumference: ",circumference(r))
