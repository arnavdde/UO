# import my_lib

from my_lib import * # be careful of overpopulating namespace by importing everything

print(fact())


from x import y # -> if the y being imported has a print statement within the bock of code it is defined in, 
                #    the print statement will be run before importing to determine the value of y

'''if importing *, and importing multiple things with functions with the same name within them, you get problems'''

