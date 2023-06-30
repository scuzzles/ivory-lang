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
