#Advent Of Code 2025 day 3 
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


def getInput(test = True, day = 3) :
    if testRun or test :
        f=open(f'inputDay{day}Test.txt')
    else :
        f=open(f'inputDay{day}.txt')

    '''
    #strip/split
    ''' 
    lines = [line.strip() for line in f]
    data = [list(map(int,x)) for x in lines]

    return data


def findJoltage(array) :
    greaterFirstNumber = max(array[:-1])
    
    firstIndex = array[:-1].index(greaterFirstNumber)

    greaterSecondNumber = max(array[firstIndex+1:])

    #logger.info(f'{array}: max:{greaterFirstNumber}, indexOf:{firstIndex}, secondGreater: {array[firstIndex:]}, {greaterSecondNumber}')

    
    return greaterFirstNumber*10+greaterSecondNumber    
    


def processDataPart1(data) :
    result = sum(map(findJoltage, data))
    
    return result

def processDataPart2(data) :
    pass


#Part1
#do stuff
data = getInput(testRun) 

result = processDataPart1(data) 

assertExpected(result, 357)

#Part 2
result2 = processDataPart2(data) 

assertExpected(result2, None, part=2)

