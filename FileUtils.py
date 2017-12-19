#-------------------------------------------------------------------------------
# Name:        Module name
# Purpose:     Brief desciption of what module does
# Usage:       Module name and required/optional command-line parameters (if any)
# Author:      Your name(s)
#
# Created:     Date
#-------------------------------------------------------------------------------
import os
import sys

_fmtPassed = "Passed: {}"
_fmtFailed = "Failed: {}\n  Expect: {}\n  Actual: {}"
_scriptFolder = os.path.dirname(os.path.abspath(__file__))

def main():
    #test_writeToFile()
    #test_getFileContent()
    #test_appendToFile()
    test_getFileContent()
    pass
def writeToFile(fileName, content):
    """writes the content parameter to the file specified by the fileName Parameter"""
    open_file=open(fileName,'w')
    open_file.write(content)
    open_file.close()

def getFileContent(fileName):
    """returns the content of the file as a string"""
    if os.path.isfile(fileName)== True:
        open_file=open(fileName,'r')
        file_script=open_file.readline()
        script=''
        while file_script!='':
            script+=file_script.rstrip('\n')
            file_script=open_file.readline()
        open_file.close()
        return script
    if os.path.isfile(fileName)==False:
        try:
            open(fileName,'r')
        except IOError:
            return "File does not exist or was not found."
def appendToFile(fileName, content):
    """appends content to the specified file (fileName)"""
    path_t_f=os.path.exists(fileName)
    if path_t_f==True:
        open_file= open(fileName,'a')
        append_open= open_file.write(content)
        open_file.close()
    if path_t_f==False:
        return fileName+" does not exist."
#example
def test_func1():
    # Test case 1
    expected = "expected value"
    func = "func1"
    actual = func1(1)
    if expected == actual:
        print _fmtPassed.format("func1(params)")
    else:
        print _fmtFailed.format(func, expected, actual)
#test functions
def test_writeToFile():
    # Test case 1
    expected = "test of the write function"
    func = writeToFile(os.path.join(_scriptFolder,"fileDemo.txt"),"test of the write function")
    actual = open("fileDemo.txt").read()
    if expected == actual:
        print _fmtPassed.format("func1(params)")
    else:
        print _fmtFailed.format(func, expected, actual)

def test_getFileContent():
    # Test case 1: file exists in the folder
    expected = "test of the write function"
    func = getFileContent(os.path.join(_scriptFolder,"fileDemo.txt"))
    actual = func
    if expected == actual:
        print _fmtPassed.format('getFileContent(os.path.join(_scriptFolder,"fileDemo.txt"))')
    else:
        print _fmtFailed.format(func, expected, actual)
    #test case 2: file does not exist in the folder
    expected_2= "expected"
    func_2= getFileContent(os.path.join(_scriptFolder,'TestNonExistingFile.txt'))
    actual_2=func_2
    if expected_2 == actual_2:
        print _fmtPassed.format("func1(params)")
    else:
        print _fmtFailed.format(func_2, expected_2, actual_2)

def test_appendToFile():
    # Test case 1
    expected = "test of the write function and the append function."
    func = appendToFile(os.path.join(_scriptFolder,"fileDemo.txt")," and the append function.")
    actual = open("fileDemo.txt",'r').read()
    if expected == actual:
        print _fmtPassed.format("func1(params)")
    else:
        print _fmtFailed.format(func, expected, actual)

if __name__ == '__main__':
    main()
