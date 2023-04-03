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

    def __str__(self):
        return f"Punkt ({self.x}, {self.y})"
  
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
    def __init__(self, punkt1, punkt2):
        super().__init__("Rechteck")
        self.A = list(punkt1)
        self.B = list(punkt2)

    def Umfang (self):
        return 2*(abs(self.A[0]-self.B[0]+self.A[1]-self.B[1]))

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
    
class Polygon(Figur):
    def __init__(self, *args):
        super().__init__("Polygon")
        self.args = args

    def Umfang(self):
        umfang = 0
        for i in range(len(self.args)):
            aktuellerpkt = self.args[i]
            naechsterpkt = self.args[(i+1) % len(self.points)]
            umfang += math.sqrt((naechsterpkt.x - aktuellerpkt.x)**2 + (naechsterpkt.y - aktuellerpkt.y)**2)
        return umfang


d =  Kreis(Punkt(2,3), 5, 8)

print(d.Umfang())
print(d.__str__())

#salami = Polygon(Punkt(3,4), Punkt(5,6))
#umfang = salami.Umfang()

#print(umfang)



