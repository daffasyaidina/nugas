from kelasbundar import *

def main():
    cyl = Cylinder(1, "Red", 1)
    print(f"Radius is {cyl.getRadius()}")
    print(f"Height is {cyl.getHeight()}")
    print(f"Color is {cyl.getColor()}")
    print(f"Area is {'{:.2f}'.format(cyl.getArea())}")
    print(f"Volume is {'{:.2f}'.format(cyl.getVolume())}")
    cyl.setRadius(2)
    cyl.setHeight(2)
    cyl.setColor("Blue")
    print(f"New Radius is {cyl.getRadius()}")
    print(f"New Color is {cyl.getColor()}")
    print(f"New Area is {'{:.2f}'.format(cyl.getArea())}")
    print(f"New Volume is {'{:.2f}'.format(cyl.getVolume())}")

main()