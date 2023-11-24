# def setup():
#     size(400,400)
#     frameRate(5)
# def draw():
#     fill(random(200,255))
#     ellipse(random(1,400),random(1,400),random(1,15),random(1,15))

# def setup():
#     size(400,400)
#     frameRate(1)
# def draw():
#     ellipse(200,200,800,800)
#     ellipse(200,200,random(1,200),random(1,200))

# def setup():
#     size(400,400)
#     frameRate(5)
# def draw():
#     stroke(random(0,255),random(0,255),random(0,255))
#     line(200,0,random(0,400),random(0,400))
# dira = 1
# a = 25
# b = 500
# def setup():
#     size(1000,1000)
#     frameRate(10000)
# def draw():
#     global a
#     global b
#     global dira
#     fill(random(0,255),random(0,255),random(0,255))
#     stroke(random(0,255),random(0,255),random(0,255))
#     a = a + dira
#     background(200)
#     ellipse(b,a,50,50)
#     if a > 950:
#         dira = -1
#         b = (random(0,1000))
#     if a < 25:
#         dira = 1
#         b = (random(0,1000))

# def setup():
#     size(1000,1000)
#     frameRate(5)
# def draw():
#     fill(random(0,255),random(0,255),random(0,255))
#     background(102,164,247)
#     triangle(470,500,530,500,500,random(0,490))
#     triangle(450,470,450,530,random(0,440),500)
#     triangle(550,470,550,530,random(550,990),500)
#     textSize(50)
#     fill(50)
#     text(u'ГОНКИ!',400,700)
#     textSize(20)
#     text(u'Конфетное обновление!',380,800)
#     fill(1)
#     ellipse(500,600,90,50)
#     fill(255,5,9)
#     text(u'Играть!',465,605)
