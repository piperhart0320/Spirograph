import turtle as t
import math 

def main():
    spirograph_animation()
    t.clearscreen()
    flower()
    t.clearscreen()
    atom()
    


def flower():
    t.speed(10)
    spirograph5()
    color()
    spirograph()
    spirograph4()
    color2()
    spirograph2()
    color3()
    spirograph3()
    t.exitonclick
   

def color():
    t.pencolor('pink')
    t.width(10)

def color2():
    t.pencolor('green')
    t.width(3)

def color3():
    t.pencolor('yellow')
    t.width(5)

def circle():
    #t.left(90)
    
    t.circle(20)

def spirograph():
    time = 0
    max = 2 * math.pi
    r = 193
    R = 300
    p = 84
    t.penup()
    t.goto(((R-r) + p), 0)
    t.pendown()
    for _ in range(750):
        time += 0.1

        x = ((R - r) * math.cos(time)) + (p * math.cos(((R - r) / r) * time))
        y = ((R - r) * math.sin(time)) - (p * math.sin(((R - r) / r) * time))
        
        t.goto(x, y)
        
def spirograph2():
    time = 0
    max = 2 * math.pi
    r = 13
    R = 50
    p = 5
    t.penup()
    t.goto(((R-r) + p), 0)
    t.pendown()
    for _ in range(400):
        time += 0.1

        x = ((R - r) * math.cos(time)) + (p * math.cos(((R - r) / r) * time))
        y = ((R - r) * math.sin(time)) - (p * math.sin(((R - r) / r) * time))
        
        t.goto(x, y)
        
def spirograph3():
    time = 0
    max = 2 * math.pi
    r = 37
    R = 40
    p = 23
    t.penup()
    t.goto(((R-r) + p), 0)
    t.pendown()
    for _ in range(880):
        time += 0.1

        x = ((R - r) * math.cos(time)) + (p * math.cos(((R - r) / r) * time))
        y = ((R - r) * math.sin(time)) - (p * math.sin(((R - r) / r) * time))
        
        t.goto(x, y)
        
def spirograph4():
    t.pencolor('magenta')
    t.width(3)
    time = 0
    max = 2 * math.pi
    r = 192
    R = 300
    p = 84
    t.penup()
    t.goto(((R-r) + p), 0)
    t.pendown()
    for _ in range(750):
        time += 0.1

        x = ((R - r) * math.cos(time)) + (p * math.cos(((R - r) / r) * time))
        y = ((R - r) * math.sin(time)) - (p * math.sin(((R - r) / r) * time))
        
        t.goto(x, y)
        
def spirograph5():
    t.pencolor('orange')
    t.width(50)
    time = 0
    max = 2 * math.pi
    r = 193
    R = 300
    p = 84
    t.penup()
    t.goto(((R-r) + p), 0)
    t.pendown()
    for _ in range(750):
        time += 0.1

        x = ((R - r) * math.cos(time)) + (p * math.cos(((R - r) / r) * time))
        y = ((R - r) * math.sin(time)) - (p * math.sin(((R - r) / r) * time))
        
        t.goto(x, y)




def atom():
    t.speed(10)
    sp2()
    nuetrons()
    sp()

def sp2():
    t.pencolor('green')
    time = 0
    max = 2 * math.pi
    r = 13
    R = 50
    p = 5
    t.penup()
    t.goto(((R-r) + p), 0)
    t.pendown()
    for _ in range(750): 
        time += 0.1

        x = ((R - r) * math.cos(time)) + (p * math.cos(((R - r) / r) * time))
        y = ((R - r) * math.sin(time)) - (p * math.sin(((R - r) / r) * time))
        
        t.goto(x, y)

def sp():
    t.shape('circle')
    t.pencolor('red')
    time = 0
    max = 2 * math.pi
    r = 193
    R = 350
    p = 84
    t.penup()
    t.goto(((R-r) + p), 0)
    t.pendown()
    for _ in range(750):
        time += 0.1

        x = ((R - r) * math.cos(time)) + (p * math.cos(((R - r) / r) * time))
        y = ((R - r) * math.sin(time)) - (p * math.sin(((R - r) / r) * time))
        
        t.goto(x, y)

def nuetrons():
    t.pencolor('yellow')
    t.right(180)
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.pendown()
    t.width(4)
    t.circle(10)
    t.width(1)



def spirograph_animation():
    spirograph_real()
    blue()
    pink2()

def spirograph_real():
    t.speed(0)
    t.pencolor('green')
    time = 0
    max = 2 * math.pi
    r = 127
    R = 303
    p = 54
    t.penup()
    t.goto(((R-r) + p), 0)
    t.pendown()
    for _ in range(2000): 
        time += 0.1

        x = ((R - r) * math.cos(time)) + (p * math.cos(((R - r) / r) * time))
        y = ((R - r) * math.sin(time)) - (p * math.sin(((R - r) / r) * time))
        
        t.goto(x, y)

def blue():
    t.speed(0)
    t.pencolor('blue')
    time = 0
    max = 2 * math.pi
    r = 128
    R = 303
    p = 57
    t.penup()
    t.goto(((R-r) + p), 0)
    t.pendown()
    for _ in range(1500): 
        time += 0.1

        x = ((R - r) * math.cos(time)) + (p * math.cos(((R - r) / r) * time))
        y = ((R - r) * math.sin(time)) - (p * math.sin(((R - r) / r) * time))
        
        t.goto(x, y)

def pink2():
    t.speed(0)
    t.pencolor('magenta')
    time = 0
    max = 2 * math.pi
    r = 128
    R = 303
    p = 57
    t.penup()
    t.goto(((R-r) + p), 0)
    t.pendown()
    for _ in range(1500): 
        time += 0.1

        x = ((R - r) * math.cos(time)) + (p * math.cos(((R - r) / r) * time))
        y = ((R - r) * math.sin(time)) - (p * math.sin(((R - r) / r) * time))
        
        t.goto(x, y)



    
if __name__ == "__main__":
    main()
