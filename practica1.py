from turtle import *

'''
cuadrado

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(360)
right(360)
right(360)
'''
#triangulo
'''
left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
'''
#pentafgono
'''
left(72)
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
'''
#hexagono
'''
left(60)
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)
'''
lados = 4
lados2 = 3
lados3 = 5
def figura ():
    pass

for i in range(lados):
    forward(100)
    left(360/lados)
for i in range(lados2):
    forward(100)
    left(360/lados2)
for i in range(lados3):
    forward(100)
    left(360/lados3)    
done()
