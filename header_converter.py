'''
******************************************
Python Converter: Raw Text --> HTTP Header w/ Python Syntax
******************************************
REQUIRES: a text file (.txt) that contains the raw header in plain text
separated by a colon (':')
--------------------------
OUTPUTS: a dictionary that maps the key (Header field) with its value
--------------------------
Devin Dwyer | 12/29/2013
'''

def convertHead(txtFile): # takes the text file and returns the dictionary
    rawHeaderLst = list() 
    headerDict = dict()
    for line in txtFile: 
        line = line.strip().split(':') # strips each line and splits it at colens
        rawHeaderLst.append(line) # appends to header list
    for element in rawHeaderLst: # additional parsing
        removeSpace = element[1] 
        element[1] = removeSpace[1:]
        if 'https' in element or 'http' in element: # check for invalid splits
            temp = element[1]
            element[1] = temp.strip(' ') + ':' + element[2]
        headerDict[element[0]] = element[1] # add to dictionary
    return headerDict

def output(header): # takes header dictionary and returns the plain text output
    print('*************************')
    print('\nHeader (as a dictionary):', '\n-------------------------')
    print('PARSED','\n......')
    for i in header:
        print(i, ':', header[i])
    print('-------------------------')
    print('SOURCE','\n......')
    print(header, '\n-------------------------')
    print('\n*************************')
    
def main():
    txtFile = open(input('Enter raw header text file: '))
    output(convertHead(txtFile))

main()
