#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:29:37 2019

@author: Jonathan Zeas
Class: CS2300-002
Instructor: Prof Michael
    

"""



import matrixFunctions


def main():
    """
    This function imports the matrix functions, and uses them to perform actions on matricies provided as part of A1.
    Inputs : none
    Returns: none
    """
    #Open files
    outFileA = open("CS2300P1aZeas.outA.txt","w")
    outFileB = open("CS2300P1aZeas.outB.txt","w")
    outFileCalc = open("CS2300P1aZeas.calc.txt","w")
    outFileTrans = open("CS2300P1aZeas.outTrans.txt","w")
    
    #Read file, create matrixA, output to console, write to file.
    matrixA = matrixFunctions.readMatrix("Amatrix")
    for row in matrixA:
        print(row)
        outFileA.write(str(row)+'\n')
    
    print("\n")
    
    #Read file, create matrixB, output to console, write to file.
    matrixB = matrixFunctions.readMatrix("Bmatrix")
    for row in matrixB:
        print(row)
        outFileB.write(str(row)+'\n')
    
    print("\n")
    
    #Read file, create matrixSub, output to console, write to file.
    matrixSub = matrixFunctions.subtractMatrix(matrixA, matrixB, 5, 1)
    for row in matrixSub:
        print(row)
        outFileCalc.write(str(row  )+'\n')
    
    
    print("\n")
    
    #Read file, create matrixTranspose, output to console, write to file.
    matrixTranspose = matrixFunctions.transposeMatrix(matrixSub)
    for row in matrixTranspose:
        print(row)
        outFileTrans.write(str(row)+'\n')
    
    print("\n")
    
    #Close all files
    outFileA.close()
    outFileB.close()
    outFileCalc.close()
    outFileTrans.close()
    
    
if __name__ == "__main__": main()