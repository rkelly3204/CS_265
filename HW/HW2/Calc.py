#!/usr/bin/env python3
#Ryan Kelly
#11/12/2018
#Assignment 2
#Written in python 3.0

import sys
import operator


# This prgram takes input as an infix then returns it in postfix order as well as evaluates the 
# expression given

operators = ["+","-","*","/","%"] # List of operatores

precedence_Dict = { "+" : 1, #Sets dictionary and precedence for each operation
		   "-" : 1,
		   "*" : 2,
		   "/" : 2,
                   "%" : 2,
		   "(" : 0}

# I used the operator Class to set the "string operator" to a given operation
operations = {"+" : operator.add, 
	      "-" : operator.sub,
	      "*" : operator.mul,
	      "/" : operator.floordiv,
	      "%" : operator.mod,

# Takes the infix expression and pares the input
def infix2postfix(infix):
	infix += " )"
	stack = ["("]
	postfix = []

	#Loops through the operators 
	for item in infix.split():
		#If "(" add to the stack
		if item == "(":
			stack.append(item)
		#If ")" go through and pop the opperator and appends to the list
		elif item == ")":
			while stack[len(stack)-1] != "(":
				if operators.__contains__(stack[len(stack)-1]):
					postfix.append(stack.pop())
			stack.pop()

		elif operators.__contains__(item):
			while precedence_Dict[stack[len(stack)-1]] >= precedence_Dict[item]:
				postfix.append(stack.pop())
			stack.append(item)
		#Else operand then adds it to the postfix
		else:
			postfix.append(item)
	return postfix

#Evaluates the postfix expression then returns result of the calculation

def evalPostfix(postfix):
	
	stack = []

	#Loops through every item postfix list

	for tok in postfix:
		
		if operators.__contains__(tok):
			y = stack.pop()
			x = stack.pop()
			result = str(operations[tok](int(x),int(y)))
			stack.append(result)
		else:
			stack.append(tok)
	return stack[0]

#Prints the the results of the postfix operation

def print_Eval(postfix, result):
	for i in postfix:
		print(i, " ", end="")
	print("= ", result)

#Goes through the program each line at a time

def token_wise( fin ):
	for line in fin:
		yield line

if __name__ == "__main__":
#Checks if a file is an argurment if not use stdin
	if len(sys.argv) < 2:
		file = sys.stdin
	else:
		file = open(sys.argv[1])
	tokens = token_wise(file)

#Loops through the lines 
	for line in tokens:
		postfix = infix2postfix(str(line))
		result = evalPostfix(postfix)
		print_Eval(postfix, result)

