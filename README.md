# A Short Summary
Ivory is a unique programming language made in part with the intent of making programming less complicated, some things are very odd because ivory is not made traditionally but if you take the time to learn it, so long as you have an understanding of python you should find that almost anything is possible with the combination of the two

## Using Ivory
One of the ways that you can run your Ivory program is to use the run command. Here is an example:
```
py ivory.py run main.iv
```
This will run a file named "main.iv" but if you wanted to run it in linux it would look like this:
```
python3 ivory.py run main.iv
```

## Using a Function
in ivory, there is no need for parenthesis; for example, here is how you would run hello world

```
print " hello world "
```
all functions are used with quotes, please note the spaces between the quotation marks and the words, this is 
because the ivory interpreter seperates each instruction by whitespace



## Sequences
in most programming languages you just write your sequence of code under an if statement or loop or wherever you need it, 
in ivory you will need to declare your sequence beforehand and then use it when needed. Here is an example of how you could do this:

```
sequence say_hi {
print " hello there "
print " how are you? "
}
sequence.use say_hi
```
RESULT: 
```
hello there
how are you?
```

## Variables
When you want to make a variable in ivory, you will do so with the "var" keyword. Here is an example

``` 
var truth = " Tom is a genius " 
```
This seems pretty simple but leads into something really cool about ivory. In ivory there are no types at all 
unless you are writting direct python code inside of ivory, so even if you tried to add a string and an integer
ivory would just assume that the string was meant to be an integer and if for some reason it didn't work then it would raise an error


## V-string
When you're programming, you need a way to combine strings and variables. In ivory the method of doing so is to use something called a v-string, similar to an f-string in python. Here's how a v-string might be used:

```
var name = input " please enter your name here: "
print v" Hello there %{ name } "
```

RESULT:
```
please enter your name here:Bob
Hello there Bob
```
although v-strings can be used with the print function, this is actually the only time that will work. but if you want to use a v-string with a different function you can still do so by creating a variable with a v-string and then passing the variable as a parameter of the function. Here's what that might look like:
```
var name = " Tom "
var combined_string = v" %{ name } is a genius "
var result = split combined_string
print result 
```
RESULT:
```
['Tom', 'is', 'a', 'genius']
```
(the split function splits a string into a list of all the words seperated by whitespace in the string)

Here is how you wouldn't want to do that:

```
var name = " Tom "
var result = split v" %{ name } is a genius "
print result
```
RESULT:
```
ERROR: UNDEFINED VARIABLE | LINE: 2 | Could not find "v"" 
```
This happens because Ivory does not accept v-strings inside of normal functions and so it tries to find a variable named v" since that is the next "word" in the line.


## math
When you're trying to do math, you will have to use the math function. Here's an example:
```
var result = math " 1 " + " 2 "
print result
```
RESULT:
```
3
```
If you've ever written in an other programming language at all you probably have one question. "Why are the strings added together?"
This is because in Ivory there are really no types, strings and numbers are not different from each other, the only difference is between float numbers and int numbers.
When you use the math function ivory will just try to add the two strings as integers and if it doesn't work it will raise an error. Here are some more math examples:
**Example 1:**
```
var result = math " 124 " - " 43 "
print result
```
RESULT:
```
81
```
**Example 2:**
```
var result = math " 10 " * " 4 "
print result
```
RESULT:
```
40
```
**Example 3:**
```
var result = math_float " 10 " * " 3.4 "
print result
```
RESULT:
```
34.0
```
The point of the "math_float" function is to execute math that requires float numbers as input.

The math function works with the following operations (+, -, *, /, %, **, //)



## Functions
If you are trying to create a function, you can do so with the function keyword. Here is how you would do that:
```
function cool_func [ parameter ] var result = v" the parameter is: %{ parameter } " ; return result ;
var test = cool_func " interesting parameter "
print test
```
RESULT:
```
the parameter is: interesting parameter
```
This might look weird and that's because Ivory is just weird. If you write a function all of the code for the function must be written in one line which is why everything is all written with the function and lines are seperated by semi-colons.

If you want to write your code one on one line you can do so by making your only line in the function a sequence.use and using a sequence. The only problem with this solution is that you will still have write your line for returning on the next line. Here is a simple way to do that:

```
sequence cool_math_thing {
var num2 = math number * " 10 "
var result = math number + num2
}
function cool_math_thing [ number ] sequence.use cool_math_thing ; return result ;
var end_result = cool_math_thing " 5 "
print end_result
```
RESULT:
```
55
```
This works because all variables created in ivory are completely global and don't have any scope.


How to use "..." parameters/infinite parameters with functions:

```
function testing [ ... ] for x in ... {{ print x }} ;
```

NOTE: the use of "..." is intentional, ... allows ivory to know that you are allowing for a variable amount of parameters,
each entered parameter will be added to the list under the variable name "..." and you will be able to iterate through
each item in the list









## Modules 

### Threading Module
Here is an example of how to use the threading module

```
import threading
import time
var x = " 0 "
sequence inthread {
var x = math x + " 1 "
print x
time_sleep " 1 "
}
sequence thread {
while running == " true " {{ sequence.use inthread }}
}
var running = " true "
run_thread " thread "
var example = input " type q to quit "
if example == " q " {{ var running = " false " }}
```
