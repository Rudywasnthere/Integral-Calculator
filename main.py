import time, sys

print("Hello, this is a definite integral calculator")
time.sleep(2.2)
print("First, you need to know the syntax of writing")
time.sleep(2)
print("So, go to this link if you need to know:\nhttps://www.tutorialspoint.com/python/python_basic_operators.htm")
function= input("First, what is your function:\n")
print("Second, on what interval are you integrating?")
lower_limit= int(input("Left Limit:"))
upper_limit= int(input("Right Limit:"))
increments= input("And how small of increments are you measuring by (delta x):")
print("Finally, you can find the area in the difference of the antiderivative")
time.sleep(3)
check1= input("Do you you know what the antiderivative? (yes or no)\n")
if check1== 'yes':
  antiderivative= input("What is it, this will make calculating easier:\n")
  lower= antiderivative.replace("x",lower_limit)
  upper= antiderivative.replace("x",upper_limit)
  integral= int(upper) - int(lower)
  print("Here's your integral, thank you")
