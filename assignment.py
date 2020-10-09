#! python3

import math

def tempConversion(degree, unit = "C"):
    answer = round((9*float(degree)/5 + 32),1)
    if unit == "F":
        answer = round((float(degree) - 32)*5/9,1)
    return answer

def factorPair(num,a):
    b = int(num/a)
    answer = [a,b]
    answer.sort()
    return answer


def cosineLaw(x,y,angle,oppositeSide = True):
    z = math.sqrt(float(x)**2 + float(y)**2 - 2*float(x)*float(y)*math.cos(angle))
    return z
    if oppositeSide == False:
        #if y = the oppositeSide
        a = 1
        b = 2*float(x)*math.cos(angle)
        c = float(x)**2 - float(y)**2
        d = (a,b,c)
        #if x = the oppositeSide
        m = 1
        n = 2*float(y)*math.cos(angle)
        p = float(y)**2 - float(x)**2
        q = (m,n,p)
        return d,q
# c^2 = a^2 + b^2 - 2abcosC
# a^2 - 2abcosC + b^2 - c^2 = 0

def convertAngle(degree):
    angle = math.pi*float(degree)/180
    return angle

def quadratic(a,b,c):
    x1 = (-float(b) + math.sqrt(float(b)**2 - 4*float(a)*float(c)))/(2*float(a))
    x2 = (-float(b) - math.sqrt(float(b)**2 - 4*float(a)*float(c)))/(2*float(a))
    solution = [x1,x2]
    solution.sort()
    return solution

def solution(x1,x2):
    if x1 > 0:
        answer = x1
    elif x2 > 0:
        answer = x2
    return answer

print(convertAngle(30))