import sys        # command line arguments
import re         # regular expression tools

# take in the two arguments
textFname = sys.argv[1]
outputFname = sys.argv[2]

# stats
words  = []

#dictionary of words
dictionary = dict()

# open input file
with open(textFname, 'r') as inputFile:
    for line in inputFile:
        line = line.strip()
        #regular expression
        word = re.compile('[\W]+')
        #line to lower case 
        listOfStrings = word.split(line.lower() )
        
        for x in listOfStrings:
        	theWord = str(x)
        	words.append(theWord)

# add words to dictionary with the number of times they show up
for i in range(0, len(words) ):
    tWords = str(words[i])
    if tWords != "":
        if tWords not in dictionary:
            dictionary[tWords] = 0
        if tWords in dictionary:
            dictionary[tWords] += 1

# write the words to the output file
outputFile = open(outputFname, 'w')

for key,val in sorted(dictionary.items() ):
        outputFile.write("%s %d\n" % (key, val) )
outputFile.close()
