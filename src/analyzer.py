import argparse
from collections import defaultdict
ASM_DIR = "./asm/"
OUTPUT_DIR = "./output/"
def parseInstructions(fileName, asmText):
    offset = 29
    occurences = defaultdict(int)
    instructions = []
    for line in asmText.splitlines():
        parts = line[offset:].partition(" ")
        instr = parts[0]
        if not instr:
            continue
        instructions.append(instr)
        occurences[instr] += 1
    # Output csv of occurences and return list of all instructions
    sum = 0
    f = open(OUTPUT_DIR + fileName + "_frequency.csv", "w")
    for e in sorted(occurences, key=occurences.get, reverse=True):
        val = occurences[e]
        sum += val
        f.write(e + "," + str(val) + "\n")
    f.write("sum," + str(sum) + "\n") # sum should equal the line count as a sanity check
    f.close()
    return instructions

def pattern(fileName, seq):
    occurences = defaultdict(int)
    # get all of the patterns from length 3 to len(seq)/2 + 1
    for length in range(3,int(len(seq)/2+1)):
        for i in range(0,len(seq)-length+1):
            currPattern = tuple(seq[i:i+length])
            occurences[currPattern] += 1
    # Output csv of occurences and return list of all instructions
    f = open(OUTPUT_DIR + fileName + "_patterns.csv", "w")
    for e in sorted(occurences, key=occurences.get, reverse=True):
        if occurences[e] > 3:
            f.write(str(e) + "\n" + str(occurences[e]) + "\n\n")
    f.close()
    return occurences
    
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="File name of the x86 assembly to analyze.")
args = vars(ap.parse_args())
fileName = args["file"]
f = open(fileName)
asmText = f.read()
fileName = fileName.partition(ASM_DIR)[2].split(".")[0]
print(fileName)
allInstr = parseInstructions(fileName, asmText)
patterns = pattern(fileName, allInstr)
for instr in allInstr:
    print(instr)

