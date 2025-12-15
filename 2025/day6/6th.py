#Advent Of Code 2025 day 6 
#by dfrodrig-git 
import re
import logging
import sys
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


testRun = True

def assertExpected( result, expected,part=1):
    logger.info(f'Result part:{part}: {result}, expected: {expected}')
    if result != expected and testRun :
        logger.critical("Unnaceptable!")


def getInput(test = True, day = None) :
    if testRun or test :
        f=open(f'inputDay{day}Test.txt')
    else :
        f=open(f'inputDay{day}.txt')

    '''
    #strip/split
    ''' 
    lines = [line.strip() for line in f]
    data = [x.split("-") for x in lines]

    return data

    ''' 
    # regex
    ''' 
    data = f.read()
    p = re.compile()

    return p.findall(data)

def processDataPart1(data) :
    pass


def processDataPart2(data) :
    pass


#Part1
#do stuff
data = getInput(testRun) 

result = processDataPart1(data) 

assertExpected(result, None)

#Part 2
result2 = processDataPart2(data) 

assertExpected(result2, None, part=2)

