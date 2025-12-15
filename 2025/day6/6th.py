#Advent Of Code 2025 day 6 
#by dfrodrig-git 
import re
import logging
import sys
import numpy
from functools import reduce
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


testRun = False

def assertExpected( result, expected,part=1):
    logger.info(f'Result part:{part}: {result}, expected: {expected}')
    if result != expected and testRun :
        logger.critical("Unnaceptable!")


def getInput(test = True, day = 6) :
    if testRun or test :
        f=open(f'inputDay{day}Test.txt')
    else :
        f=open(f'inputDay{day}.txt')

    '''
    #strip/split
    ''' 
    lines = [line for line in f]
    data = [x.split() for x in lines]

    return data, lines

    ''' 
    # regex
    ''' 
    data = f.read()
    p = re.compile()

    return p.findall(data)

def processDataPart1(data) :
    t = numpy.transpose(data)
    
    result = 0
    
    for line in t :
        operator = line[-1]
        if operator == '+' :
            r = sum(map(lambda x:int(x), line[:-1]))
        if operator == '*' :
            r = reduce(lambda x,y : int(x)*int(y), line[:-1])

        #print(f'Got {r}  as a result of {operator} on {line[:-1]}')
        result += r

    return result
    

def processCol(column) :
    print(f'processing column: {column} ')
    return int("".join("".join(column).split()))
    
    
    
def processRange(startIndex, endIndex, operator, lines) :
    numbers = []
    print(f'Checking for indexes: {startIndex}, {endIndex}, applying {operator}')

    for col in range(startIndex,endIndex-1) :
        numbers.append(processCol([x[col] for x in lines]))
    
    print(f'Numbers result: {numbers} ')
    
    r= sum(numbers) if operator == '+' else reduce(lambda x,y:x*y, numbers)
    
    print(f'After applying "{operator}" we get: {r}')
    return r
        
    
def processDataPart2(lines) :
    
    markers = []
    
    for i, value in enumerate(lines[-1]) :
        if value in ['+', '*'] :
            markers.append((i, value))
    
    nrows = len(lines)
    ncols = len(lines[-1])
    
    allMarkersResult = 0
    print(f'Retrieved markers: {markers} ')
    
    for marker, nextMarker in zip(markers[:-1], markers[1:]) :
        allMarkersResult += processRange(marker[0], nextMarker[0], marker[1], lines[:-1])
    
    allMarkersResult += processRange(markers[-1][0], ncols+1, markers[-1][1], lines[:-1])
    
    return allMarkersResult
        

#Part1
#do stuff
data,lines = getInput(testRun) 
print(f'{data}')

result = processDataPart1(data) 

assertExpected(result, 4277556)

#Part 2
result2 = processDataPart2(lines) 

assertExpected(result2, 3263827, part=2)

