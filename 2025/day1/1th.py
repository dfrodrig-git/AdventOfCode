#Advent Of Code 2025 day 1 
#by dfrodrig-git 
import re
from collections import Counter

import logging
import sys
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


testRun = False

def assertExpected( result, expected, part=1):
    logger.info(f'Result part:{part}: {result}, expected: {expected}')
    if result != expected and testRun :
        logger.critical("Unnaceptable!")


def getInput(test = True, day = 1) :
    if testRun or test :
        f=open(f'inputDay{day}Test.txt')
    else :
        f=open(f'inputDay{day}.txt')

    data = [line.strip() for line in f]
    return data

def dial(start, dial) :
    direction = dial[0]
    value = int(dial[1:])
    
    newStart = start
    flips = 0
    if direction == 'L' :
        newStart = (start - value) % 100
        flips = ((start-value) // 100)*-1
        if start == 0 :
            flips -= 1
    if direction == 'R' :
        newStart = (start + value) % 100 
        flips = ((start+value) // 100)
        if newStart == 0 :
            flips -= 1
    
    logger.info(f'Start = {start}, Dial = {dial}, newStart = {newStart}, flips = {flips}')
    return newStart, flips 

#Part 1
result = getInput(testRun)


start = 50
password = 0
for dialNumber in result :
    start,flips = dial(start, dialNumber)
    #logger.info(f'dialed: {dialNumber},  new Start: {start}, flips: {flips}' )
    if start == 0:
        password += 1
    password += flips


assertExpected(password, 3, part=1)
#answer 995

assertExpected(password, 6, part=2)


5856


#Part 2
''' 
resultTest= sum([int(x)*int(y) for x,y in getInput(test=True, filterDo=True)])
print(f'Result Part2 Test: {resultTest}, while expected is {testExpected2}')

result= sum([int(x)*int(y) for x,y in getInput(test=False, filterDo=True)])
print(f'Result: {result}')
'''