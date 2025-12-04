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

def findJoltagePart2(array, nBatteries=12) :    
    batteries=[]
    offset = 0
    while len(batteries) < nBatteries :
        #guarantee we will not run out of batteries, we will check only up to a max
        logger.info(f'b:{batteries},  offset:{offset}')
        missingBatteries = nBatteries - len(batteries)
        checkUpToIndex = -missingBatteries+1 
        checkArray = array[offset:checkUpToIndex] if checkUpToIndex < 0 else array[offset:]
        #logger.info(f'checking: {array[offset:checkUpToIndex]}, indexes:{offset},{checkUpToIndex}')
        maxNumber = max(checkArray)
        indexOfMaxNumber = checkArray.index(maxNumber)
        
        offset += indexOfMaxNumber+1
        batteries.append(maxNumber)           
    
    logger.info(f'final number: {batteries}')

    return sum([v*10**i for i,v in enumerate(reversed(batteries))])

def processDataPart1(data) :
    result = sum(map(findJoltage, data))
    
    return result

def processDataPart2(data) :
    
    result = sum(map(findJoltagePart2, data))
    
    return result


#Part1
#do stuff
data = getInput(testRun) 

result = processDataPart1(data) 

assertExpected(result, 357)

#Part 2
result2 = processDataPart2(data) 

assertExpected(result2, None, part=2)


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unit Tests
##############################################################################
def unitTests() :
    pairs = (('987654321111111',987654321111 ),
    ('811111111111119',811111111119),
    ('234234234234278',434234234278  ),
    ('818181911112111',888911112111  )
    )
    for pair in pairs:
        assertExpected(findJoltagePart2(list(map(int,list(pair[0])))),pair[1]  )

#unitTests()
