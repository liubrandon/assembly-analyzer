import argparse
from collections import defaultdict
def countRegisters(asmText):
    

def parseInstructions(fileName, asmText):
    offset = 32
    occurences = defaultdict(int)
    instructions = []
    for line in asmText.splitlines()[1:]:
        parts = line[offset:].partition(" ")
        instr = parts[0]
        if not instr:
            continue
        instructions.append(instr)
        occurences[instr] += 1
    # Output csv of occurences and return list of all instructions
    f = open(fileName[:fileName.index(".")] + "_frequency.csv", "a")
    for e in sorted(occurences, key=occurences.get, reverse=True):
        f.write(e + "," + str(occurences[e]) + "\n")
    f.close()
    return instructions

def pattern(seq):
    storage = {}
    for length in range(3,int(len(seq)/2+1)):
        valid_strings = {}
        for start in range(0,len(seq)-length+1):
            valid_strings[start] = tuple(seq[start:start+length])
        candidates = set(valid_strings.values())
        if len(candidates) != len(valid_strings.values()):
            print("Pattern found for " + str(length))
            storage = valid_strings
        else:
            print("No pattern found for " + str(length))
            return set(filter(lambda x: [list(storage.values())].count(x) > 1, storage.values()))
    return storage

# https://stackoverflow.com/questions/35964155/checking-if-list-is-a-sublist
def sublist(ls1, ls2):
    '''
    >>> sublist([], [1,2,3])
    True
    >>> sublist([1,2,3,4], [2,5,3])
    True
    >>> sublist([1,2,3,4], [0,3,2])
    False
    >>> sublist([1,2,3,4], [1,2,5,6,7,8,5,76,4,3])
    False
    '''
    def get_all_in(one, another):
        for element in one:
            if element in another:
                yield element

    for x1, x2 in zip(get_all_in(ls1, ls2), get_all_in(ls2, ls1)):
        if x1 != x2:
            return False

    return True

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="File name of the x86 assembly to analyze.")
args = vars(ap.parse_args())

f = open(args["file"])
asmText = f.read()
allInstr = parseInstructions(args["file"], asmText)
for instr in allInstr:
    print(instr)
patterns = pattern(allInstr)
print(patterns)