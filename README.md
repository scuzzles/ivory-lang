# A Short Summary
Ivory is a unique programming language made in part with the intent of making programming less complicated, some things are very odd because ivory is not made traditionally but if you take the time to learn it, so long as you have an understanding of python you should find that almost anything is possible with the combination of the two


## ivory basics
Ivory was partially with the intent of making programming less complicated; (in some ways) for instance, when using a variable "x" with the value of "4" in ivory you do not need to worry about whether it is an integer or string because ivory will convert it on its own. you also do not need parenthsis to use a function. For instance, here is how you might add to numbers with an integer result: 
```
var test = " 4 " 
var othernum = " 3 "
var result = add_int test + othernum
print result
```
RESULT:
```
7
```
**Note**
If you do not add spaces between each quotation and the following data your program will not work correctly
here is an example:
```
var test = " 4 " 
var othernum = "3"
var result = add_int test + othernum
print result
```
RESULT:
```
ERROR IN LINE(3): UNDEFINED VARIABLE | Could not find "othernum"
```
This happens because when ivory's interpreter is looking to assign a variable it looks for either another variable or for a quotation mark seperate from any other objects, so when ivory looked for a value for othernum nothing had been assigned. 

Please note that the choice to use the "result" variable was intentional. Attempting to use a function inside of another function will not work unless you first assign the result to a function

### Using Functions
Although I have briefly discussed functions, some important details have been left out. Here is how to use a funciton without using variables.
```
var added = add_int " 2 " + " 3 "
print added
``` 
RESULT:
```
5
```
This is a fairly simple function to use but it's also not that difficult to create, this is because ivory has a built in "py" function that allows you to execute single python lines. Here is what the "add_int" function looks like:
```
function add_int [ NUM1 op num2 ] var RESULT = py int(FindVar("NUM1")) + int(FindVar("num2")) ; return RESULT ;
```
now it may look odd that it's made entirely in one line of code but this is required when writing functions in ivory. Each function in ivory is written on one line and to have seperate operations you just add a semicolon where you would end your line but that does not allow you to go to a new line. This is something a plan to remove in the future. Another important thing to note is the way the functions are saving variables. All variables are saved with absolutely no seperation, if you import a module and a function you use from that module has a variable in it with the same name as your own then you will either alter the variable from the module or it will change it in yours. For instance, if a math module adds to a variable named "num" then and your program has the same variable, your variable will change. In the future all built-in Ivory modules will have fully capitalized variables, to avoid clashing do not use all capital variable names in your programs.

The final thing I will discuss here is again related to variable names. You may make the name of a variable absolutely anything. Here is an example

```
var ())=-\< = " hello "
print ())=-\<
```
RESULT:
```
hello
```
This code works because Ivory does not check individual characters, in fact ivory completely ignores any line that does not start with an instruction. This means that you can name your variables just about anything you want to.

## module documentation/example code
If you want documentation on how to use some of the modules for ivory, or if you want to see some projects built with ivory, look [here](https://ivory.itzscuzzles.repl.co/Documentation.html)

## installation and use
### installation
Despite a lot of programming languages having fairly complicated installations, ivory is quite simple. Just install this repository as a zip file or [click here](https://ivory.itzscuzzles.repl.co/ivory.html) for the website and click download, this gives you access to downloads of all of the previous versions of ivory. ***PLEASE NOTE*** it is required that you have python version 3 installed in order to use ivory, this allows for ivory to be downloadable on all operating systems with the only variation being python.
### use
To use ivory all you need to do is write code into a .iv file in the same directory as the ivory.py interpreter. Then you will run the interpreter and type the name of the file your code is in, do not include .iv at the end; for instance, if you are coding the the main.iv file, when you are prompted for the name you will type "main"

# more documentation
## sequences
when you are programming it is important to be able to execute a sequence or block of code under a certain circumstance, for instance maybe you use an if statement and you need to execute more than one line of code. In ivory instead of writing this under or inside of the if statement, you write it seperately in it's own sequence and then call the sequence in the if statement. Here is a basic example:
```
sequence normal_response {
print v" hello there %{ name } "
print " welcome to (app name) "
}

sequence admin_response {
print " hello admin user "
print " your list of commands is ... "
}

var name = input " enter your name here: "

if name == " admin " {{ sequence.use admin_response }}
else {{ sequence.use normal_response }}
```
RESULT: 
```
enter your name here:admin
hello admin user
your list of commands is ...
```
do note that it is impossible to write a program like this without first declaring a sequence and then using the sequence in your if statement. This is annoying and can occasionally get confusing but after you spend probably 10 minutes learning it you get used to it and can do it without thinking

## importing modules
in ivory, all you have to do to import a module is have the .iv file for it saved in the same folder as your ivory interpreter and file. An exmaple of a module is the "listsplus" module that comes with ivory to make lists much easier to use. Here is an example of how you could use it
```
import listsplus

var example = list [ " this is the first value " ] [ " this is the second value " ] 
print example
listappend example " this is the third value " 
print example
```
RESULT: 
```
['this is the first value', 'this is the second value']
['this is the first value', 'this is the second value', 'this is the third value']
```
You may have noticed that the way the list was coded and the way it printed are very different. This is because python is printing the lists and it prints them differently because it view lists in a different manner, **do not try to create a list the way that you do in most languages**, it will not work in ivory.

## math
Since ivory ignores all lines that do not have a direct instruction, you need to use a math function in order to do any math. There are two ways you can do this. If you do not need to input float numbers or numbers with a decimal then you can just use the math function. Here is an example

```
var number = math " 10 " + " 10 "
print number
```
RESULT:
```
20
```
Although this does work in a lot of cases, sometimes you need to include a decimal in your input, for this you will use math_float
```
var number = math_float " 4.3 " - " 1.2 "
print number
```
RESULT:
```
3.1
```
## the py function
Because ivory is a really basic programming language and doesn't really have a community, some things that would be easy in other programming languages isn't possible. Because of this I have added a py function, this uses python's "eval()" function to execute one python function, meaning you can essentially write python inside of ivory. Here is an example.
```
py i.time.sleep(1)
```
This will cause the program to wait 1 second before completing the next task, but in order to use this you need the python time module. Because of this issue, I added a blank file, Ivory_imports.py, any python module or library imported into this file will automatically be imported into the ivory interpreter as i, so the time module is typed "i.time"
## lists
although the listsplus module has already been mentioned, it is important to know how to use it because it is the primary and best method for list manipulation.
I will start with simply creating and using lists. To create a list you will need to clarify that what you are doing is creating a list. Here is how you can do that.
```
import listsplus

var mylist = list [ " value 1 " ] [ " value 2 " ] [ " value 3 " ]
print mylist
```
RESULT:
```
['value 1', 'value 2', 'value 3']
```
**Do not** forget when creating a list that you need to type "list" before typing out the actual list.
### appending to a list
Next is how to append to a list. To do this you will use the "listappend" function
```
import listsplus

var mylist = list [ " value 1 " ] [ " value 2 " ] [ " value 3 " ]
print mylist
listappend mylist " value 4 "
print mylist
```
RESULT:
```
['value 1', 'value 2', 'value 3']
['value 1', 'value 2', 'value 3', 'value 4']
```
### removing items from a list
To remove items from a list you will need to use the "listdelete" function. Here is how you would do that.
```
import listsplus

var mylist = list [ " value 1 " ] [ " value 2 " ] [ " value 3 " ]
print mylist
listdelete mylist " 1 "
print mylist
```
RESULT:
``` 
['value 1', 'value 2', 'value 3']
['value 1', 'value 3']
```
### list values
in order to get a specific value from a list using a number you will need to use the "listval" function. Here is an example:
```
import listsplus

var mylist = list [ " value 1 " ] [ " value 2 " ] [ " value 3 " ]
print mylist
var 2nd = listval mylist " 1 "
print 2nd
```
RESULT:
```
['value 1', 'value 2', 'value 3']
value 2
```
### indexing a list
If you are trying to index a list, you will use the "getval" function, here is an example of how to do this:
```
import listsplus

var mylist = list [ " value 1 " ] [ " value 2 " ] [ " value 3 " ]
print mylist
var val2 = getval mylist " value 2 "
print val2
```
RESULT:
```
['value 1', 'value 2', 'value 3']
1
```
### splitting a list
Sometimes it can be useful to split a string into a list of all the words in that string, to do this in ivory you will use the "listsplit" function
```
import listsplus

var string = " this is a string "
print string
var thelist = listsplit string
print thelist
```
RESULT:
```
this is a string
['this', 'is', 'a', 'string']
```
### joining a list
joining a list into a string is very useful in some cases, it is a majority of how ivory was built. To join a list you will use the "listjoin" function
```
import listsplus

var thelist = list [ " this " ] [ " is " ] [ " a " ] [ " list " ]
print thelist
var thestring = listjoin " , " thelist
print thestring
```
RESULT:
```
['this', 'is', 'a', 'list']
this,is,a,list
```
If you wanted to join a list and seperate it with spaces you would need to use the "listjoin_blank" function. Here is how you could do that:
```
import listsplus

var thelist = list [ " this " ] [ " is " ] [ " a " ] [ " list " ]
print thelist
var thestring = listjoin_blank thelist
print thestring
```
RESULT:
```
['this', 'is', 'a', 'list']
this is a list
```
### basic examples
listappend:
```
listappend list " this gets appended "
```
appends to a list titled "list"

listdelete:
```
listdelete list_variable " 2 "
```
deletes the third value from a list titled "list_variable"

listval:
```
listval cool_list " 1 "
```
returns the second value of a list named "cool_list"

getval:
```
getval aList " jerry "
```
returns the index value of "jerry" in list "aList"

listsplit:
```
listsplit theString
```
this will return a value of "theString" that has been split into a list.

listjoin:
```
listjoin " , " theList
```
this will return a value of "theList" that has been joined into a string, seperated by commas.

listjoin_blank:
```
listjoin_blank theList
```
this will return a version of "theList" that has been joined into a string and is seperated by spaces.