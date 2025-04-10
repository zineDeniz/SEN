import turtle

# Ekran ayarları
pencere = turtle.Screen()
pencere.title("SEN Kalbi")
pencere.bgcolor("black")

# Kalp çizimi için turtle
kalp = turtle.Turtle()                                                                                                                                     
kalp.hideturtle()
kalp.pensize(5)
kalp.color("#FF4C4C")  # Kalp çizgi rengi
kalp.speed(2)

# Kalbi çiz
kalp.penup()
kalp.goto(0, -200)
kalp.pendown()
kalp.left(140)
kalp.forward(300)
kalp.circle(-150 , 199.1)
kalp.left(120)
kalp.circle(-150 , 199.1)
kalp.forward(300)

# "SEN" yazısı için turtle
yazi = turtle.Turtle()
yazi.hideturtle()
yazi.color("white")
yazi.penup()
yazi.goto(0, 1)  # Yazıyı kalbin üst kısmına hizala
yazi.write("SEN", align="center", font=("Courier", 60, "bold"))

turtle.done()