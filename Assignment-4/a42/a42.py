#!/usr/bin/env python3
'''Assignment 4 Part 2'''

from typing import IO
import random

class GenRandom:
    '''GenRandom class'''

    def __init__(self, count: int):
        self.count: int = count
        random.seed()
        self.table: list[tuple] = []
        for i in range(0, self.count):
            current: ArtConfig = ArtConfig(random.randrange(0, 3), (random.randrange(0, 701), random.randrange(0,501)), 
                      random.randrange(0, 101), (random.randrange(10, 31), random.randrange(10, 31)), 
                      (random.randrange(10, 101), random.randrange(10, 101)), 
                      (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)), 
                      random.uniform(0.0, 1.0))
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

def main():
    '''main method'''
    randomTable: GenRandom = GenRandom(10)
    print("CNT SHA   X   Y RAD  RX  RY   W   H   R   G   B  OP")
    #print(f"{randomTable.table[0][1].shapeType}")
    for i in range(len(randomTable.table)):
        print("{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3.1f}".format(randomTable.table[i][0], 
                                   randomTable.table[i][1].shapeType, randomTable.table[i][1].x, randomTable.table[i][1].y, 
                                   randomTable.table[i][1].radius, randomTable.table[i][1].RX, randomTable.table[i][1].RY, randomTable.table[i][1].width, 
                                   randomTable.table[i][1].height, randomTable.table[i][1].red, randomTable.table[i][1].green, randomTable.table[i][1].blue, 
                                   randomTable.table[i][1].opacity))

main()

                                                                                                                                                                                                                                                                                                        
