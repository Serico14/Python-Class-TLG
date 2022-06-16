#!/usr/bin/env python3

#Defining function
#def function1(x, y= 'Awesome'):
#    print(f"{x} is {y}!")

#Re-calls function - can execute multiple times
#function1("Erico", "Awesome")

#Keyword document
#function1(y="awesome", x="Python")

#Positional Arguments
#function1("Python","Awesome")

#function1()

#def add(x,y):
 #   total= x + y
  #  return total

#def sub(x,y):
 #   total= x - y
 #   return total

#def main():
 #   add(10,5)
  #  sub(10,5)

def oddoreven(x):
    if x % 2 == 0:
        return True
    else:
        return Flase

def main():
    num= int(input("Choose a number:"))
    print(oddoreven(num))
            
main()
