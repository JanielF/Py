### Modules ### 

import Basic.my_module as my_module

my_module.sumValues(5,3,1)
my_module.printValue("Hola Python")

from Basic.my_module import sumValues, printValue

sumValues(5,6,1)
printValue("Hola Python")

import math

print(math.pi)
print(math.pow(2,8))

from math import pi as PI_Value

print(PI_Value)