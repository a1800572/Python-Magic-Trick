import numpy as np
import random
import winsound
import pandas as pd
def main():
 while True:
    arr=np.random.choice(range(0, 100),21,replace=False).reshape(7,3)
    #error sekoituksessa
    #arr=pd.DataFrame(arr, columns=["col1","col2","col3"])
    print(arr)
    print("--------------")
    userin = str(input("which column has the number? "))
    print("--------------")
    if userin == "1":
        arr1=[arr[0,1], arr[1,1], arr[2,1], arr[3,1], arr[4,1], arr[5,1], arr[6,1],
              arr[0,0], arr[1,0], arr[2,0], arr[3,0], arr[4,0], arr[5,0], arr[6,0],
              arr[0,2], arr[1,2], arr[2,2], arr[3,2], arr[4,2], arr[5,2], arr[6,2]]
        arr2 = np.reshape(arr1, (7,3));
        print(arr2)
        print("--------------")
    
    if userin == "2":
        arr1=[arr[0,0], arr[1,0], arr[2,0], arr[3,0], arr[4,0], arr[5,0], arr[6,0],
              arr[0,1], arr[1,1], arr[2,1], arr[3,1], arr[4,1], arr[5,1], arr[6,1],
              arr[0,2], arr[1,2], arr[2,2], arr[3,2], arr[4,2], arr[5,2], arr[6,2]]
        arr2 = np.reshape(arr1, (7,3));
        print(arr2)
        print("--------------")

    if userin == "3":
        arr1=[arr[0,0], arr[1,0], arr[2,0], arr[3,0], arr[4,0], arr[5,0], arr[6,0],
              arr[0,2], arr[1,2], arr[2,2], arr[3,2], arr[4,2], arr[5,2], arr[6,2],
              arr[0,1], arr[1,1], arr[2,1], arr[3,1], arr[4,1], arr[5,1], arr[6,1]]
        arr2 = np.reshape(arr1, (7,3));
        print(arr2)
        print("--------------")
    userin1 = str(input("which column has the number? "))
    print("--------------")

#second
    if userin1 == "1":
        arr1=[arr2[0,1], arr2[1,1], arr2[2,1], arr2[3,1], arr2[4,1], arr2[5,1], arr2[6,1],
              arr2[0,0], arr2[1,0], arr2[2,0], arr2[3,0], arr2[4,0], arr2[5,0], arr2[6,0],
              arr2[0,2], arr2[1,2], arr2[2,2], arr2[3,2], arr2[4,2], arr2[5,2], arr2[6,2]]
        arr3 = np.reshape(arr1, (7,3));
        print(arr3)
        print("--------------")

    if userin1 == "2":
        arr1=[arr2[0,0], arr2[1,0], arr2[2,0], arr2[3,0], arr2[4,0], arr2[5,0], arr2[6,0],
              arr2[0,1], arr2[1,1], arr2[2,1], arr2[3,1], arr2[4,1], arr2[5,1], arr2[6,1],
              arr2[0,2], arr2[1,2], arr2[2,2], arr2[3,2], arr2[4,2], arr2[5,2], arr2[6,2]]
        arr3 = np.reshape(arr1, (7,3));
        print(arr3)
        print("--------------")

    if userin1 == "3":
        arr1=[arr2[0,0], arr2[1,0], arr2[2,0], arr2[3,0], arr2[4,0], arr2[5,0], arr2[6,0],
              arr2[0,2], arr2[1,2], arr2[2,2], arr2[3,2], arr2[4,2], arr2[5,2], arr2[6,2],
              arr2[0,1], arr2[1,1], arr2[2,1], arr2[3,1], arr2[4,1], arr2[5,1], arr2[6,1]]
        arr3 = np.reshape(arr1, (7,3));
        print(arr3)
        print("--------------")
    userin2 = str(input("which column has the number? "))
    print("--------------")

#third
    if userin2 == "1":
        print("The number you are thinking is " + str(arr3[3,0]))
        winsound.PlaySound("Audio/Laugh.wav", winsound.SND_ASYNC)
        
    if userin2 == "2":
        print("The number you are thinking is " + str(arr3[3,1]))
        winsound.PlaySound("Audio/Laugh.wav", winsound.SND_ASYNC)
        
    if userin2 == "3":
        print("The number you are thinking is " + str(arr3[3,2]))
        winsound.PlaySound("Audio/Laugh.wav", winsound.SND_ASYNC)

    choice = input("Would you like to try again? (Enter y for yes n for no) ")

    if choice == "y":
        continue
    elif choice == "n":
        break
main()
