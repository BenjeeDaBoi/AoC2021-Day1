# # # # # # # # # # # # # # # # # # 
# # # # Advent of Code 2021 # # # #
# # # - - - - - - - - - - - - # # #
# # # #   Code by Benjee    # # # # 
# # # # # # # # # # # # # # # # # #
# #  Solutions are individual   # #
# # # # # # # # # # # # # # # # # #


import os

def readMeasures():
    
    file = open(os.path.join(os.getcwd(), os.path.dirname(__file__), "input/puzzle_input.txt"), "r")
    depthMeasures = []
    
    for num in file:
        depthMeasures.append(int(num))
        
    file.close()
    return depthMeasures

def calcDepthMeasureIncrements(depthMeasures):
    
    depthIncreases = 0
    for i in range(1, len(depthMeasures)):
        if (depthMeasures[i] > depthMeasures[i-1]):
            depthIncreases = depthIncreases + 1
            
    return depthIncreases

def calcThreeWaysDepthMeasureIncrements(depthMeasures):
    
    depthIncreases = 0
    depthMeasures[0] = depthMeasures[0] + depthMeasures[1] + depthMeasures[2] # Get rid of 2000 double if statements here
    for i in range(1, len(depthMeasures) - 2):
        depthMeasures[i] = depthMeasures[i] + depthMeasures[i+1] + depthMeasures[i+2]
        if (depthMeasures[i] > depthMeasures[i-1]):
            depthIncreases = depthIncreases + 1

    return depthIncreases


# Execute Solution

depthMeasures = readMeasures()
print(f"The amount of Depth Measure Increases of the Test Sample is {calcDepthMeasureIncrements(depthMeasures)}")
print(f"The amount of Triple Depth Measure Increases of the Test Sample is {calcThreeWaysDepthMeasureIncrements(depthMeasures)}")