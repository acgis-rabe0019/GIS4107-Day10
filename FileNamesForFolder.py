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
    input_file=sys.argv
    if len(input_file)==3:
        test_dumpfile()
    if len(input_file)!=3:
        print 'FileNamesForFolder, folder_to_scan, output_file'
        sys.exit()

def dumpFileList(folder,dumpfile):
    """ gets a listing of absolute file names in folder and writes them one per
    line into the dummpfile"""
    if os.path.exists==True:
        folder_list=os.listdir(folder)
        open_dumpsite= open(dumpFile,'w')
        for files in folder_list:
            open_dumpsite.write(files)
            open_dumpsite.write('\n')
        open_dumpsite.close()
    if os.path.exists==False:
        "File does not exist."

def test_dumpfile():
    # Test case 1
    expected = "expected value"
    func = "func1"
    actual = dumpFileList(sys.argv[1],sys.argv[2])
    if expected == actual:
        print _fmtPassed.format("func1(params)")
    else:
       print _fmtFailed.format(func, expected, actual)

    # Test case 2 ...
##    expected = "expected value"
##    func = "func1"
##    actual = dumpFileList(sys.argv[0], sys.argv[1])
##    if expected == actual:
##        print _fmtPassed.format("func1(params)")
##    else:
##        print _fmtFailed.format(func, expected, actual)


if __name__ == '__main__':
    main()
