#Create a Python program that computes the area of a circle

def area_of_the_circle(Radius):
    area = 3.14*Radius**2
    return area

Radius = float(input(" Please enter the radius of circle: "))
print(" The area of the circle is: ", area_of_the_circle(Radius))
