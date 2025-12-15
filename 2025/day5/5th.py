#Advent Of Code 2025 day 5 
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


def getInput(test = True, day = 5) :
    if testRun or test :
        f=open(f'inputDay{day}Test.txt')
    else :
        f=open(f'inputDay{day}.txt')

    '''
    #strip/split
    ''' 
    lines = [line.strip() for line in f]
    
    ranges = [list(map(int, x.split("-"))) for x in lines if "-" in x]
    
    ingredients = [int(x) for x in lines if "-" not in x and len(x)>0]
    
        

    return ranges, ingredients

def checkIngredientInRange(ingredient, rangeMap) :
    if ingredient in range(*rangeMap) :
        return True

def processDataPart1(ranges, ingredients) :
    
    freshIngredients = []
    
    for ingredient in ingredients :
        for rangeMap in ranges :
            freshIngredients.append(ingredient) if ingredient in range(rangeMap[0], rangeMap[1]+1) else None
    
    #print(f'freshIngredients: {freshIngredients}')

    return len(set(freshIngredients))

class Range :
    def __init__(self,start, end) :
        self.start = start
        self.end = end
        self.nextNode = None
        self.orphan = False
    
    def setNextNode(self, nextNode) :
        self.nextNode = nextNode
    
    def updateRange(self) :
        if self.nextNode is None :
            return None
        
        #handle overlap
        if self.end >= self.nextNode.start :
            if self.nextNode.end > self.end :
               self.end = self.nextNode.end
            self.nextNode.orphan = True
            self.nextNode = self.nextNode.nextNode
       
            return self
        
        return self.nextNode
                                  
def processDataPart2(ranges) :
    
    rangeNodes = []
    for rangeMap in ranges :
        newRange = Range(rangeMap[0], rangeMap[1])
        rangeNodes.append(newRange)

    rangeNodes.sort(key= lambda x: x.start)
    
    #created Linked List
    [x.setNextNode(y) for x,y in zip(rangeNodes[:-1], rangeNodes[1:])  ]
    
    #remove overlaps
    nextNode = rangeNodes[0]
    
    while nextNode.nextNode is not None :
        nextNode = nextNode.updateRange()
        
    #check new List
    newRanges = [x for x in rangeNodes if x.orphan==False]
    
    #compute result:
    #result= sum( [ x.end-x.start+1  for x in newRanges ])
    
    print(f'{[(x.start, x.end) for x in newRanges]}')
    
    return newRanges
    
#Part1
#do stuff
ranges, ingredients = getInput(testRun) 

print(f'ranges: {ranges}')
print(f'ingredients: {ingredients}')

result = processDataPart1(ranges, ingredients) 

assertExpected(result, 3)

#Part 2
result2 = processDataPart2(ranges) 

assertExpected(result2, 14, part=2)

 