#!/usr/bin/env python3
'''Assignment 4 Part 1'''

from typing import IO
import random

class GenRandom:
    '''GenRandom class'''

    def __init__(self, count: int):
        self.count: int = count
        random.seed()
        self.table: list[tuple] = []
        for i in range(0, self.count):
            current: ArtConfig = ArtConfig(random.randrange(0, 3), (random.randrange(500+i, i + 502), random.randrange(i + 200, i + 202)), 
                      random.randrange(0, 101), (random.randrange(10, 31), random.randrange(10, 31)), 
                      (random.randrange(10, 101), random.randrange(10, 101)), 
                      (random.randrange(200, 256), random.randrange(200, 256), random.randrange(0, 25)), 
                      random.uniform(0.0, 0.35))
            self.table.append((i, current))

class ArtConfig:
    '''ArtConfig class'''
    def __init__(self, shapeType: int, coordinates: tuple, radius: int, ellipseR: tuple, rectangleSize: tuple, color: tuple, opacity: float):
        self.shapeType: int = shapeType
        self.x: int = coordinates[0]
        self.y: int = coordinates[1]
        self.radius: int = radius
        self.RX: int = ellipseR[0]
        self.RY: int = ellipseR[1]
        self.width: int = rectangleSize[0]
        self.height: int = rectangleSize[1]
        self.red: int = color[0]
        self.green: int = color[1]
        self.blue: int = color[2]
        self.opacity: float = opacity

class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def drawCircleLine(self, f: IO[str], t: int):
        '''drawCircle method'''
        ts: str = "   " * t
        line: str = f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.rad}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></circle>'
        f.write(f"{ts}{line}\n")

class Rectangle:
    '''Rectangle class'''
    def __init__(self, rec: tuple, col: tuple):
        self.x: int = rec[0]
        self.y: int = rec[1]
        self.width: int = rec[2]
        self.height: int = rec[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def drawRectangleLine(self, f: IO[str], t: int):
        '''drawRectangle method'''
        ts: str = "   " * t
        line: str = f'<rect x ="{self.x}" y ="{self.y}" width="{self.width}" height="{self.height}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></rect>'
        f.write(f"{ts}{line}\n")

class Ellipse:
    '''Ellipse class'''
    def __init__(self, ell: tuple, col: tuple):
        self.cx: int = ell[0]
        self.cy: int = ell[1]
        self.rx: int = ell[2]
        self.ry: int = ell[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def drawEllipseLine(self, f: IO[str], t: int):
        '''drawEllipse method'''
        ts: str = "   " * t
        line: str = f'<ellipse cx ="{self.cx}" cy ="{self.cy}" rx="{self.rx}" ry="{self.ry}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></ellipse>'
        f.write(f"{ts}{line}\n")

class ProEpilogue:
    '''ProEpilogue class'''
    def __init__(self, title: str, canvas: tuple, fnam, shapeCount, randomConfigs):
        self.title: str = title
        self.svgWidth: int = canvas[0]
        self.svgHeight: int = canvas[1]
        self.fileName: str = fnam
        self.shapeCount = shapeCount
        self.randomConfigs = randomConfigs
        
    def writeHTMLcomment(f: IO[str], t: int, com: str):
        '''writeHTMLcomment method'''
        ts: str = "   " * t
        f.write(f'{ts}<!--{com}-->\n')

    def openSVGcanvas(f: IO[str], t: int, canvas: tuple):
        '''openSVGcanvas method'''
        ts: str = "   " * t
        ProEpilogue.writeHTMLcomment(f, t, "Define SVG drawing box")
        f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

    def closeSVGcanvas(f: IO[str], t: int):
        '''closeSVGcanvas method'''
        ts: str = "   " * t
        f.write(f'{ts}</svg>\n')
        f.write(f'</body>\n')
        f.write(f'</html>\n')

    def writeHTMLline(f: IO[str], t: int, line: str):
        '''writeLineHTML method'''
        ts = "   " * t
        f.write(f"{ts}{line}\n")

    def writeHTMLHeader(f: IO[str], title: str):
        '''writeHeadHTML method'''
        ProEpilogue.writeHTMLline(f, 0, "<html>")
        ProEpilogue.writeHTMLline(f, 0, "<head>")
        ProEpilogue.writeHTMLline(f, 1, f"<title>{title}</title>")
        ProEpilogue.writeHTMLline(f, 0, "</head>")
        ProEpilogue.writeHTMLline(f, 0, "<body>")

    def writeHTMLfile(self):
        '''writeHTMLfile method'''
        f: IO[str] = open(self.fileName, "w")
        ProEpilogue.writeHTMLHeader(f, self.title)
        ProEpilogue.openSVGcanvas(f, 1, (self.svgWidth,self.svgHeight))
        genArt(f, 2, self.randomConfigs, self.shapeCount)
        ProEpilogue.closeSVGcanvas(f, 1)
        f.close()
        
def genArt(f: IO[str], t: int, randomConfigurations: GenRandom, count: int):
    '''genART method'''
    for i in range(0, count):
        if(randomConfigurations.table[i][1].shapeType == 0):
            Circle((randomConfigurations.table[i][1].x,randomConfigurations.table[i][1].y,randomConfigurations.table[i][1].radius), 
                   (randomConfigurations.table[i][1].red,randomConfigurations.table[i][1].green,randomConfigurations.table[i][1].blue
                   ,randomConfigurations.table[i][1].opacity)).drawCircleLine(f, t)
        elif(randomConfigurations.table[i][1].shapeType == 1):
           Rectangle((randomConfigurations.table[i][1].x,randomConfigurations.table[i][1].y,randomConfigurations.table[i][1].width, randomConfigurations.table[i][1].height), 
                   (randomConfigurations.table[i][1].red,randomConfigurations.table[i][1].green,randomConfigurations.table[i][1].blue
                   ,randomConfigurations.table[i][1].opacity)).drawRectangleLine(f, t)
        else:
            Ellipse((randomConfigurations.table[i][1].x,randomConfigurations.table[i][1].y,randomConfigurations.table[i][1].RX, randomConfigurations.table[i][1].RY), 
                   (randomConfigurations.table[i][1].red,randomConfigurations.table[i][1].green,randomConfigurations.table[i][1].blue
                   ,randomConfigurations.table[i][1].opacity)).drawEllipseLine(f, t)

def main():
    '''main method'''
    shapeCount: int = 500 #number of shapes to generate
    randomConfigurations: GenRandom = GenRandom(shapeCount)
    ProEpilogue("My Art", (1920,1080), "a43.html", shapeCount, randomConfigurations).writeHTMLfile()

main()

                                                                                                                                                                                                                                                                                                        
