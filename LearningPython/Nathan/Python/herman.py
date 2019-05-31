#!/bin/python3

import math

def TaxiCabGeometry(radius):
    C = 4*radius
    pi = C/(2*radius)
    area = pi*radius**2
    return area

def EuclidianGeometry(radius):
    return math.pi*radius**2

def main():
    R = float(input())
    TCG = TaxiCabGeometry(R)
    EG = EuclidianGeometry(R)
    print("%.4f" % EG)
    print("%.4f" % TCG)

if __name__=="__main__":
    main()
