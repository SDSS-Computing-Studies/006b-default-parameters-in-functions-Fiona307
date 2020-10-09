#! python3

import math

def tempConversion(degree, unit = "C"):
    answer = round((9*float(degree)/5 + 32),1)
    if unit == "F":
        answer = round((float(degree) - 32)*5/9,1)
    return answer

def factorPair(num,a):
    b = num/a
    answer = [a,b]
    answer.sort()
    return answer


#def cosineLaw():

#def convertAngle():

#def solution():

#def quadratic():

