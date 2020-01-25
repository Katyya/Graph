from graph import *
windowSize(1000,900)
canvasSize(1000,900)
brushColor(101,199,208)
rectangle(0,0,1000,400)
brushColor(0,0,255)
rectangle(0,400,1000,650)
brushColor(202,208,101)
rectangle(0,650,1000,900)
penColor(202,208,101)
x=0
for i in range(9):
    circle(50+x,680,60)
    x+=200
brushColor(0,0,255)
penColor(0,0,255)
y=0
for i in range(9):
    circle(150+y,610,60)
    y+=200
def sun():
    penColor(255, 243, 67)
    brushColor(255, 243, 67)
    circle(800, 150, 100)
    

def clouds(x,y,r):
    brushColor(255, 255, 255)
    penColor(0, 0, 0)
    penSize(1)
    circle(x , y , r)
    circle(x-r, y+r, r)
    circle(x+r, y, r)
    circle(x , y+r, r)
    circle(x+r, y + r, r)
    circle(x + (2*r), y, r)
    circle(x + ((7 * r)/3), y+r, r)

def bord():
    brushColor("Brown")
    penColor(0, 0, 0)
    circle(250,450,50)
    rectangle(250, 450, 450, 500)
    brushColor(0, 0, 255)
    penColor(0, 0, 255)
    rectangle(200, 400, 300, 450)
    brushColor("Brown")
    polygon ( [(450,450), (540,450), (450,500)] )
    penColor(0, 0, 0)
    brushColor(255,255,255)
    penSize(5)
    circle(480, 465, 10)
    brushColor(0,0,0)
    rectangle(350, 200, 365, 450)
    penSize(1)
    brushColor(153, 133, 120)
    polygon([(365, 200), (450, 325), (390, 325)])
    polygon([(365, 450), (450, 325), (390, 325)])

def sun_unbrella():
    brushColor("Brown")
    penColor(0, 0, 0)
    rectangle(120, 850, 130, 580)
    h=0
    for i in range(5):
        polygon([(125, 580), (30+h, 650), (70+h, 650)])
        h+=40

sun()
clouds(220,150,30)
clouds(470,100,40)
bord()
sun_unbrella()

run()