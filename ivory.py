import pickle
import sys
import random
import Ivory_imports as i
from Ivory_files import CreateFile, SaveToFile, LoadFromFile
memory = []
varmem = []
functions = ["print", "randnum", "save_file", "load_file", "var", "add", "sub"]
newerFunctions = ["sequence", "sequence.use", "py", "while", "whiletrue", "display_sequence", "i.create_file", "i.save_to_file", "i.load_from_file", "list", "from_list", "for", "test", "sequence.create", "try", "append", "break"]
inprogramfunctions = []
functionsmem = []
processmem = []
processdata = []
inprogramsequences = []
sequencesmem = []
filename = input("Enter the name of your file here:")
print("")
Content = open(f"{filename}.iv", "r").readlines()
forvalue = []


# looks through the list of saved variables and finds the corresponding data
def FindVar(var):
    try:
        VarNumVal = varmem.index(var)
        return memory[VarNumVal]
    # tries to return an error for a specific line and variable
    except ValueError:
        
        for L in Content:
            if var in L.split(sep=None):
                if L.startswith("var"):
                    if L.split(sep=None)[3] == var:
                        pass
                    linenum = Content.index(L) + 1
                
                else:
                    linenum = Content.index(L) + 1
        try:
            print(f"ERROR IN LINE({linenum}): UNDEFINED VARIABLE | Could not find \"{var}\" ")
        except UnboundLocalError:
            print(f"ERROR: UNDEFINED VARIABLE | Could not find \"{var}\" ")
        sys.exit(1)

        
# saves a variable to the list of variables or rewrites an already saved variable
def SaveVar(varname, varvalue):
    if varname in varmem:
        varnum = varmem.index(varname)
        memory[varnum] = varvalue
    else:
        varmem.append(varname)
        memory.append(varvalue)

# creates a sort of a global variable (mostly used for duplicating lists or some specific status)
def MakeProcess(name, var):
  var = list(var)
  if name in processmem:
    namenum = processmem.index(name)
    processdata[namenum] = var
  else:
    processmem.append(name)
    processdata.append(var)

# loads a saved process
def LoadProcess(name):
  processval = processmem.index(name)
  thevar = processdata[processval]
  return thevar

# looks through the list of saved functions and returns its data
def FindFunc(function):
    FuncNumVal = inprogramfunctions.index(function)
    return functionsmem[FuncNumVal]

# looks through the list of saved sequences and returns its data
def FindSeq(sequence):
    try:
        FuncNumVal = inprogramsequences.index(sequence)
        return sequencesmem[FuncNumVal]
    except ValueError:
        for L in Content:
            if sequence in L.split(sep=None):
                if L.startswith("var"):
                    if L.split(sep=None)[3] == sequence:
                        pass
                    linenum = Content.index(L) + 1
                
                else:
                    linenum = Content.index(L) + 1
        print(f"ERROR IN LINE({linenum}): UNDEFINED SEQUENCE | Could not find \"{sequence}\" ")
        sys.exit(1)
        




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



# i.create_file " the.txt "

def Iopen(Line):
    SplitLine = Line.split(sep=None)

def ICreateFile(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    if SplitLine[0] == "\"":
        SplitLine.pop(0)
        SplitLine.pop(len(SplitLine) - 1)
        pickle.dump([[], []], open(" ".join(SplitLine), "wb"))

# filename, content, contentname
# i.save_to_file " the.txt " " 1 " " level "

def Ibreak():
    forvalue.append("notactive")
    


def ISaveToFile(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    if SplitLine[0] == "\"":
        SplitLine.pop(0)
        endofcurrent = SplitLine.index("\"")
        MakeProcess("current", SplitLine)
        current = LoadProcess("current")
        for x in range(endofcurrent, len(SplitLine)):
            current.pop(endofcurrent)
        print(current)
        FileName = " ".join(current)
        loadedfile = pickle.load(open(FileName, "rb"))
        for x in range(0, SplitLine.index("\"") + 1):
            SplitLine.pop(0)
    else:
        FileName = FindVar(SplitLine[0])
        loadedfile = pickle.load(open(FindVar(SplitLine[0]), "rb"))
        SplitLine.pop(0)
    
    if SplitLine[0] == "\"":
        SplitLine.pop(0)
        endofcurrent = SplitLine.index("\"")
        MakeProcess("filecontent", SplitLine)
        FileCurrent = LoadProcess("filecontent")
        for x in range(endofcurrent, len(SplitLine)):
            FileCurrent.pop(endofcurrent)
        print(FileCurrent)
        filecontent = " ".join(FileCurrent)
        for x in range(0, SplitLine.index("\"") + 1):
            SplitLine.pop(0)
    else:
        filecontent = FindVar(SplitLine[0])
        SplitLine.pop(0)

    if SplitLine[0] == "\"":
        SplitLine.pop(0)
        endofcurrent = SplitLine.index("\"")
        MakeProcess("contentname", SplitLine)
        ContentCurrent = LoadProcess("contentname")
        for x in range(endofcurrent, len(SplitLine)):
            ContentCurrent.pop(endofcurrent)
        print(ContentCurrent)
        contentname = " ".join(ContentCurrent)
        for x in range(0, SplitLine.index("\"") + 1):
            SplitLine.pop(0)
    else:
        contentname = FindVar(SplitLine[0])
        SplitLine.pop(0)
    if contentname in loadedfile[0]:
        loadedfile[1] = filecontent
        loadedfile[0] = contentname
    else:
        loadedfile[1].append(filecontent)
        loadedfile[0].append(contentname)
    pickle.dump(loadedfile, open(FileName, "wb"))

# i.load_from_file " the.txt " " level "
def ILoadFromFile(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    if SplitLine[0] == "\"":
        SplitLine.pop(0)
        endofcurrent = SplitLine.index("\"")
        MakeProcess("current", SplitLine)
        current = LoadProcess("current")
        for x in range(endofcurrent, len(SplitLine)):
            current.pop(endofcurrent)

        FileName = " ".join(current)
        loadedfile = pickle.load(open(FileName, "rb"))
        for x in range(0, SplitLine.index("\"") + 1):
            SplitLine.pop(0)
    else:
        FileName = FindVar(SplitLine[0])
        loadedfile = pickle.load(open(FindVar(SplitLine[0]), "rb"))
        SplitLine.pop(0)

    if SplitLine[0] == "\"":
        SplitLine.pop(0)
        endofcurrent = SplitLine.index("\"")
        MakeProcess("filecontent", SplitLine)
        FileCurrent = LoadProcess("filecontent")
        for x in range(endofcurrent, len(SplitLine)):
            FileCurrent.pop(endofcurrent)

        contentname = " ".join(FileCurrent)
        for x in range(0, SplitLine.index("\"") + 1):
            SplitLine.pop(0)
    else:
        contentname = FindVar(SplitLine[0])
        SplitLine.pop(0)

    return LoadFromFile(FileName, contentname)

# load_list " thefunny.txt " " 0 "
def LoadList(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    if SplitLine[0] == "\"":
        SplitLine.pop(0)
        endofcurrent = SplitLine.index("\"")
        MakeProcess("current", SplitLine)
        current = LoadProcess("current")
        for x in range(endofcurrent, len(SplitLine)):
            current.pop(endofcurrent)

        FileName = " ".join(current)
        loadedfile = pickle.load(open(FileName, "rb"))
        for x in range(0, SplitLine.index("\"") + 1):
            SplitLine.pop(0)
    else:
        FileName = FindVar(SplitLine[0])
        loadedfile = pickle.load(open(FindVar(SplitLine[0]), "rb"))
        SplitLine.pop(0)

    if SplitLine[0] == "\"":
        SplitLine.pop(0)
        endofcurrent = SplitLine.index("\"")
        MakeProcess("filecontent", SplitLine)
        FileCurrent = LoadProcess("filecontent")
        for x in range(endofcurrent, len(SplitLine)):
            FileCurrent.pop(endofcurrent)

        listindex = " ".join(FileCurrent)
        for x in range(0, SplitLine.index("\"") + 1):
            SplitLine.pop(0)
    else:
        listindex = FindVar(SplitLine[0])
        SplitLine.pop(0)
    return pickle.load(open(FileName, "rb"))[int(listindex)]

# length
# returns the length of a string or list
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

# creates a list
# list [ cool ] [ the bigger funny ]
def List(Line):
    SplitLine = Line.split(sep=None)
    newlist = []
    SplitLine.pop(0)
    listval = SplitLine.count("]")
    #print(SplitLine)
    for d in range(0, listval):
        MakeProcess("currentvar", SplitLine)
        currentvar = LoadProcess("currentvar")
        currentvar.pop(0)
        #print(currentvar)


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
        #print(currentvar)
    return newlist

# appends a value to a list
def AddToList(Line):
    SplitLine = Line.split(sep=None)
    LineValues = Line.split(sep=None)
    SplitLine.pop(0)
    thevar = FindVar(LineValues[1])
    SplitLine.pop(0)
    if SplitLine[0] == "\"":
        SplitLine.pop(0)
        SplitLine.pop(len(SplitLine) - 1)
        thevar.append(" ".join(SplitLine))
        SaveVar(LineValues[1], thevar)
    else:
        thevar.append(FindVar(SplitLine[0]))
    SaveVar(LineValues[1], thevar)


# removes a value from a list
def RemoveFromList(Line):
    SplitLine = Line.split(sep=None)
    LineValues = Line.split(sep=None)
    thevar = FindVar(LineValues[1])
    thevarname = LineValues[1]
    SplitLine.pop(0)
    SplitLine.pop(0)
    try:
        indexval = int(SplitLine[0])
    except ValueError:
        indexval = int(FindVar(SplitLine[0]))
    thevar.pop(indexval)

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
def Irange(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    if SplitLine[0] == "(":
        SplitLine.pop(0)
        startval = FindVar(SplitLine[0])
        SplitLine.pop(0)
        SplitLine.pop(0)
    else:
        startval = SplitLine[0]
        SplitLine.pop(0)
    SplitLine.pop(0)
    if SplitLine[0] == "(":
        SplitLine.pop(0)
        endval = FindVar(SplitLine[0])
        SplitLine.pop(0)
        SplitLine.pop(0)
    else:
        endval = SplitLine[0]
        SplitLine.pop(0)
    rangelist = []
    for b in range(int(startval), int(endval)):
        rangelist.append(b)
    return rangelist

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
    if SplitLine[0] == "range":
        endofrange = SplitLine.index("{{")
        MakeProcess("newline", SplitLine)
        newline = LoadProcess("newline")
        for d in range(endofrange, len(newline)):
            newline.pop(endofrange)
        newlist = Irange(" ".join(newline))
    else:
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

def randnum(Line):
    Splitline = Line.split(sep=None)
    if Splitline[1] == "(":
        num1 = FindVar(Splitline[2])
        if Splitline[4] == "(":
            num2 = FindVar(Splitline[5])
        if Splitline[4] != "(":
            num2 = Splitline[4]

    if Splitline[1] != "(":
        num1 = Splitline[1]
        if Splitline[2] == "(":
            num2 = FindVar(Splitline[3])
        if Splitline[2] != "(":
            num2 = Splitline[2]
    return random.randint(int(num1), int(num2))

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
        # This finds sequences and imports them to be used in functions
        
        

# sequence seq_name print " hello there " ; var cool = input what is your name? %} {% print v" hello there { cool } " ;

# sequence.use seq_name

# executes a sequence of code that has been stored in memory
def Sequence(Line):
    LineValues = Line.split(sep=None)
    newline = FindSeq(LineValues[1])
    SplitLine = newline.split(sep=None)
    SplitLine.pop(0)
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
        if currentline == []:
            pass
        elif currentline[0] == "var":
            variable(" ".join(currentline))
        elif currentline[0] == "if":
            Iif(" ".join(currentline))
        for value in currentline:
            SplitLine.pop(0)
        SplitLine.pop(0)

# evaluates a line of code and executes the corresponding function
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
    except Exception as E:
        print(f"ERROR CODE: {E} | LINE: {Line}")
    
        
            

# this is honestly really weird and I forgot I did this, continue on 
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


# this is made to display a sequence in multiple lines of code before a sequence could be written on multiple lines
def DisplaySequence(Line):
    LineValues = Line.split(sep=None)
    NewerLine = FindSeq(LineValues[1]).split(sep=None)
    lines = NewerLine.count(";")
    NewerLine.pop(0)
    NewerLine.pop(0)
    for line in range(0, lines):
        MakeProcess("currentseq", NewerLine)
        currentseq = LoadProcess("currentseq")
        endofseq = currentseq.index(";")
        for x in range(endofseq, len(currentseq)):
            currentseq.pop(endofseq)
        for val in currentseq:
            NewerLine.pop(0)
        NewerLine.pop(0)
        result = " ".join(currentseq)
        print(f"{result} ;")


# this evaluates a stored function
def Ifunction(Line):
    LineValues = Line.split(sep=None)
    NewLine = FindFunc(LineValues[0])
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
                        ELine = Line
                        print(f"ERROR Line: {Line} | SYNTAX ERROR | Missing required \" at end of statement")
                        sys.exit(1)     
                    for v in range(endofcurrentvar, len(currentvar)):
                        currentvar.pop(endofcurrentvar)
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
        try:
            evaluate(" ".join(currentline))
        except Exception as E:
            print(f"PYTHON ERROR: {E}")
            print(f"ERROR LINE: {Line}")
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

# not important now that ivory deals with number values mostly on it's own
def Iint(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    try:
        number = int(SplitLine[0])
    except ValueError:
        number = int(FindVar(SplitLine[0]))
    return number

def Ifloat(Line):
    SplitLine = Line.split(sep=None)
    SplitLine.pop(0)
    try:
        number = float(SplitLine[0])
    except ValueError:
        number = float(FindVar(SplitLine[0]))
    return number

# this is a while loop, needs some work though
def Iwhile(Line):

# WHILE EQUAL TO
# WHILE EQUAL TO
# WHILE EQUAL TO

# LineValues is for the unedited split version of the line
    LineValues = Line.split(sep=None)
    if "==" in LineValues:

        SplitLine = Line.split(sep=None)
# The first variable for comparison is the 2nd value in the line
        var1 = FindVar(LineValues[1])
        SplitLine.pop(0)
        SplitLine.pop(0)
        SplitLine.pop(0)
# This checks if the second var is going to be a string or a variable
        if SplitLine[0] == "\"":
            SplitLine.pop(0)
            endofval = SplitLine.index("\"")
            endofline = len(SplitLine)
            for x in range(endofval, endofline):
                SplitLine.pop(endofval)

            var2 = " ".join(SplitLine)
        else:
            var2 = FindVar(LineValues[3])
# I think that useableLine is just for a new line but I'm not sure why I did it this way
# I made this a long time ago
        useableLine = Line.split(sep=None)
        LineStartVal = useableLine.index("sequence.use")
        for z in range(0, LineStartVal):
            useableLine.pop(0)

        while var2 == FindVar(LineValues[1]):

            Sequence(" ".join(useableLine))

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

        
        while var1 < var2:
            Sequence(" ".join(useableLine))
            var1 = float(FindVar(LineValues[1]))
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
    newstring = " ".join(SplitString)
    return newstring


# sub ( health ) - ( damage )
# sub health -= ( damage )

# this is trash, forget you saw this
def Sub(Line):
    SplitLine = Line.split(sep=None)
    if "-" in SplitLine:
        SplitLine.pop(0)
        if SplitLine[0] == "(":
            SplitLine.pop(0)
            num1 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            num1 = SplitLine[0]
        SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "(":
            SplitLine.pop(0)
            num2 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            num2 = SplitLine[0]
        return float(num1) - float(num2)
    if "-=" in SplitLine:
        SplitLine.pop(0)


        theval = FindVar(SplitLine[0])
        thevalname = SplitLine[0]

        SplitLine.pop(0)
        SplitLine.pop(0)


        if SplitLine[0] == "(":
            SplitLine.pop(0)
            otherval = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            otherval = SplitLine[0]
        try:
            result = float(theval) - float(otherval)
            SaveVar(thevalname, result)
        except ValueError:
            print("ERROR LINE:", Line)



# try CODE ; except ERROR ; OTHERCODE
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





# avert your eyes
def product(Line):
    SplitLine = Line.split(sep=None)
    if "*" in SplitLine:
        SplitLine.pop(0)
        if SplitLine[0] == "(":
            SplitLine.pop(0)
            num1 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            num1 = SplitLine[0]
        SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "(":
            SplitLine.pop(0)
            num2 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            num2 = SplitLine[0]
        return float(num1) * float(num2)
    if "*=" in SplitLine:
        SplitLine.pop(0)


        theval = FindVar(SplitLine[0])
        thevalname = SplitLine[0]

        SplitLine.pop(0)

        SplitLine.pop(0)


        if SplitLine[0] == "(":
            SplitLine.pop(0)
            otherval = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            otherval = SplitLine[0]
        result = float(theval) * float(otherval)
        SaveVar(thevalname, result)

# another useless math function
def div(Line):
    SplitLine = Line.split(sep=None)
    if "/" in SplitLine:
        SplitLine.pop(0)
        if SplitLine[0] == "(":
            SplitLine.pop(0)
            num1 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            num1 = SplitLine[0]
        SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "(":
            SplitLine.pop(0)
            num2 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            num2 = SplitLine[0]
        return float(num1) / float(num2)
    if "/=" in SplitLine:
        SplitLine.pop(0)


        theval = FindVar(SplitLine[0])
        thevalname = SplitLine[0]

        SplitLine.pop(0)
        SplitLine.pop(0)


        if SplitLine[0] == "(":
            SplitLine.pop(0)
            otherval = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            otherval = SplitLine[0]
        result = float(theval) / float(otherval)
        SaveVar(thevalname, result)

# ew
def add(Line):
    SplitLine = Line.split(sep=None)
    if "+" in SplitLine:
        SplitLine.pop(0)
        if SplitLine[0] == "(":
            SplitLine.pop(0)
            num1 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            num1 = SplitLine[0]
        SplitLine.pop(0)
        SplitLine.pop(0)
        if SplitLine[0] == "(":
            SplitLine.pop(0)
            num2 = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            num2 = SplitLine[0]
        return float(num1) + float(num2)
    if "+=" in SplitLine:
        SplitLine.pop(0)


        theval = FindVar(SplitLine[0])
        thevalname = SplitLine[0]

        SplitLine.pop(0)
        SplitLine.pop(0)


        if SplitLine[0] == "(":
            SplitLine.pop(0)
            otherval = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            otherval = SplitLine[0]
        result = float(theval) + float(otherval)
        SaveVar(thevalname, result)


# if var == " hello " {% sequence.use seq_name %} else {% print " not hello " %}
# this is an if statement, the example above was for version 1.0.0
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
                return True
            
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
            NewLine = " ".join(SplitLine)
            print(NewLine)
        elif SplitLine[0] == "v\"":
            print(vString(" ".join(SplitLine)))
        elif SplitLine[0] == "randnum":
            print(randnum(" ".join(SplitLine)))
        else:
            foundvar = FindVar(SplitLine[0])
            print(foundvar)
    except IndexError:
        for L in Content:
            if Line in L:
                linenum = Content.index(L) + 1
        print(f"ERROR IN LINE({linenum}): UNFINISHED FUNCTION | Missing insructions after print statement")
        sys.exit(1)


# this will determine how a variable will be saved
def variable(Line):
    LineValues = Line.split(sep=None)
    try:
        if LineValues[2] == "\"":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SplitLine.pop(0)
            endofline = len(SplitLine) - 1
            SplitLine.pop(endofline)
            SaveVar(LineValues[0], " ".join(SplitLine))
        if LineValues[2] == "v\"":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            thevstring = vString(" ".join(SplitLine))
            SaveVar(LineValues[0], thevstring)
        if LineValues[2] == "sub":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], Sub(" ".join(SplitLine)))
        if LineValues[2] == "add":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], add(" ".join(SplitLine)))
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
                    sys.exit(1)
                SaveVar(varName, loadedfile)
            else:
                SplitLine.pop(0)
                thevar = FindVar(SplitLine[0])
                loadedfile = pickle.load(open(thevar, "rb"))
                SaveVar(varName, loadedfile)
        if LineValues[2] == "randnum":
            varName = LineValues[0]
            LineValues.pop(0)
            LineValues.pop(0)
            NewLine = " ".join(LineValues)
            number = randnum(NewLine)
            SaveVar(varName, number)
        if LineValues[2] == "py":
            
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SplitLine.pop(0)

            SaveVar(LineValues[0], eval(" ".join(SplitLine)))
            
            
        if LineValues[2] == "product":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], product(" ".join(SplitLine)))
        if LineValues[2] == "i.load_from_file":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], ILoadFromFile(" ".join(SplitLine)))
        if LineValues[2] == "i.load_list":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], LoadList(" ".join(SplitLine)))
        if LineValues[2] == "list":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], List(" ".join(SplitLine)))
        if LineValues[2] == "length":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], Length(" ".join(SplitLine)))
        if LineValues[2] == "range":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], Irange(" ".join(SplitLine)))
        if LineValues[2] == "from_list":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], FromList(" ".join(SplitLine)))
        if LineValues[2] == "int":
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            SplitLine.pop(0)
            SaveVar(LineValues[0], Iint(" ".join(SplitLine)))
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
    except IndexError:
        print(f"SYNTAX ERROR: When creating variable \"{LineValues[0]}\" something went wrong")
        sys.exit(1)


# this just makes it easier to determine what function to use
def IvoryFunctions(Line, function=None):
    if function == None:
        pass
    elif function == "print":
        Iprint(Line)
    elif function == "randnum":
        randnum(Line)
    elif function == "var":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        variable(" ".join(SplitLine))
    elif function == "save_file":
        save_file(Line)
    elif function == "load_file":
        load_file(Line)
    elif function == "sub":
        Sub(Line)
    elif function == "add":
        add(Line)

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
    elif function == "display_sequence":
        DisplaySequence(Line)
    elif function == "i.create_file":
        ICreateFile(Line)
    elif function == "i.save_to_file":
        ISaveToFile(Line)
    elif function == "i.load_from_file":
        ILoadFromFile(Line)
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
    elif function == "append":
        AddToList(Line)
    elif function == "break":
        Ibreak()


# interpreter
# interpreter
# interpreter
# interpreter
# interpreter
# interpreter
# interpreter

# this executes a .iv file using all of the functions above
def execute(Content):
    linenum = 0
    Iimport("import iv_built-in")
    variable("+ = \" + \"")
    variable("- = \" - \"")
    variable("* = \" * \"")
    variable("/ = \" / \"")
    variable("** = \" ** \"")
    variable("% = \" % \"")
    variable("// = \" // \"")
    for Line in Content:
        linenum += 1
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

        




        if Line.startswith("sub"):
            Sub(Line)


    # LOADING FUNCTIONS
    # LOADING FUNCTIONS
    # LOADING FUNCTIONS
    # LOADING FUNCTIONS

        if LineValues == []:
            pass
        elif LineValues[0] == "from":
            Iimportfrom(Line)
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

execute(Content)