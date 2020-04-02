# UCSD_ECE16_SP20
The repository belongs to Jonathan Oen for UCSD ECE16 for Spring 2020.
Let's make something really cool!!
 
 Markdown Report
 Challenge 1 questions
 Q. Show the code: Starting with a = “Hello World!!!”, come up with a code snippet that will give us b = “Hello” and c = “World” and d = “!!!” . Also, in code, check if “ello” is in a. 
 code:
  a = "Hello World!!!"
    b = "Hello"
    c = "World"
    d = "!!!"
    print(b+c+d)

Q. In the following code, what is the output of the print statement? Why doesn’t original_list = ['hi','how','are','you']?
The output is : ['hi',1,2,'you']
The reason it prints this and doesn't replace the 1 and the 2 with
'how' and 'are' is because the print statement is set to print the 
original array which remains unchanged

Challenge 2 questions
Q. Show the code: Make a Numpy Array called test_array  from a list = [0,10,4,12]. Subtract 20 from the test_array, what do you get? What is the shape of the test_array
Result: [-20 -10 -16  -8]
Shape: (4,)

Q. Show the code: Make a 2D array of test_2D_array from [0,10,4,12]
                                                        [1,20,3,41]
code:
arr = np.array([(0,10,4,12),
                    (1,20,3,41)])

Q. Make a 2D array of zeros with shape of 10x20 and then print it out
zeroes = np.zeros((10,20))
print(zeroes)

Q. Show the code: Out of the test_array, create the following using hstack and vstack: 
rowArr = np.hstack((myPythonList, myPythonList))
VArr = np.vstack((rowArr, rowArr, rowArr, rowArr))
print(VArr)

Q. Show the code: Using arange, make an array called arange_array1 to equal [-3, 3,9,15] and arange_array2 to equal [ -7,  -9, -11, -13, -15, -17, -19]
arange_array1 = np.arange(-3, 16, 6)
arange_array2 = np.arange(-7,-20, -2)
print(arange_array1)
print(arange_array2)

Q. Make an array called linspace_array using linspace that goes from 0 to 100 with 49 steps. 
Q. How do linspace and arange differ? When might you use one over the other?
linspace_array = np.linspace(0, 100.0, num = 49)
They differ because for arange, you determine the step size compared to linspace in which you determine the number of steps. You would use linspace for when you have to fill data with a certain number of steps and arange when you want to set the size of the step

Q. What is an array of size 3x4 that would produce the following results. Show your work on how you deduced your answer on paper or some kind of graphics:
[(12,3,1,12),(0,0,1,2),(4,2,3,1)]

Q. Using fromstring, vstack, and a for loop, create an array of 100x4 from s: [[1,2,3,4],[1,2,3,4],[1,2,3,4]…..[1,2,3,4]]. 
s = np.array([1,2,3,4])
stacked_arr = s
for i in range (0,99):
    stacked_arr = np.vstack((stacked_arr, s))
    
print(stacked_arr.size)
# ece16sp2020-jonathanO1
