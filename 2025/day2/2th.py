#Advent Of Code 2025 day 2 
#by dfrodrig-git 
#Advent Of Code 2025 day 2 
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


def getInput(test = True, day = 2) :
    if testRun or test :
        f=open(f'inputDay{day}Test.txt')
    else :
        f=open(f'inputDay{day}.txt')

    ''' 
    ## split / strip
    '''
    
    #data = [line.strip() for line in f]
    
    lines = [line.split(",") for line in f]
    
    data = [x.split("-") for x in lines[0]]
    
    data = [(int(x[0]), int(x[1])) for x in data ]
    return data

    ''' 
    ## regular expressions
    
    data = f.read()

    p=re.compile(r"mul\((\d+),(\d+)\)")
    #if filterDo :
    #    data=re.sub(r"don\'t\(\)(?s).*?do\(\)","",data)

    return p.findall(data)
    ''' 
    
def checkDuplicate(number) :
    value = str(number)
    if len(value)%2 :
        return 0
    else :
        size = len(value)//2 
        return number if value[:size] == value[size:] else 0

def checkDuplicatePart2(number) :
    value = str(number) 
    repetitions = range(2,len(value)+1)
    
    for rep in repetitions :
        if len(value) % rep :
            continue

        chunkSize = len(value)//rep
        offset = 0
        items=[]
        for i in range(rep) :
            items.append(value[offset:chunkSize+offset])
            offset += chunkSize
        if len(set(items)) == 1 :
            return number
    return 0

def processDataPart1(data) :
    result = 0
    for dataRange in data :
        result += sum(map(checkDuplicate, range(dataRange[0], dataRange[1]+1)))
             
    return result
        


def processDataPart2(data) :
    result = 0
    for dataRange in data :
        result += sum(map(checkDuplicatePart2, range(dataRange[0], dataRange[1]+1)))
             
    return result


#Part1
#do stuff
data = getInput(testRun) 

result = processDataPart1(data) 

assertExpected(result, 1227775554)

#Part 2
result2 = processDataPart2(data) 

assertExpected(result2, 4174379265, part=2)

