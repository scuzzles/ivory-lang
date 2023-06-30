import pickle
import sys
import random
import Ivory_imports as i
from Ivory_files import CreateFile, SaveToFile, LoadFromFile
memory = []
varmem = []
functions = ["print", "input", "randnum", "save_file", "load_file", "var", "add", "sub"]
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



def FindVar(var):
    try:
        VarNumVal = varmem.index(var)
        return memory[VarNumVal]
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
        # print(SplitLine)
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

# from cringe import tyler
# inprogramfunctions.append(LineValues[1])
#         functionsmem.append(Line)
def Iimportfrom(Line):
    LineValues = Line.split(sep=None)
    ImportContent = open(f"{LineValues[1]}.iv", "r").readlines()
    for ImportedLine in ImportContent:
        SplitLine = ImportedLine.split(sep=None)
        if SplitLine[1] == LineValues[3]:
            inprogramfunctions.append(SplitLine[1])
            functionsmem.append(ImportedLine)
            #print('BRUH')
        else:
            pass
def Iimport(Line):
    LineValues = Line.split(sep=None)
    ImportContent = open(f"{LineValues[1]}.iv", "r").readlines()
    for ImportedLine in ImportContent:
        SplitLine = ImportedLine.split(sep=None)

        if SplitLine == []:
            pass
        elif SplitLine[0] == "function":
            inprogramfunctions.append(SplitLine[1])
            functionsmem.append(ImportedLine)
        else:
            pass
        

# sequence seq_name print " hello there " ; var cool = input what is your name? %} {% print v" hello there { cool } " ;

# sequence.use seq_name

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

# sequence funny print " hello world! " ; var name = input enter name here: ; if name == " funnyman " {{ print " you are a stinky " }} ;
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

# sequence seqname print

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


# function hello [ enteredName ] print v" hello there enteredName " ;
# hello " tyrae "
def Ifunction(Line):
    LineValues = Line.split(sep=None)
    NewLine = FindFunc(LineValues[0])
    PureList = NewLine.split(sep=None)
    SplitLine = NewLine.split(sep=None)
    SplitLine.pop(0)
    SplitLine.pop(0)
    SplitLine.pop(0)
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
                endofcurrentvar = currentvar.index("\"")
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
                SaveVar(f"{PureList[1]}_return_val", " ".join(currentline))
            else:
                SaveVar(f"{PureList[1]}_return_val", FindVar(currentline[0]))

        SplitLine.pop(0)

def Iwhiletrue(Line):
    WhileSplit = Line.split(sep=None)
    WhileSplit.pop(0)
    while True:
        Sequence(" ".join(WhileSplit))

# int " 34 "
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


def Iwhile(Line):

    LineValues = Line.split(sep=None)
    if "==" in LineValues:

        SplitLine = Line.split(sep=None)
        var1 = FindVar(LineValues[1])
        #print(var1)
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
            #print(var2)
        else:
            var2 = FindVar(LineValues[3])
        useableLine = Line.split(sep=None)
        LineStartVal = useableLine.index("sequence.use")
        for z in range(0, LineStartVal):
            useableLine.pop(0)

        while var2 == FindVar(LineValues[1]):

            Sequence(" ".join(useableLine))

# v" hello there %{ var } you are chatting with %{ othervar } "
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
        #print(SplitLine)
        SplitLine.pop(0)


        if SplitLine[0] == "(":
            SplitLine.pop(0)
            otherval = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            otherval = SplitLine[0]
        #print(thevalname)
        #print(otherval)
        try:
            result = float(theval) - float(otherval)
            SaveVar(thevalname, result)
        except ValueError:
            print("ERROR LINE:", Line)



# try CODE ; except ERROR ; OTHERCODE

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
        #print(SplitLine)
        SplitLine.pop(0)


        if SplitLine[0] == "(":
            SplitLine.pop(0)
            otherval = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            otherval = SplitLine[0]
        #print(thevalname)
        #print(otherval)
        result = float(theval) * float(otherval)
        SaveVar(thevalname, result)

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
        #print(SplitLine)
        SplitLine.pop(0)


        if SplitLine[0] == "(":
            SplitLine.pop(0)
            otherval = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            otherval = SplitLine[0]
        #print(thevalname)
        #print(otherval)
        result = float(theval) / float(otherval)
        SaveVar(thevalname, result)

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
        #print(SplitLine)
        SplitLine.pop(0)


        if SplitLine[0] == "(":
            SplitLine.pop(0)
            otherval = FindVar(SplitLine[0])
            SplitLine.pop(0)
        else:
            otherval = SplitLine[0]
        #print(thevalname)
        #print(otherval)
        result = float(theval) + float(otherval)
        SaveVar(thevalname, result)


# if var == " hello " {% sequence.use seq_name %} else {% print " not hello " %}

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
                        SaveVar(f"{PureList[1]}_return_val", " ".join(currentline))
                    else:
                        SaveVar(f"{PureList[1]}_return_val", FindVar(currentline[0]))
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
                        SaveVar(f"{PureList[1]}_return_val", " ".join(currentline))
                    else:
                        SaveVar(f"{PureList[1]}_return_val", FindVar(currentline[0]))

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
                        SaveVar(f"{PureList[1]}_return_val", " ".join(currentline))
                    else:
                        SaveVar(f"{PureList[1]}_return_val", FindVar(currentline[0]))
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
                        SaveVar(f"{PureList[1]}_return_val", " ".join(currentline))
                    else:
                        SaveVar(f"{PureList[1]}_return_val", FindVar(currentline[0]))
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
            #print(SplitLine)
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
            #print(SplitLine)
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
            #print(SplitLine)
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

def Ipy(Line):
    eval(Line)


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



def variable(Line):
    LineValues = Line.split(sep=None)

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
    # print(LineValues)
    # print(LineValues[2])
    if LineValues[2] == "input":
        # if LineValues.index("input") == 2:
        varname = LineValues[0]
        SplitLine = Line.split(sep=None)
        for x in range(0, 3):
            SplitLine.pop(0)
        NewLine = " ".join(SplitLine)
        inp = input(NewLine)
        SaveVar(varname, inp)
    if LineValues[2] == "sub":
        SplitLine = Line.split(sep=None)
        SplitLine.pop(0)
        SplitLine.pop(0)
        SaveVar(LineValues[0], Sub(" ".join(SplitLine)))
# bruh = sub= num -= 10
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
                #print("PYTHON ERROR TYPE: FileNotFoundError")
                sys.exit(1)
            SaveVar(varName, loadedfile)
        else:
            SplitLine.pop(0)
            # print(SplitLine)
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
        SaveVar(LineValues[0], FindVar(f"{SplitLine[0]}_return_val"))


# THE ULTIMATE FUNCTION
# THE ULTIMATE FUNCTION
# THE ULTIMATE FUNCTION
# THE ULTIMATE FUNCTION
# THE ULTIMATE FUNCTION
# THE ULTIMATE FUNCTION
# THE ULTIMATE FUNCTION
# THE ULTIMATE FUNCTION

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

# "i.create_file", "i.save_to_file", "i.load_from_file"
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

def execute(Content):
    linenum = 0
    Iimport("import iv_built-in")
    variable("+ = \" + \"")
    variable("- = \" - \"")
    variable("* = \" * \"")
    variable("/ = \" / \"")
    for Line in Content:
        linenum += 1
        LineValues = Line.split(sep=None)
        # IDENTIFYING VARIABLES
        if Line.startswith("var"):
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            variable(" ".join(SplitLine))





            #else:
            #    varmem.append(LineValues[0])
            #    SplitLine = Line.split(sep=None)
            #    SplitLine.pop(0)
            #    SplitLine.pop(0)
            #    if SplitLine[0] == "\"":
            #        SplitLine.pop(0)
            #        endofline = len(SplitLine) - 1
            #        SplitLine.pop(endofline)
            #        NewLine = " ".join(SplitLine)
                    # print(NewLine)
            #        memory.append(NewLine)
            #    else:
            #        memory.append(memory[varmem.index(SplitLine[0])])q


        # function test [ num ] { return randnum 1 ( number ) }




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
        

# NEW SEQ
# sequence ex { CODE }

        if Line.startswith("sequence"):
            #print(Line)
            if Line.startswith("sequence.use"):
                pass
            else:
                #print("fsdfsdfsdfsdfsd")
                SplitLine = Line.split(sep=None)
                inprogramsequences.append(LineValues[1])
                
                if LineValues[2] != "{":
                    sequencesmem.append(Line)
                if LineValues[2] == "{":
                    #print("AAAAAA")
                    
                    seqLine = Content.index(Line)
                    #print(seqLine)
                    MakeProcess("filecopy", Content)
                    filecopy = LoadProcess("filecopy")
                    for x in range(0, seqLine):

                        filecopy.pop(0)
                    #print(filecopy)
                    try:
                        endofseq = filecopy.index("}\n")
                        #print(endofseq)
                        for x in range(1, len(filecopy)):
                            nextseq = len(filecopy) + 20
                            if filecopy[x].startswith("sequence.use"):
                                pass
                            elif filecopy[x].startswith("sequence"):
                                nextseq = x
                                break
                        #print(f"next: {nextseq}")
                        #print(f"end: {endofseq}")
                        if nextseq < endofseq:
                            #print(nextseq)
                            print("SYNTAX ERROR: Make sure the end of your sequence does not have spaces")
                            print("example: \"}    \"")
                            sys.exit(1)
                    except ValueError:
                        #print("OKAY BUD")
                        try:
                            endofseq = filecopy.index("}")
                            #print(endofseq)
                            for x in range(1, len(filecopy)):
                                nextseq = len(filecopy) + 20
                                if filecopy[x].startswith("sequence.use"):
                                    pass
                                elif filecopy[x].startswith("sequence"):
                                    nextseq = x
                                    break
                            #print(f"next: {nextseq}")
                            #print(f"end: {endofseq}")
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

        if Line.startswith("input"):
            SplitLine = Line.split(sep=None)
            SplitLine.pop(0)
            NewLine = " ".join(SplitLine)
            inp = input(NewLine)
            memory.append(inp)

    # save " test " " file.txt "
        if Line.startswith("save_file"):
            save_file(Line)




    # IF THAN EX: if 1 == f print test else print broken
        if Line.startswith("if"):
            Iif(Line)
        if Line.startswith("else"):
            Ielse(Line)



        if Line.startswith("print_line"):
            print(Content[int(LineValues[1]) - 1])

execute(Content)