
#!python3
import assignment

def test1():
  x = assignment.toRadians(30)
  assert round(x,4) == 0.5236

def test2():
  x = assignment.solution([-8.9, 5.3])
  assert x == 5.3

def test3():
  x1,x2 = assignment.quadratic(3,5,-8)
  assert round(x1,2) == -2.67
  assert round(x2,2) == 1

def test4():
  answer = assignment.cosineLaw(6,9,34)
  assert round(answer,1) == 5.2

def test5():
  answer = assignment.cosineLaw(10,3,50,oppositeSide=False)
  assert round(answer,1) == 11.7 
