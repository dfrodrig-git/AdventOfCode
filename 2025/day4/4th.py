#Advent Of Code 2025 day 4 
#by dfrodrig-git 
import re
import logging
import sys
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


testRun = False

def assertExpected( result, expected,part=1):
    logger.info(f'Result part:{part}: {result}, expected: {expected}')
    if result != expected and testRun :
        logger.critical("Unnaceptable!")


def getInput(test = True, day = 4) :
    if testRun or test :
        f=open(f'inputDay{day}Test.txt')
    else :
        f=open(f'inputDay{day}.txt')

    '''
    #strip/split
    ''' 
    lines = [line.strip() for line in f]
    data = [list(x) for x in lines]

    return data

  
class Node :        
        
    def __init__(self, x, y, symbol) :
        self.x = x
        self.y = y
        self.isForkliftAccessible = False
        self.neighbours = []
        self.symbol = symbol 
    
    def remove(self) :
        self.symbol='.'
        
    def isRoll(self) :
        return 1 if self.symbol == '@' else 0
    
    
    def setNeighbours(self, neighbours=[]) :
        self.neighbours = [x for x in neighbours if (x is not None and x is not self)]
        
    def setForkliftAccessible(self) :
        self.numberAdjacentRolls = sum([x.isRoll() for x in self.neighbours ])
        if self.numberAdjacentRolls < 4 :
            self.isForkliftAccessible = True

        
    def getNeighbourhoodPos(self) :
        neighbours = []
        for vectorX in (-1,0,1) :
            for vectorY in (-1,0,1) :
                neighbourPos = (self.x+vectorX, self.y+vectorY)
                neighbours.append(neighbourPos) 
        return set(neighbours)
        
    '''
    def __str__(self) :
        return f'({self.x},{self.y}) - {self.symbol} - isRoll:{self.isRoll()}'
    '''
    def __str__(self) :
        return f'{self.symbol} - isRoll:{self.isRoll()} isForkLiftAccessible:{self.isForkliftAccessible}'
    ''' 
    def __repr__(self) : 
        return f'({self.x},{self.y}) - {self.symbol} - isRoll:{self.isRoll()}'
    '''
    def __repr__(self) : 
        return f'({self.x},{self.y}) - {self.symbol} - isRoll:{self.isRoll()} isForkLiftAccessible:{self.isForkliftAccessible}'

    
def processDataPart1(data) :
    #create Nodes
    nodeMap = {}
    for y in range(0, len(data)) :
        for x in range(0, len(data[0])) :
            nodeMap[(x,y)] = Node(x,y, data[x][y])
    
    #addNeighbours (also deremines if node is forkLiftAccessible)
    for node in nodeMap.values() :
        node.setNeighbours([nodeMap.get((x,y), None) for x,y in node.getNeighbourhoodPos()])
        node.setForkliftAccessible()
    
    return nodeMap

def getResult(nodeMap) :
    return len([x for x in nodeMap.values() 
                if x.isForkliftAccessible
                and x.isRoll()])


def processDataPart2(data) :
    nodeMap = {}
    for y in range(0, len(data)) :
        for x in range(0, len(data[0])) :
            nodeMap[(x,y)] = Node(x,y, data[x][y])

    #addNeighbours
    for node in nodeMap.values() :
        node.setNeighbours([nodeMap.get((x,y), None) for x,y in node.getNeighbourhoodPos()])
        node.setForkliftAccessible()

    removed = len([x.remove()  for x in nodeMap.values() if x.isForkliftAccessible and x.isRoll()])
    
    while True :
        [x.setForkliftAccessible() for x in nodeMap.values() if x.isRoll()]
        toRemove = [x.remove() for x in nodeMap.values() if x.isForkliftAccessible and x.isRoll()]
        if len(toRemove) == 0 :
            break
        removed += len(toRemove)
    
    return removed

#Part1
#do stuff
data = getInput(testRun) 

nodeMap = processDataPart1(data) 

result = getResult(nodeMap) 

assertExpected(result, 13)
''' 


''' 
#Part 2
#nodeMap = processDataPart1(data) 
result2 = processDataPart2(data) 


assertExpected(result2, 43, part=2)


'''
# Unit test:
''' 