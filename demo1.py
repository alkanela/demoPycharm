import sys
import math
import datetime
from datetime import date


def main():
    print("1. {0}".format(
        "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky."))
    print("2. Python version is {0}".format(sys.version))
    print("3. Current DateTime is: " + str(datetime.datetime.today()))
    radius = float(input('4. Enter the radius of circle :'))
    circle_area(radius)

    f_name = str(input('5. Enter your First Name:'))
    l_name = str(input('Enter your Last Name:'))
    print("Your Full Name is " + f_name + " " + l_name)

    color_list = ["Red", "Green", "White", "Black"]
    print("6. Colors list is:")
    for i in color_list:
        print("\t" + i)

    d1 = date(2014, 7, 2)
    d2 = date(2014, 7, 11)
    date_diff = d2 - d1
    print("7. Day diff between " + str(d1) + " and " + str(d2) + " is:" + str(date_diff.days))

    sphere_r = 6.0
    sphere_volume = 4 / 3.0 * math.pi * sphere_r ** 3
    print("8. Volume of the sphere with radius " + str(sphere_r) + " is: " + str(sphere_volume))


def circle_area(r):
    circle_area = math.pi * r * r
    print("Area of the circle is : %.2f" % circle_area)


if __name__ == "__main__":
    main()



