# A Short Summary
Ivory is a unique programming language made in part with the intent of making programming less complicated, some things are very odd because ivory is not made traditionally but if you take the time to learn it, so long as you have an understanding of python you should find that almost anything is possible with the combination of the two

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

```sequence say_hi {
print " hello there "
print " how are you? "
}
sequence.use say_hi
```
RESULT: 
```hello there
how are you?
```

## Variables
When you want to make a variable in ivory, you will do so with the "var" keyword. Here is an example

``` var truth = " Tom is a genius " ```
This seems pretty simple but leads into something really cool about ivory. In ivory there are no types at all 
unless you are writting direct python code inside of ivory, so even if you tried to add a string and an integer
ivory would just assume that the string was meant to be an integer and if for some reason it didn't work then it would raise an error




## Functions

How to use "..." parameters/infinite parameters with functions:

```function testing [ ... ] for x in ... {{ print x }} ;```

NOTE: the use of "..." is intentional, ... allows ivory to know that you are allowing for a variable amount of parameters,
each entered parameter will be added to the list under the variable name "..." and you will be able to iterate through
each item in the list









## Modules 

### Threading Module
Here is an example of how to use the threading module

```import threading
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
