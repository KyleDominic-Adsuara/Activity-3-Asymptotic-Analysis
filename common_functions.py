import time
import matplotlib.pyplot as plt 
import numpy as np 
import math

graphLimit = []
result1 = []
result2 = []
result3 = []
result4 = []
result5 = []
result6 = []

def logarithmic(n):
	log = math.log(n)
	return log

def linearithmic(n):
	log = math.log(n)
	lin = n * log
	return lin

def linear(n):
	return n

def quadratic(n):
	quad = math.pow(n,2)
	return quad

def polynomial(n):
	poly = math.pow(n,3)
	return poly

def exponential(n):
	expo = math.pow(2,n)
	return expo

def test_run():
	n = int(input("pls enter number: "))
	graphLimit.append(n)

	start1 = time.time()
	print("logarithmic result: ", logarithmic(n),"\n")
	end1 = time.time()
	result1.append(end1-start1)

	start2 = time.time()
	print("linearithmic result: ",linearithmic(n),"\n")
	end2 = time.time()
	result2.append(end2-start2)

	start3 = time.time()
	print("linear result: ",linear(n),"\n")
	end3 = time.time()
	result3.append(end3-start3)

	start4 = time.time()
	print("quadratic result: ",quadratic(n),"\n")
	end4 = time.time()
	result4.append(end4-start4)

	start5 = time.time()
	print("polynomial result: ",polynomial(n),"\n")
	end5 = time.time()
	result5.append(end5-start5)

	start6 = time.time()
	print("exponential result: ",exponential(n),"\n")
	end6 = time.time()
	result6.append(end6-start6)

	Q = input("would you like to run another test? (y/n): ")
	if Q == "y":
		test_run()
	else:
		print("results of your tests are in order: \n")

test_run()
print("please wait for the graph........")

#fig, ax = plt.subplots()
plt.plot(graphLimit, result1, label='logarithmic', linewidth=1,color='red')
plt.plot(graphLimit, result2, label='linearithmic', linewidth=1,color='blue')
plt.plot(graphLimit, result3, label='linear', linewidth=1,color='yellow')
plt.plot(graphLimit, result4, label='quadratic', linewidth=1,color='green')
plt.plot(graphLimit, result5, label='polynomial', linewidth=1,color='violet')
plt.plot(graphLimit, result6, label='exponential', linewidth=1,color='orange')
plt.legend()
plt.xlabel('Graph limit')
plt.ylabel('Runtime')
plt.title('Common function runtime!')

plt.show()