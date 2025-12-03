#Advent Of Code 2025 day 2 
#by dfrodrig-git 
#Advent Of Code 2025 day 2 
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


def getInput(test = True, day = 4) :
    if testRun or test :
        f=open(f'inputDay{day}Test.txt')
    else :
        f=open(f'inputDay{day}.txt')

    data = [line.strip() for line in f]
    return data


def processDataPart1(data) :
    pass


def processDataPart2(data) :
    pass


#Part1
#do stuff
data = getInput() 

result = processDataPart1() 

assertExpected(result, None)

#Part 2
result2 = processDataPart2() 

assertExpected(result2, None, part=2)

