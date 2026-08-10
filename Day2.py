#Variables and data types
# swapping of numbers
a=5
b=6
a,b=b,a
print("A is:",a)
print("B is:",b)

# control flow
a= int(input("Enter a number:"))
if a%2==0:
    print("The digit is even:",a)
else:
    print("the digit is odd:",a)
    
# Loops
n=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n} x {i}={n*i}")
    
# List and Dictonaries
sentence = "data science with python is fun and python is powerful"
words = sentence.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

# Functions
def is_palindrome(s):
    return s ==s[::-1]
print(is_palindrome("madam"))
print(is_palindrome("python"))

# Data Science Starter
import pandas as pd
df=pd.read_csv("data.csv")
print(df.head())