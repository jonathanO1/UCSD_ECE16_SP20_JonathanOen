# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:47:34 2020

@author: ninja
"""
import numpy as np

def main():

    a = "Hello World!!!"
    b = "Hello"
    c = "World"
    d = "!!!"
    print(b+c+d)
    
    #question 1
    myPythonList = [0,10,4,12]
    test_array = np.array(myPythonList)
    test_array = test_array - 20
    print(test_array)
    print(test_array.shape)
    
    print("\n\n")
    
    #question 2
    arr = np.array([(0,10,4,12),
                    (1,20,3,41)])
    print(arr)
    print("\n\n")
    
    #question 3
    zeroes = np.zeros((10,20))
    print(zeroes)
    
    print("\n\n")
    #question 4
    rowArr = np.hstack((myPythonList, myPythonList))
    VArr = np.vstack((rowArr, rowArr, rowArr, rowArr))
    print(VArr)
    
    print("\n\n")
    #question 5
    arange_array1 = np.arange(-3, 16, 6)
    arange_array2 = np.arange(-7,-20, -2)
    print(arange_array1)
    print(arange_array2)
    
    print("\n\n")
    
    #question 6
    linspace_array = np.linspace(0, 100.0, num = 49)
    print(linspace_array)
    print("\n\n")
    
    #question 7
    #array is:
    #[(12,3,1,12),(0,0,1,2),(4,2,3,1)]
    
    #question 8
    e = np.array([(12,3,1,12),(0,0,1,2),(4,2,3,1)])
    print(e[0])
    print(e[1,0])
    print(e[:,1])
    print(e[2,:2])
    print(e[2,2:])
    print(e[:,2])
    print(e[1,3])
    
    s = np.array([1,2,3,4])
    stacked_arr = s
    for i in range (0,99):
        stacked_arr = np.vstack((stacked_arr, s))
    
    print(stacked_arr.size)
    
if __name__ == "__main__":
    main()


