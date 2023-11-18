import pickle
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys
import random
import socket
from importlib import import_module
import time
global i
i = import_module("Ivory_imports")
ivoryImports = [i]
Linenum = [0]
currentfunc = [0]
currentseq = [0]
activefunc = [0]
Version = ["1.9.6"]
lockedfunc = [0]
sequenceval = ["notactive"]
memory = []
varmem = []
functions = ["print", "save_file", "load_file", "var"]
newerFunctions = ["sequence", "sequence.use", "py", "while", "whiletrue", "list", "from_list", "for", "sequence.create", "try", "append", "break"]
inprogramfunctions = []
functionsmem = []
processmem = []
processdata = []
inprogramsequences = []
sequencesmem = []
importing = [False]
forvalue = []

def FindVar(var):
    try:
        VarNumVal = varmem.index(var)
        return memory[VarNumVal]
    except ValueError:
        
        
        if var.endswith("return_val__"):
            print("it did")
        
        print(f"ERROR: UNDEFINED VARIABLE | LINE: {Linenum[0]} | Could not find \"{var}\" ")
        if sequenceval[0] == "active":
            print(f"ERROR OCCURED IN SEQUENCE: \"{currentseq[0]}\"")
        
            
        sys.exit(1)

        
def SaveVar(varname, varvalue):
    if varname in varmem:
        varnum = varmem.index(varname)
        memory[varnum] = varvalue
    else:
        varmem.append(varname)
        memory.append(varvalue)

def MakeProcess(name, var):
  var = list(var)
  if name in processmem:
    namenum = processmem.index(name)
    processdata[namenum] = var
  else:
    processmem.append(name)
    processdata.append(var)

def LoadProcess(name):
  processval = processmem.index(name)
  thevar = processdata[processval]
  return thevar

def FindFunc(function):
    FuncNumVal = inprogramfunctions.index(function)
    return functionsmem[FuncNumVal]

def FindSeq(sequence):
    try:
        FuncNumVal = inprogramsequences.index(sequence)
        return sequencesmem[FuncNumVal]
    except ValueError:
        linenum = Linenum[0]
        print(f"ERROR IN LINE({linenum}): UNDEFINED SEQUENCE | Could not find \"{sequence}\" ")
        sys.exit(1)
        
def Ithread():
    seq = FindVar("called_seq__")
    Sequence(f"sequence.use {seq}")



# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS
# IVORY FUNCTIONS


def py_import(module):
    check = open("Ivory_imports.py", "r").readlines()
    if f"import {module}\n" in check or f"import {module}" in check:
        pass
    else:
        
        file = open("Ivory_imports.py", "a+")
        file.write(f"import {module}\n")
        file.close()
        time.sleep(1)
        ivoryImports[0] = import_module("Ivory_imports")

def Ibreak():
    forvalue.append("notactive")




def Length(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    if SplitLine[0] == "\"":
        SplitLine.pop(0)
        SplitLine.pop(len(SplitLine) - 1)
        length = len(" ".join(SplitLine))
    else:
        length = len(FindVar(SplitLine[0]))
    return length

def List(Line):
    SplitLine = Line.split(sep=None)
    newlist = []
    SplitLine.pop(0)
    listval = SplitLine.count("]")
    for d in range(0, listval):
        MakeProcess("currentvar", SplitLine)
        currentvar = LoadProcess("currentvar")
        currentvar.pop(0)


        if currentvar[0] == "\"":
            currentvar.pop(0)


            endquote = currentvar.index("\"")
            currentvar.pop(endquote)
            endofvar = currentvar.index("]")

            for b in range(endofvar, len(currentvar)):

                currentvar.pop(endofvar)

            SplitLine.pop(0)
            SplitLine.pop(0)
            for d in range(0, len(currentvar)):
                SplitLine.pop(0)
            SplitLine.pop(0)
            SplitLine.pop(0)
            newlist.append(" ".join(currentvar))

        elif currentvar[0] == "]":
            pass

        else:
            SplitLine.pop(0)

            newlistval = FindVar(SplitLine[0])
            newlist.append(newlistval)
            SplitLine.pop(0)
            SplitLine.pop(0)
            # [ var ]
    return newlist


# table { " val1 " " val 2 " }
def table(Line):
    SplitLine = Line.split(sep=None)
    global result
    result = []
    SplitLine.pop(0)
    SplitLine.pop(0)
    startnum = len(SplitLine)
    if SplitLine[0] == "}":
      pass
    else:
        while startnum > 0:
            if SplitLine[0] == "\"":
                SplitLine.pop(0)
                endofstring = SplitLine.index("\"")
                templine = list(SplitLine)
                for x in range(endofstring, len(SplitLine)):
                    templine.pop(endofstring)
                for x in templine:
                    SplitLine.pop(0)
                    startnum -= 1
                SplitLine.pop(0)
                startnum -= 1
                result.append(" ".join(templine))
            elif SplitLine[0] in varmem:
                found = FindVar(SplitLine[0])
                SplitLine.pop(0)
                startnum -= 1
                result.append(found)
            elif SplitLine[0] == "}":
                break
            else:
                print(f"ERROR IN LINE {Linenum[0]}: TABLE ERROR | Invalid value in table")
                if sequenceval[0] == "active":
                    if currentseq[0] != 0:
                        print(f"ERROR OCCURED IN SEQUENCE: \"{currentseq[0]}\"")
                sys.exit(1)
            
        
    return result
    


        


    #for x in SplitLine:
    #    if x == "\"":
    #        SplitLine.pop(0)
    #        endofstring = SplitLine.index("\"")
    #        templine = list(SplitLine)
    #        for f in range(endofstring, len(templine)):
    #            templine.pop(endofstring)
    #        print(templine)
    #        for x in templine:
    #            SplitLine.pop(0)
    #        SplitLine.pop(0)
    #    print(SplitLine)



# from_list " list " 1
def FromList(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    if SplitLine[0] == "\"":
        MakeProcess("thisquote", SplitLine)
        thisquote = LoadProcess("thisquote")
        thisquote.pop(0)
        endofquote = thisquote.index("\"")
        for t in range(endofquote, len(thisquote)):
            thisquote.pop(endofquote)
            thelist = " ".join(thisquote)
        SplitLine.pop(0)
        for t in range(0, len(thisquote)):
            SplitLine.pop(0)
        SplitLine.pop(0)
    else:
        thelist = FindVar(SplitLine[0])
        SplitLine.pop(0)
    if SplitLine[0] == "(":
        SplitLine.pop(0)
        thenum = FindVar(SplitLine[0])
    else:
        thenum = SplitLine[0]
    foundlist = FindVar(thelist)
    return foundlist[int(thenum)]
# range 1 - 5

# makes a list of numbers between a range of two numbers



# list = ...
# for i in list {{ sequence.use loop }}

# for loop
def ForLoop(Line):
    forvalue.append("active")
    SplitLine = Line.split(sep=None)
    LineValues = Line.split(sep=None)
    SplitLine.pop(0)
    SaveVar(LineValues[1], "None")
    SplitLine.pop(0)
    SplitLine.pop(0)
    
    newlist = FindVar(SplitLine[0])
    SplitLine.pop(0)
    SplitLine.pop(0)
    SplitLine.pop(len(SplitLine) - 1)


    for item in newlist:
        SaveVar(LineValues[1], item)
        if SplitLine[0] in functions:
            IvoryFunctions(" ".join(SplitLine), SplitLine[0])
        elif SplitLine[0] in newerFunctions:
            NewFunctions(" ".join(SplitLine), SplitLine[0])
        elif SplitLine[0] in inprogramfunctions:
            Ifunction(" ".join(SplitLine))
        if forvalue[len(forvalue) - 1] == "notactive":
            break
        

def save_file(Line):
    LineValues = Line.split(sep=None)
    if LineValues[1] == "append":
        pass
    if LineValues[1] == "\"":
        MakeProcess("SplitLine", LineValues)
        SplitLine = LoadProcess("SplitLine")
        SplitLine.pop(0)
        SplitLine.pop(0)
        MakeProcess("LineForSave", SplitLine)
        LineForSave = LoadProcess("LineForSave")
        for value in LineForSave:
            if value == "\"":
                maxval = LineForSave.index(value)
            else:
                pass
        for x in range(maxval, len(LineForSave)):
            LineForSave.pop(maxval)

        SaveValue = " ".join(LineForSave)
        for FinalValues in LineForSave:
            SplitLine.pop(0)

        endofline = len(SplitLine) - 1
        SplitLine.pop(endofline)
        SplitLine.pop(0)
        SplitLine.pop(0)
        SaveFile = " ".join(SplitLine)
        pickle.dump(SaveValue, open(SaveFile, "wb"))
    else:
        VarVal = FindVar(LineValues[1])
        SplitLine = LineValues
        for x in range(0, 3):
            SplitLine.pop(0)
        endofline = len(SplitLine)
        SplitLine.pop(endofline - 1)
        SaveFile = " ".join(SplitLine)
        pickle.dump(VarVal, open(SaveFile, "wb"))

def load_file(Line):
    LineValues = Line.split(sep=None)
    SplitLine = Line.split(sep=None)
    varmem.append(LineValues[0])
    SplitLine.pop(0)
    SplitLine.pop(0)
    if SplitLine[1] == "\"":
        SplitLine.pop(0)
        SplitLine.pop(0)

        endofline = len(SplitLine) - 1
        SplitLine.pop(endofline)
        file = " ".join(SplitLine)
        loadedfile = pickle.load(open(file, "rb"))
        memory.append(loadedfile)
    else:
        SplitLine.pop(0)
        thevar = FindVar(SplitLine[0])
        loadedfile = pickle.load(open(thevar, "rb"))
        memory.append(loadedfile)

def IimportAll(module):
    try:
        ImportContent = open(f"{module}.iv", "r").readlines()
    except FileNotFoundError:
        try:
            ImportContent = open(f"modules/{module}.iv", "r").readlines()
        except FileNotFoundError:
            print(f"ERROR IN LINE({Linenum[0]}): IMPORT ERROR | Could not find module \"{module}\"")
            sys.exit(1)
    importing[0] = True
    execute(ImportContent)
    importing[0] = False


# imports a function from a module
def Iimportfrom(Line):
    LineValues = Line.split(sep=None)
    ImportContent = open(f"{LineValues[1]}.iv", "r").readlines()
    for ImportedLine in ImportContent:
        SplitLine = ImportedLine.split(sep=None)
        if SplitLine[1] == LineValues[3]:
            inprogramfunctions.append(SplitLine[1])
            functionsmem.append(ImportedLine)
        else:
            pass

# imports all functions from a specific module
def Iimport(Line):
    LineValues = Line.split(sep=None)
    try:
        ImportContent = open(f"{LineValues[1]}.iv", "r").readlines()
    except FileNotFoundError:
        try:
            ImportContent = open(f"modules/{LineValues[1]}.iv", "r").readlines()
        except FileNotFoundError:
            linenum = Content.index(Line) + 1
            print(f"ERROR IN LINE({linenum}): IMPORT ERROR | Could not find module \"{LineValues[1]}\"")
            sys.exit(1)
    required = []
    for ImportedLine in ImportContent:
        SplitLine = ImportedLine.split(sep=None)

        if SplitLine == []:
            pass
        elif SplitLine[0] == "function":
            inprogramfunctions.append(SplitLine[1])
            functionsmem.append(ImportedLine)
            if "sequence.use" in SplitLine:
                using_sequence = SplitLine.index("sequence.use")
                required.append(SplitLine[using_sequence + 1])
        elif SplitLine[0] == "import":
            Iimport(f"import {SplitLine[1]}")
        else:
            pass
    for NewLine in ImportContent:
        if NewLine.startswith("sequence"):
            if NewLine.startswith("sequence.use"):
                pass
            else:
                SeqValues = NewLine.split(sep=None)
                SplitLine = NewLine.split(sep=None)
                if SplitLine[1] in required:
                    inprogramsequences.append(SeqValues[1])
                    
                    if SeqValues[2] != "{":
                        sequencesmem.append(NewLine)
                    if SeqValues[2] == "{":
                        seqLine = ImportContent.index(NewLine)
                        MakeProcess("filecopy", ImportContent)
                        filecopy = LoadProcess("filecopy")
                        for x in range(0, seqLine):

                            filecopy.pop(0)
                        try:
                            endofseq = filecopy.index("}\n")

                            for x in range(1, len(filecopy)):
                                nextseq = len(filecopy) + 20
                                if filecopy[x].startswith("sequence.use"):
                                    pass
                                elif filecopy[x].startswith("sequence"):
                                    nextseq = x
                                    break

                            if nextseq < endofseq:

                                print("SYNTAX ERROR: Make sure the end of your sequence does not have spaces")
                                print("example: \"}    \"")
                                sys.exit(1)
                        except ValueError:

                            try:
                                endofseq = filecopy.index("}")

                                for x in range(1, len(filecopy)):
                                    nextseq = len(filecopy) + 20
                                    if filecopy[x].startswith("sequence.use"):
                                        pass
                                    elif filecopy[x].startswith("sequence"):
                                        nextseq = x
                                        break
                                if nextseq < endofseq:
                                    print("SYNTAX ERROR: Make sure the end of your sequence does not have spaces")
                                    print("example: \"}    \"")
                                    sys.exit(1)
                            except ValueError:
                                print("SYNTAX ERROR: Make sure the end of your sequence does not have spaces")
                                print("example: \"}    \"")
                                sys.exit(1)
                        for d in range(ImportContent.index(NewLine) + 1, ImportContent.index(filecopy[endofseq - 1]) + 1):
                            ImportContent.pop(ImportContent.index(NewLine) + 1)
                        for fd in range(endofseq, len(filecopy)):
                            filecopy.pop(endofseq)
                        filecopylist = []
                        for value in filecopy:
                            if value == "}":
                                new = value
                            else:
                                new = value.split(sep=None)
                            new = " ".join(new)
                            filecopylist.append(new)
                            filecopylist.append(";")
                        filecopylist = " ".join(filecopylist)
                        filecopylist = filecopylist.split(sep=None)
                        filecopylist.pop(2)
                        filecopylist.pop(2)
                        sequencesmem.append(" ".join(filecopylist))
        
        



def Sequence(Line):
    sequenceval[0] = "active"
    LineValues = Line.split(sep=None)
    newline = FindSeq(LineValues[1])
    
    SplitLine = newline.split(sep=None)
    SplitLine.pop(0)
    SplitLine.pop(0)
    endofline1 = SplitLine.index(";")
    linevalues = SplitLine.count(";")
    currentseq[0] = LineValues[1]
    for x in range(0, linevalues):
        currentseq[0] = LineValues[1]
        endofcurrentline = SplitLine.index(";")
        MakeProcess("currentline", SplitLine)
        currentline = LoadProcess("currentline")

        for value in range(endofcurrentline, len(SplitLine)):
            currentline.pop(endofcurrentline)
        evaluate(" ".join(currentline))
        if currentline == []:
            pass
        elif currentline[0] == "var":
            variable(" ".join(currentline))
        elif currentline[0] == "if":
            Iif(" ".join(currentline))
        elif currentline[0] == "return":
            currentline.pop(0)
            print(currentline)
            print(activefunc[0])
            if currentline[0] == "\"":
                currentline.pop(0)
                currentline.pop(len(currentline) - 1)
                SaveVar(f"{activefunc[0]}_return_val__", " ".join(currentline))
            else:
                print(f"return would be: {FindVar(currentline[0])}")
                SaveVar(f"{activefunc[0]}_return_val__", FindVar(currentline[0]))
        for value in currentline:
            SplitLine.pop(0)
        SplitLine.pop(0)

def evaluate(Line):
    SplitLine = Line.split(sep=None)
    try:
        if SplitLine == []:
            pass
        elif SplitLine[0] in functions:
            IvoryFunctions(" ".join(SplitLine), SplitLine[0])
        elif SplitLine[0] in newerFunctions:
            NewFunctions(" ".join(SplitLine), SplitLine[0])
        elif SplitLine[0] in inprogramfunctions:
            Ifunction(" ".join(SplitLine))
        elif SplitLine[0] == "else":
            Ielse(" ".join(SplitLine))
        elif SplitLine[0] == "var:":
          pass
    except Exception as E:
        print(f"ERROR CODE: {E} | LINE: {Line}")
        if sequenceval[0] == "active":
            if currentseq[0] != 0:
                print(f"ERROR OCCURED IN SEQUENCE: \"{currentseq[0]}\"")
        print(f"Line number: {Linenum[0]}")
        sys.exit(1)
    
        
            

# this is honestly really weird and I forgot I did this, move on 
def CreateSequence(Line):
    LineValues = Line.split(sep=None)
    newline = Line
    SplitLine = newline.split(sep=None)
    SplitLine.pop(0)
    endofline1 = SplitLine.index(";")
    linevalues = SplitLine.count(";")
    for x in range(0, linevalues):
        endofcurrentline = SplitLine.index(";")
        MakeProcess("currentline", SplitLine)
        currentline = LoadProcess("currentline")

        for value in range(endofcurrentline, len(SplitLine)):
            currentline.pop(endofcurrentline)

        evaluate(" ".join(currentline))
        if currentline[0] == "var":
            variable(" ".join(currentline))
        if currentline[0] == "if":
            Iif(" ".join(currentline))
        for value in currentline:
            SplitLine.pop(0)
        SplitLine.pop(0)



def Ifunction(Line):
    LineValues = Line.split(sep=None)
    NewLine = FindFunc(LineValues[0])
    currentfunc[0] = LineValues[0]
    PureList = NewLine.split(sep=None)
    SplitLine = NewLine.split(sep=None)
    SplitLine.pop(0)
    SplitLine.pop(0)
    SplitLine.pop(0)

    if SplitLine[0] == "...":
        listofvars = []
        
        
        templine = list(LineValues)
        templine.pop(0)


        while len(templine) > -1:

            try:
                if templine[0] == "\"":
                    templine.pop(0)
                    endofquote = templine.index("\"")
                    appendLine = list(templine)
                    #aL is for "appendLine" but I was lazy so instead I'm doing more work and typing this
                    aL = len(appendLine)
                    for x in range(endofquote, aL):
                        appendLine.pop(endofquote)
                    listofvars.append(" ".join(appendLine))
                    for value in appendLine:
                        templine.pop(0)
                    templine.pop(0)
                else:
                    thevalue = FindVar(templine[0])
                    templine.pop(0)
                    listofvars.append(thevalue)

            except IndexError:
                break
        SaveVar("...", listofvars)
        SplitLine.pop(0)

    else:
        endofvars = SplitLine.index("]")
        MakeProcess("varline", SplitLine)
        varline = LoadProcess("varline")

        for z in range(endofvars, len(varline)):
            varline.pop(endofvars)
        LineValues.pop(0)
        for var in varline:
            try:
                if LineValues[0] == "\"":
                    LineValues.pop(0)
                    MakeProcess("currentvar", LineValues)
                    currentvar = LoadProcess("currentvar")
                    try:
                        endofcurrentvar = currentvar.index("\"")
                    except ValueError:   
                        ELine = Linenum[0]
                        print(f"ERROR Line: {Line} | SYNTAX ERROR | Missing required statements in statement")
                        if sequenceval[0] == "active":
                            if currentseq[0] != 0:
                                print(f"ERROR OCCURED IN SEQUENCE: \"{currentseq[0]}\"")
                        sys.exit(1)     
                    for v in range(endofcurrentvar, len(currentvar)):
                        currentvar.pop(endofcurrentvar)
                    indexval = -1
                    for x in currentvar:
                        indexval += 1
                        if x == '\\"':
                            currentvar[indexval] = "\""
                    SaveVar(var, " ".join(currentvar))
                    for value in currentvar:
                        LineValues.pop(0)
                    LineValues.pop(0)
                else:
                    SaveVar(var, FindVar(LineValues[0]))
                    LineValues.pop(0)
            except IndexError:
                for L in Content:
                    if Line in L:
                        linenum = Content.index(L) + 1
                print(f"ERROR IN LINE({linenum}): SYNTAX ERROR | Missing required values in the \"{Line.split(sep=None)[0]}\" function")
                if sequenceval[0] == "active":
                    if currentseq[0] != 0:
                        print(f"ERROR OCCURED IN SEQUENCE: \"{currentseq[0]}\"")
                sys.exit(1)

            SplitLine.pop(0)
    SplitLine.pop(0)
    linevalues = SplitLine.count(";")
    for x in range(0, linevalues):
        endofcurrentline = SplitLine.index(";")
        MakeProcess("currentline", SplitLine)
        currentline = LoadProcess("currentline")
        
        for value in range(endofcurrentline, len(SplitLine)):
            currentline.pop(endofcurrentline) 
        
        if currentline[0] == "sequence.use":
            activefunc[0] = PureList[1]
        try:
            evaluate(" ".join(currentline))
        except Exception as E:
            print(f"PYTHON ERROR: {E}")
            print(f"ERROR LINE: {Line}")
            print(f"Line Number: {Linenum[0]}")
            if sequenceval[0] == "active":
                if currentseq[0] != 0:
                    print(f"ERROR OCCURED IN SEQUENCE: \"{currentseq[0]}\"")
            sys.exit(1)
        if currentline[0] == "var":
            variable(" ".join(currentline))
        if currentline[0] == "if":
            Iif(" ".join(currentline))
        
        
        for value in currentline:
            SplitLine.pop(0)
        # return name
        if currentline[0] == "return":
            currentline.pop(0)
            if currentline[0] == "\"":
                currentline.pop(0)
                currentline.pop(len(currentline) - 1)
                SaveVar(f"{PureList[1]}_return_val__", " ".join(currentline))
            else:
                SaveVar(f"{PureList[1]}_return_val__", FindVar(currentline[0]))

        SplitLine.pop(0)

# a while true loop, I would suggest you do not ever use this
def Iwhiletrue(Line):
    WhileSplit = Line.split(sep=None)
    WhileSplit.pop(0)
    while True:
        Sequence(" ".join(WhileSplit))


# this is a while loop, needs some work though
def Iwhile(Line):

# WHILE EQUAL TO
# WHILE EQUAL TO
# WHILE EQUAL TO

# LineValues is for the unedited split version of the line
    LineValues = Line.split(sep=None)
    if "==" in LineValues:

        SplitLine = Line.split(sep=None)
        var1 = FindVar(LineValues[1])
        SplitLine.pop(0)
        SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            endofval = SplitLine.index("\"")
            endofline = len(SplitLine)
            for x in range(endofval, endofline):
                SplitLine.pop(endofval)

            var2 = " ".join(SplitLine)
        else:
            var2 = FindVar(LineValues[3])
        useableLine = Line.split(sep=None)
        LineStartVal = useableLine.index("{{")
        for z in range(0, LineStartVal):
            useableLine.pop(0)
        useableLine.pop(0)
        useableLine.pop(len(useableLine) - 1)
        while var2 == FindVar(LineValues[1]):

            evaluate(" ".join(useableLine))

# WHILE GREATER THAN
# WHILE GREATER THAN
# WHILE GREATER THAN

    if ">" in LineValues:
        SplitLine = Line.split(sep=None)
        var1 = FindVar(LineValues[1])

        SplitLine.pop(0)
        SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            endofval = SplitLine.index("\"")
            endofline = len(SplitLine)
            for x in range(endofval, endofline):
                SplitLine.pop(endofval)
            var2 = " ".join(SplitLine)

        else:
            var2 = FindVar(LineValues[3])
        useableLine = Line.split(sep=None)
        LineStartVal = useableLine.index("sequence.use")
        for z in range(0, LineStartVal):
            useableLine.pop(0)
        while var1 > var2:
            Sequence(" ".join(useableLine))
            var1 = float(FindVar(LineValues[1]))
            var2 = float(FindVar(LineValues[3]))

# WHILE LESS THAN
# WHILE LESS THAN
# WHILE LESS THAN

    if "<" in LineValues:
        SplitLine = Line.split(sep=None)
        var1 = float(FindVar(LineValues[1]))

        SplitLine.pop(0)
        SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            endofval = SplitLine.index("\"")
            endofline = len(SplitLine)
            for x in range(endofval, endofline):
                SplitLine.pop(endofval)
            var2 = float(" ".join(SplitLine))
            MakeProcess("typevar2", "string")
        else:
            var2 = float(FindVar(LineValues[3]))
            MakeProcess("typevar2", "var")
            
        useableLine = Line.split(sep=None)
        LineStartVal = useableLine.index("sequence.use")
        for z in range(0, LineStartVal):
            useableLine.pop(0)

        
        while var1 < var2:
            typevar2 = LoadProcess("typevar2")
            Sequence(" ".join(useableLine))
            var1 = float(FindVar(LineValues[1]))
            if typevar2 == "var":
                var2 = float(FindVar(LineValues[3]))
    

# allows you to add variables to the middle of a string
def vString(string):
    SplitString = string.split(sep=None)
    SplitString.pop(0)
    SplitString.pop(len(SplitString) - 1)
    varValues = SplitString.count("%{")
    for value in range(0, varValues):
        varbeg = SplitString.index("%{")
        SplitString.pop(varbeg)
        varend = SplitString.index("}")
        thevar = varend - 1
        SplitString[thevar] = str(FindVar(SplitString[thevar]))
        SplitString.pop(varend)
    indexval = -1
    for x in SplitString:
        indexval += 1
        if x == '\\"':
            SplitString[indexval] = "\""
    newstring = " ".join(SplitString)
    return newstring


# sub ( health ) - ( damage )
# sub health -= ( damage )





# does not work
def Itry(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    endofcurrentline = SplitLine.index(";")
    MakeProcess("thisline", SplitLine)
    thisline = LoadProcess("thisline")
    for v in range(endofcurrentline, len(thisline)):
        thisline.pop(endofcurrentline)
    for value in thisline:
        SplitLine.pop(0)
    SplitLine.pop(0)
    SplitLine.pop(0)
    exception = SplitLine[0]

    try:
        evaluate(" ".join(thisline))
    except Exception as e:
        print("test")
        SplitLine.pop(0)
        evaluate(" ".join(SplitLine))









def Iif(Line):
    LineValues = Line.split(sep=None)
    SplitLine = Line.split(sep=None)
    if "==" in LineValues:
        SplitLine.pop(0)
        SplitLine.pop(0)
        SplitLine.pop(0)

        if SplitLine[0] == "\"":
            NewLine = Line.split(sep=None)
            NewLine.pop(0)
            NewLine.pop(0)
            NewLine.pop(0)
            NewLine.pop(0)
            SplitLine.pop(0)
            endofline = NewLine.index("\"")
            for v in range(endofline, len(NewLine)):
                NewLine.pop(endofline)
            for t in range(0, len(NewLine)):
                SplitLine.pop(0)
            SplitLine.pop(0)
            SplitLine.pop(0)
            indexval = -1
            for x in NewLine:
                indexval += 1
                if x == '\\"':
                    NewLine[indexval] = "\""
            checkedvar = " ".join(NewLine)

            if str(FindVar(LineValues[1])) == str(checkedvar):

                MakeProcess("newestline", SplitLine)
                newestline = LoadProcess("newestline")
                try:
                    endofif = newestline.index("}}")
                except ValueError:
                    for L in Content:
                        if Line in Content:
                            linenum = Content.index(L) + 1
                    print(f"ERROR IN LINE({linenum}): UNFINISHED STATEMENT | If statement missing", "\"{{}}\"", "brackets")
                    sys.exit(1)
                for x in range(endofif, len(newestline)):
                    newestline.pop(endofif)

                evaluate(" ".join(newestline))
                if newestline[0] == "return":
                    currentline = newestline
                    for L in Content:
                        if L.startswith("function"):
                            if Line in L:
                                PureList = L.split(sep=None)
                    
                    currentline.pop(0)
                    if currentline[0] == "\"":
                        currentline.pop(0)
                        currentline.pop(len(currentline) - 1)
                        SaveVar(f"{PureList[1]}_return_val__", " ".join(currentline))
                    else:
                        SaveVar(f"{PureList[1]}_return_val__", FindVar(currentline[0]))
                MakeProcess("ifval", "true")
                return True
                
            else: 
                MakeProcess("ifval", "false")
                return False
            
# COMPARES VARS
        else:
            checkedvar = FindVar(SplitLine[0])
            if str(FindVar(LineValues[1])) == str(checkedvar):
                SplitLine.pop(0)
                SplitLine.pop(0)
                SplitLine.pop(len(SplitLine) - 1)
                evaluate(" ".join(SplitLine))
                if SplitLine[0] == "return":
                    currentline = newestline
                    for L in Content:
                        if L.startswith("function"):
                            if Line in L:
                                PureList = L.split(sep=None)
                    
                    currentline.pop(0)
                    if currentline[0] == "\"":
                        currentline.pop(0)
                        currentline.pop(len(currentline) - 1)
                        SaveVar(f"{PureList[1]}_return_val__", " ".join(currentline))
                    else:
                        SaveVar(f"{PureList[1]}_return_val__", FindVar(currentline[0]))

# if " 12 " > var {{ print " test " }}
    elif "!=" in LineValues:
        SplitLine.pop(0)
        SplitLine.pop(0)
        SplitLine.pop(0)

        if SplitLine[0] == "\"":
            NewLine = Line.split(sep=None)
            NewLine.pop(0)
            NewLine.pop(0)
            NewLine.pop(0)
            NewLine.pop(0)
            SplitLine.pop(0)
            endofline = NewLine.index("\"")
            for v in range(endofline, len(NewLine)):
                NewLine.pop(endofline)
            for t in range(0, len(NewLine)):
                SplitLine.pop(0)
            SplitLine.pop(0)
            SplitLine.pop(0)
            checkedvar = " ".join(NewLine)

            if str(FindVar(LineValues[1])) != str(checkedvar):

                MakeProcess("newestline", SplitLine)
                newestline = LoadProcess("newestline")
                try:
                    endofif = newestline.index("}}")
                except ValueError:
                    for L in Content:
                        if Line in Content:
                            linenum = Content.index(L) + 1
                    print(f"ERROR IN LINE({linenum}): UNFINISHED STATEMENT | If statement missing", "\"{{}}\"", "brackets")
                    if sequenceval[0] == "active":
                        if currentseq[0] != 0:
                            print(f"ERROR OCCURED IN SEQUENCE: \"{currentseq[0]}\"")
                    sys.exit(1)
                for x in range(endofif, len(newestline)):
                    newestline.pop(endofif)

                evaluate(" ".join(newestline))
                if newestline[0] == "return":
                    currentline = newestline
                    for L in Content:
                        if L.startswith("function"):
                            if Line in L:
                                PureList = L.split(sep=None)
                    
                    currentline.pop(0)
                    if currentline[0] == "\"":
                        currentline.pop(0)
                        currentline.pop(len(currentline) - 1)
                        SaveVar(f"{PureList[1]}_return_val__", " ".join(currentline))
                    else:
                        SaveVar(f"{PureList[1]}_return_val__", FindVar(currentline[0]))
                MakeProcess("ifval", "true")
                return True
            else: 
                MakeProcess("ifval", "false")
                return True
            
# COMPARES VARS
        else:
            checkedvar = FindVar(SplitLine[0])
            if str(FindVar(LineValues[1])) != str(checkedvar):
                SplitLine.pop(0)
                SplitLine.pop(0)
                SplitLine.pop(len(SplitLine) - 1)
                evaluate(" ".join(SplitLine))
                if SplitLine[0] == "return":
                    currentline = newestline
                    for L in Content:
                        if L.startswith("function"):
                            if Line in L:
                                PureList = L.split(sep=None)
                    
                    currentline.pop(0)
                    if currentline[0] == "\"":
                        currentline.pop(0)
                        currentline.pop(len(currentline) - 1)
                        SaveVar(f"{PureList[1]}_return_val__", " ".join(currentline))
                    else:
                        SaveVar(f"{PureList[1]}_return_val__", FindVar(currentline[0]))
    elif ">" in LineValues:
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num1 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num1 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num2 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num2 = FindVar(SplitLine[0])
            SplitLine.pop(0)

        if float(num1) > float(num2):
            #print(SplitLine)
            SplitLine.pop(0)
            SplitLine.pop(len(SplitLine) - 1)
            evaluate(" ".join(SplitLine))
            
            MakeProcess("ifval", "true")
            return True
        else:
            MakeProcess("ifval", "false")
            return True
    elif "<" in LineValues:
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num1 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num1 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num2 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num2 = FindVar(SplitLine[0])
            SplitLine.pop(0)

        if float(num1) < float(num2):
            SplitLine.pop(0)
            SplitLine.pop(len(SplitLine) - 1)
            evaluate(" ".join(SplitLine))
            MakeProcess("ifval", "true")
            return True
        else:
            MakeProcess("ifval", "false")
            return True
# if greater than or equal to ...
    elif ">=" in LineValues:
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num1 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num1 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num2 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num2 = FindVar(SplitLine[0])
            SplitLine.pop(0)

        if float(num1) >= float(num2):
            SplitLine.pop(0)
            SplitLine.pop(len(SplitLine) - 1)
            evaluate(" ".join(SplitLine))
            
            MakeProcess("ifval", "true")
            return True
        else:
            MakeProcess("ifval", "false")
            return True
# if less than or equal to ... 
    elif "<=" in LineValues:
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num1 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num1 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num2 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num2 = FindVar(SplitLine[0])
            SplitLine.pop(0)

        if float(num1) <= float(num2):
            SplitLine.pop(0)
            SplitLine.pop(len(SplitLine) - 1)
            evaluate(" ".join(SplitLine))
            
            MakeProcess("ifval", "true")
            return True
        else:
            MakeProcess("ifval", "false")
            return True
# if var includes " test " {{ CODE }}
    elif "includes" in LineValues:
        SplitLine.pop(0)
        firstval = FindVar(SplitLine[0])
        SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            MakeProcess("currentvar", SplitLine)
            currentvar = LoadProcess("currentvar")
            endvar = currentvar.index("\"")
            for c in range(endvar, len(currentvar)):
                currentvar.pop(endvar)
            var = " ".join(currentvar)
            for value in currentvar:
                SplitLine.pop(0)
            SplitLine.pop(0)

        else:
            var = FindVar(SplitLine[0])
            SplitLine.pop(0)
        if var in firstval:
            SplitLine.pop(0)
            SplitLine.pop(len(SplitLine) - 1)
            evaluate(" ".join(SplitLine))
            
            MakeProcess("ifval", "true")
            return True
        else:
            MakeProcess("ifval", "false")
        
# I don't think this is even used anymore 
def checkif(Line):
    LineValues = Line.split(sep=None)
    SplitLine = Line.split(sep=None)
    if "==" in LineValues:
        SplitLine.pop(0)
        SplitLine.pop(0)
        SplitLine.pop(0)

        if SplitLine[0] == "\"":
            NewLine = Line.split(sep=None)
            NewLine.pop(0)
            NewLine.pop(0)
            NewLine.pop(0)
            NewLine.pop(0)
            SplitLine.pop(0)
            endofline = NewLine.index("\"")
            for v in range(endofline, len(NewLine)):
                NewLine.pop(endofline)
            for t in range(0, len(NewLine)):
                SplitLine.pop(0)
            SplitLine.pop(0)
            SplitLine.pop(0)
            checkedvar = " ".join(NewLine)

            if str(FindVar(LineValues[1])) == str(checkedvar):
                MakeProcess("ifval", "true"); return True
            else: 
                MakeProcess("ifval", "false")
                return True
        else:
            checkedvar = FindVar(SplitLine[0])
            if str(FindVar(LineValues[1])) == str(checkedvar):
                MakeProcess("ifval", "true"); return True
            else:
                MakeProcess("ifval", "false")
                return True
            

# if " 12 " > var {{ print " test " }}
    elif ">" in LineValues:
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num1 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num1 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num2 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num2 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        if float(num1) > float(num2):
            MakeProcess("ifval", "true"); return True
        else:
            MakeProcess("ifval", "false")
            return True
    elif "<" in LineValues:
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num1 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num1 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            num2 = SplitLine[0]
            SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            num2 = FindVar(SplitLine[0])
            SplitLine.pop(0)

        if float(num1) < float(num2):
            MakeProcess("ifval", "true"); return True
        else:
            MakeProcess("ifval", "false")
            return True
# if var includes " test " {{ CODE }}
    elif "includes" in LineValues:
        SplitLine.pop(0)
        firstval = FindVar(SplitLine[0])
        SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            MakeProcess("currentvar", SplitLine)
            currentvar = LoadProcess("currentvar")
            endvar = currentvar.index("\"")
            for c in range(endvar, len(currentvar) - 1):
                currentvar.pop(endvar)
            var = " ".join(currentvar)
            for value in currentvar:
                SplitLine.pop(0)
            SplitLine.pop(0)
        else:
            var = FindVar(SplitLine[0])
            SplitLine.pop(0)
        if var in firstval:
            MakeProcess("ifval", "true"); return True


# if thevar == " hello " {{ CODE }}
# else {{ CODE }}

# sequence example var thevar = " hello " ; if thevar == " hello " {{ CODE }} ; else {{ CODE }}

# else {{ ... }}
# else statement
def Ielse(Line):
    check = "".join(LoadProcess("ifval"))
    
    if check == "false":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        if SplitLine[0] == "{{":
            SplitLine.pop(0)
            SplitLine.pop(len(SplitLine) - 1)
            newline = " ".join(SplitLine)
            evaluate(newline)
        else:
            print("SYNTAX ERROR: \"{{\" not included in else statement")
            sys.exit(1)

# this allows you to use a python function inside of ivory
def Ipy(Line):
    eval(Line)

# print
def Iprint(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    try:
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            SplitLine.pop(len(SplitLine) - 1)
            indexval = -1
            for x in SplitLine:
                indexval += 1
                if x == '\\"':
                    SplitLine[indexval] = "\""

            NewLine = " ".join(SplitLine)
            print(NewLine)
        elif SplitLine[0] == "v\"":
            print(vString(" ".join(SplitLine)))
        else:
            foundvar = FindVar(SplitLine[0])
            print(foundvar)
    except IndexError:
        
        print(f"ERROR IN LINE({Linenum[0]}): UNFINISHED FUNCTION | Missing insructions after print statement")
        if sequenceval[0] == "active":
            if currentseq[0] != 0:
                print(f"ERROR OCCURED IN SEQUENCE: \"{currentseq[0]}\"")
        sys.exit(1)

def Irange(num1, num2):
    rangelist = []
    for x in range(int(num1), int(num2)):
        rangelist.append(x)
    return rangelist
def changeval():
    FindVar("table__")[int(FindVar("location__"))] = FindVar("newval__")
    

# this will determine how a variable will be saved
def variable(Line):
    LineValues = Line.split(sep=None)

    if LineValues[2] == "\"":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        SplitLine.pop(0)
        SplitLine.pop(0)
        endofline = len(SplitLine) - 1
        SplitLine.pop(endofline)
        indexval = -1
        for x in SplitLine: 
            indexval += 1
            if x == '\\"':
                SplitLine[indexval] = "\""
        SaveVar(LineValues[0], " ".join(SplitLine))
    if LineValues[2] == "v\"":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        SplitLine.pop(0)
        thevstring = vString(" ".join(SplitLine))
        SaveVar(LineValues[0], thevstring)
    if LineValues[2] == "load_file":
        coolLine = Line.split(sep=None)
        SplitLine = Line.split(sep=None)
        varName = coolLine[0]
        SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[1] == "\"":
            SplitLine.pop(0)
            SplitLine.pop(0)

            endofline = len(SplitLine) - 1
            SplitLine.pop(endofline)
            file = " ".join(SplitLine)
            try:
                loadedfile = pickle.load(open(file, "rb"))
            except FileNotFoundError:
                for L in Content:
                    if file in L.split(sep=None):
                        if "load_file" in L.split(sep=None):
                            linenum = Content.index(L) + 1

                print(f"ERROR IN LINE({linenum}): FILE NOT FOUND | Couldn't find {file}")
                if sequenceval[0] == "active":
                    if currentseq[0] != 0:
                        print(f"ERROR OCCURED IN SEQUENCE: \"{currentseq[0]}\"")
                sys.exit(1)
            SaveVar(varName, loadedfile)
        else:
            SplitLine.pop(0)
            thevar = FindVar(SplitLine[0])
            loadedfile = pickle.load(open(thevar, "rb"))
            SaveVar(varName, loadedfile)

    if LineValues[2] == "py":
        try:
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], eval(" ".join(SplitLine)))
        except Exception as E:
            print(f"PYTHON ERROR: {E}")
            print(f"ERROR LINE: {Line}")
            print(f"Line Number: {Linenum[0]}")
            if sequenceval[0] == "active":
                if currentseq[0] != 0:
                    print(f"ERROR OCCURED IN SEQUENCE: \"{currentseq[0]}\"")
            sys.exit(1)    
        

    if LineValues[2] == "list":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        SplitLine.pop(0)
        SaveVar(LineValues[0], List(" ".join(SplitLine)))
    if LineValues[2] == "table":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        SplitLine.pop(0)
        SaveVar(LineValues[0], table(" ".join(SplitLine)))
    if LineValues[2] == "length":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        SplitLine.pop(0)
        SaveVar(LineValues[0], Length(" ".join(SplitLine)))

    if LineValues[2] == "from_list":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        SplitLine.pop(0)
        SaveVar(LineValues[0], FromList(" ".join(SplitLine)))
    if LineValues[2] in varmem:
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        SplitLine.pop(0)
        SaveVar(LineValues[0], FindVar(SplitLine[0]))
    if LineValues[2] in inprogramfunctions:
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        SplitLine.pop(0)
        Ifunction(" ".join(SplitLine))
        SaveVar(LineValues[0], FindVar(f"{SplitLine[0]}_return_val__"))



# this just makes it easier to determine what function to use
def IvoryFunctions(Line, function=None):
    if function == None:
        pass
    elif function == "print":
        Iprint(Line)

    elif function == "var":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        variable(" ".join(SplitLine))
    elif function == "var:":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        #typevar(" ".join(SplitLine))
    elif function == "save_file":
        save_file(Line)
    elif function == "load_file":
        load_file(Line)



# just more functions, ignore the typo
def NewFunctions(Line, function=None):
    SplitLine = Line.split(sep=None)
    if function == None:
        pass
    elif function == "sequence.use":
        Sequence(Line)
    elif function == "py":
        SplitLine.pop(0)
        Ipy(" ".join(SplitLine))
    elif function == "whiletrue":
        Iwhiletrue(Line)
    elif function == "while":
        Iwhile(Line)
    



    elif function == "list":
        List(Line)
    elif function == "from_list":
        FromList(Line)
    elif function == "for":
        ForLoop(Line)
    elif function == "i.test":
        Sequence(Line)
    elif function == "sequence.create":
        CreateSequence(Line)
    elif function == "try":
        Itry(Line)

    elif function == "break":
        Ibreak()


def Imakeserv(pages, pageData):
    global Serv
    class Serv(BaseHTTPRequestHandler):

        def do_GET(self):
            if self.path in pages:
                loc = pages.index(self.path)
                theseq = FindVar(f"{self.path}_onrequest")
                evaluate(f"sequence.use {theseq}")
                data = pageData[loc] 
            try:
                file_to_open = data
                self.send_response(200)
            except:
                file_to_open = "404 page not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))

def Irunserv(port):
    httpd = HTTPServer(('localhost', port), Serv)
    httpd.serve_forever()
# interpreter
# interpreter
# interpreter
# interpreter
# interpreter
# interpreter
# interpreter

def execute(Content):
    
    Iimport("import iv_built-in")
    variable("+ = \" + \"")
    variable("- = \" - \"")
    variable("* = \" * \"")
    variable("/ = \" / \"")
    variable("** = \" ** \"")
    variable("% = \" % \"")
    variable("// = \" // \"")
    variable("= = \" = \"")
    SaveVar("BLANK", "")
    SaveVar("SPACE", " ")
    SaveVar("VERSION", Version[0])
    SaveVar("THE_TRUTH", "Alli is the most beautiful girl in the entire world and I love her so so so so so so so so much and I always will. This is the truth in my heart")
    MakeProcess("ifval", "true")
    for Line in Content:
        i = ivoryImports[0]
        sequenceval[0] = "notactive"
        linenum = Linenum[0]
        if importing[0]:
            pass
        if not importing[0]:
            linenum += 1
        Linenum[0] = linenum
        LineValues = Line.split(sep=None)
        # IDENTIFYING VARIABLES
        if Line.startswith("var"):
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            variable(" ".join(SplitLine))


      

        if Line.startswith("import"):
            Iimport(Line)

        if Line.startswith("function"):
            inprogramfunctions.append(LineValues[1])
            functionsmem.append(Line)

        







    # LOADING FUNCTIONS
    # LOADING FUNCTIONS
    # LOADING FUNCTIONS
    # LOADING FUNCTIONS

        if LineValues == []:
            pass
        elif LineValues[0] == "from":
            Iimportfrom(Line)
        elif LineValues[0] == "*import":
            IimportAll(LineValues[1])
        #elif LineValues[0] in functions:
        #    IvoryFunctions(Line, LineValues[0])
        elif LineValues[0] in newerFunctions:
            NewFunctions(Line, LineValues[0])
        elif LineValues[0] not in inprogramfunctions:
            pass
        elif LineValues[0] in inprogramfunctions:
            Ifunction(Line)
        

        # stores a sequence properly in memory to be used in the future
        if Line.startswith("sequence"):
            if Line.startswith("sequence.use"):
                pass
            else:

                SplitLine = Line.split(sep=None)
                inprogramsequences.append(LineValues[1])
                
                if LineValues[2] != "{":
                    sequencesmem.append(Line)
                if LineValues[2] == "{":
                    seqLine = Content.index(Line)
                    MakeProcess("filecopy", Content)
                    filecopy = LoadProcess("filecopy")
                    for x in range(0, seqLine):

                        filecopy.pop(0)
                    try:
                        endofseq = filecopy.index("}\n")
 
                        for x in range(1, len(filecopy)):
                            nextseq = len(filecopy) + 20
                            if filecopy[x].startswith("sequence.use"):
                                pass
                            elif filecopy[x].startswith("sequence"):
                                nextseq = x
                                break
                        if nextseq < endofseq:
                            print("SYNTAX ERROR: Make sure the end of your sequence does not have spaces")
                            print("example: \"}    \"")
                            sys.exit(1)
                    except ValueError:

                        try:
                            endofseq = filecopy.index("}")
                            for x in range(1, len(filecopy)):
                                nextseq = len(filecopy) + 20
                                if filecopy[x].startswith("sequence.use"):
                                    pass
                                elif filecopy[x].startswith("sequence"):
                                    nextseq = x
                                    break
                            if nextseq < endofseq:
                                print("SYNTAX ERROR: Make sure the end of your sequence does not have spaces")
                                print("example: \"}    \"")
                                sys.exit(1)
                        except ValueError:
                            print("SYNTAX ERROR: Make sure the end of your sequence does not have spaces")
                            print("example: \"}    \"")
                            sys.exit(1)
                    for d in range(Content.index(Line) + 1, Content.index(filecopy[endofseq - 1]) + 1):
                        Content.pop(Content.index(Line) + 1)
                        Linenum[0] += 1
                    for fd in range(endofseq, len(filecopy)):
                        filecopy.pop(endofseq)
                    filecopylist = []
                    for value in filecopy:
                        if value == "}":
                            new = value
                        else:
                            new = value.split(sep=None)
                        new = " ".join(new)
                        filecopylist.append(new)
                        filecopylist.append(";")
                    filecopylist = " ".join(filecopylist)
                    filecopylist = filecopylist.split(sep=None)
                    filecopylist.pop(2)
                    filecopylist.pop(2)
                    sequencesmem.append(" ".join(filecopylist))
                    







        if Line.startswith("print"):
            Iprint(Line)


        if Line.startswith("save_file"):
            save_file(Line)





        if Line.startswith("if"):
            Iif(Line)
        if Line.startswith("else"):
            Ielse(Line)



        if Line.startswith("print_line"):
            print(Content[int(LineValues[1]) - 1])


if __name__ == '__main__':
  args = sys.argv[1:]
  if args:
    if args[0] == "run":
        filename = args[1]
        Content = open(filename, "r").readlines()
        execute(Content)
    if args[0] == "version":
        print(Version[0])
    if args[0] == "ver":
        print(Version[0])
  else:
    filename = input("enter the name of your file here:")
    print("")
    Content = open(f"{filename}.iv", "r").readlines()
    execute(Content)
