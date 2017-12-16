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
#need to do something additional with argv confusing instructions
def main():
    test_dumpfile()

def dumpFileList(folder,dumpFile):
    """ gets a listing of absolute file names in folder and writes them one per
    line into the dummpfile"""
    folder_list=os.listdir(folder)
    open_dumpsite= open(dumpFile,'w')
    for files in folder_list:
        open_dumpsite.write(files)
        open_dumpsite.write('\n')
    open_dumpsite.close()


def test_dumpfile():
    # Test case 1
    expected = "expected value"
    func = "func1"
    actual = dumpFileList("C:\Users\chris\Desktop",os.path.join(_scriptFolder,"dump_file_test.txt"))
    if expected == actual:
        print _fmtPassed.format("func1(params)")
    else:
        print _fmtFailed.format(func, expected, actual)

    # Test case 2 ...


if __name__ == '__main__':
    main()
