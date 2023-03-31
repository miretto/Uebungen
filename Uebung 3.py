import math

class Figur:
    def __init__(self, name):
        self.name = name

    def Umfang(self):
        return 0
    
    def __str__(self):
        return self.name

class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y
   
class Dreieck(Figur):
    def __init__(self, ax, ay, bx, by, cx, cy):
        super().__init__("Dreieck")
        self.A = Punkt(ax,ay)
        self.B = Punkt(bx,by)
        self.C = Punkt(cx,cy)

        self.a = abs(((ax-bx)**2 +(ay-by)**2)**0.5)
        self.b = abs(((bx-cx)**2 +(by-cy)**2)**0.5)
        self.c = abs(((cx-ax)**2 +(cy-ay)**2)**0.5)

    def Umfang(self):
        return self.a + self.b + self.c
    
    def __str__(self):
        return f"Dreieck mit den Seitenlängen {self.a}, {self.b}, {self.c}"


class Rechteck(Figur):
    def __init__(self, ax, ay, bx, by):
        super().__init__("Rechteck")
        self.A = Punkt(ax,ay)
        self.B = Punkt(bx,by)

        self.x = abs(ax-bx)
        self.y = abs(ay-by)

    def Umfang (self):
        return 2*(self.x + self.y)
    
    def __str__(self):
        return f"Rechteck mit den Seitenlängen {self.x}, {self.y}"

class Kreis(Figur):
    def __init__(self, mx, my, radius):
        super().__init__("Kreis")
        self.punktkoord = Punkt(mx,my)
        self.radius = radius

        self.mittelpunkt = (mx,my)

    def Umfang(self):
        return 2*math.pi*self.radius

    def __str__(self):
        return f"Kreis M={self.mittelpunkt} r={self.radius}"
    

d = Kreis(4,6,8)

print(d.__str__())

z = Rechteck(4,5,6,7)

print(z.__str__())


test ob es klappt