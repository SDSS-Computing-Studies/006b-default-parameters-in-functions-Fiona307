[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3353521&assignment_repo_type=AssignmentRepo)
## SDSS Computing Studies Python Assignment
### Assignment #xx <Title> (Total Marks xx)

Objectives:
* Receive multiple return values from a function as a list or tuple
* Have default input parameters in a function
* Create your own module and use dot notation


### Multiple Values in Variable Assignment
Sometimes you, might want to return multiple values from a function.
Normally, a function returns a single variable, but that variable
could include a list or a tuple.
This means that if you know a function will return a list or tuple that 
always contains two values, then you can store those two values into
2 separate variables.
See example1.py

### Default Parameters in Function Definition
A function call requires the correct number of input parameters or
an error will occur, but you can also include optional parameters 
that can be specified by name.  If these are not included in your
function call, then a default value is specified.
see example2.py

### Creating Your Own Module and dot Notation
You may recall that when you needed to do the square root, we used the
math module, and imported it using the command "import math".  All of the
math commands could be used, but we need to include the dot notation. For
example, to use the sqrt function form the math module, we would type:
math.sqrt(x)
We can make our own modules that store our important functions, and import
them for use in other programs.
See example3.py

### 4 Tasks
Note: You will be reating a module called "assignment.py".
All of your functions will be defined in the module, but there
should be no other commands.  You should be importing your commands
from each of your task files.


##### Task 1
Temperature Conversion
In the assignment.py file:
define a function called tempConversion()
It will have one required float parameter called degrees
It will have an optional parameter called unit with a default of C
If the unit is C, convert the degrees into fahrenheight and return the 
fahrenheight as a float
If the unit is F, convert the degrees into celsius and return the 
celsius as a float
All answers should be rounded to 1 decimal place

Test your program in task1.py by importing your assignment.py module
and testing with the command:

Example Command
print( assignment.tempConversion(10, unit="F") )
expects:
-12.2

##### Task 2
Factor Pair
In the assignment.py file:
Define a function called factorPair().
It has 2 required integer inputs:
a number, and a factor
The return value is a sorted list of the 2 factors that multiply to 
make the number

Example Command:
print( factorPair(10,2) )
expects:
[2, 5]

##### Problem 1

The cosine law is used to find the length of a missing side in a triangle
that is not a right triangle.
It uses the formula:
c^2 = a^2 + b^2 - 2*a*b*cos(C)

In the assignment.py file:
define a function called cosineLaw().

The function should take three input parameters, and an optional 4th parameter.
Two of the required parameters are going to be the sides of a triangle
and the 3rd is going to be an angle measurement in degrees
The optional parameter is a boolean True or False called "oppositeSide".
The default will be True.

Calculate the missing side of the triangle using the Cosine Law.  You may need to do
some algebra to isolate your variable.  You will also need to use the quadratic
formula to find the length of the side if it's not side c.

We will use the math module to access a method called math.cos
math.cos will tell us the cosine of an angle if it is in radians,
but since we are entering the angle measure in degrees, 
ou will need to create a function called toRadians()

create the function toRadians()
it will take 1 input value, a float that is the measure of the angle in degrees
The function will convert the measure from degrees to raidans

math.pi radians = 180 degrees

the return value will be a float value that is the angle measure in radians


create a function called quadratic.  The function will require 3 float parameters.
The function will use the quadratic formula to find the solutions to a
quadratic equation in the format ax^2 + bx + c = 0 and will return
a sorted list of the 2 solutions

create a function called solution. The function will require 2 float parameters
as inputs.  Since the quadratic formula will generate 2 answers, one negative and
one positive, this will help us decide which should be the length of the missing side.
Return this value.
(x points) 

