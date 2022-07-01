#!/usr/bin/env python3
'''Assignment 4 Part 1'''

from typing import IO

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

class ProEpilogue:
    def __init__(self, title: str, canvas: tuple, fnam):
        self.title: str = title
        self.svgWidth: int = canvas[0]
        self.svgHeight: int = canvas[1]
        self.fileName: str = fnam
        
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
        genArt(f, 2)
        ProEpilogue.closeSVGcanvas(f, 1)
        f.close()
        
def genArt(f: IO[str], t: int):
   '''genART method'''
   Circle((50,50,50), (255,0,0,1.0)).drawCircleLine(f, t)
   Circle((150,50,50), (255,0,0,1.0)).drawCircleLine(f, t)
   Circle((250,50,50), (255,0,0,1.0)).drawCircleLine(f, t)
   Circle((350,50,50), (255,0,0,1.0)).drawCircleLine(f, t)
   Circle((450,50,50), (255,0,0,1.0)).drawCircleLine(f, t)

   Rectangle((0,250,100,50),(0,0,255,1.0)).drawRectangleLine(f, t)
   Rectangle((100,250,100,50),(255,0,0,1.0)).drawRectangleLine(f, t)
   Rectangle((200,250,100,50),(0,255,0,1.0)).drawRectangleLine(f, t)
   Rectangle((300,250,100,50),(0,0,255,1.0)).drawRectangleLine(f, t)
   Rectangle((400,250,100,50),(255,0,0,1.0)).drawRectangleLine(f, t)

def main():
    '''main method'''
    ProEpilogue("My Art", (500,300), "a41.html").writeHTMLfile()

main()

                                                                                                                                                                                                                                                                                                        
