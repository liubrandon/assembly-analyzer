import argparse
from collections import defaultdict

def parseInstructions(fileName, asmText):
    offset = 21
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
    f = open(fileName[:fileName.index(".")] + "_frequency.csv", "w")
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
    f = open(fileName[:fileName.index(".")] + "_patterns.csv", "w")
    for e in sorted(occurences, key=occurences.get, reverse=True):
        if occurences[e] > 3:
            f.write(str(e) + "\n" + str(occurences[e]) + "\n\n")
    f.close()
    return occurences
    
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="File name of the x86 assembly to analyze.")
args = vars(ap.parse_args())

f = open(args["file"])
asmText = f.read()
allInstr = parseInstructions(args["file"], asmText)
for instr in allInstr:
    print(instr)
patterns = pattern(args["file"], allInstr)

