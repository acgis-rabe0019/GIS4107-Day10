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
    test_exportToKml()
    #print test_exportToKmz()

def exportToKml(inFile, outKml):
    """converts the input data and exports it as a kml file"""
    out_file=open(outKml,'w')
    header=getKmlHeader()
    footer=getKmlFooter()
    out_file.write(header)
    for intext in open(inFile):
        data=[intext.strip('\n')]
        split_data=data[0].split(',')
        if split_data[1]=='Lat':
            pass
        else:
            placemark=getKmlPlacemark(split_data[2],split_data[1],split_data[3],split_data[4])
            out_file.writelines(placemark)
    out_file.write(footer)
    out_file.close()

def getKmlHeader():
    """gets the header from .txt file"""
    header_line1="<?xml version="+'"1.0"'+ ' encoding="UTF-8"?>'
    header_line2='<kml xmlns="http://www.opengis.net/kml/2.2">'
    header_line3='<Document>'
    return header_line1+'\n'+header_line2+'\n'+header_line3+'\n'

def getKmlPlacemark(longitude,latitude,depth,magnitude):
    """returns the placemark section of the KML file"""
    placemark_utils=["<Placemark>",'</Placemark>','<Point>','</Point>','\n','\t']

    name="<name>"+magnitude+"</name>"
    description= "<description>"+ "Mag="+ magnitude+ ', Depth='+depth+' km</description>'
    coordinates= '<coordinates>'+longitude+','+latitude+',0'+'</coordinates>'

    return '\t'+placemark_utils[0]+placemark_utils[4]+'\t'+'\t'+name+placemark_utils[4]+'\t'+'\t'+description+placemark_utils[4]+'\t'+'\t'+placemark_utils[2]+placemark_utils[4]+'\t'+'\t'+'\t'+coordinates+'\n'+'\t'+'\t'+placemark_utils[3]+'\n'+'\t'+placemark_utils[1]+placemark_utils[4]
def getKmlFooter():
    """returns the kml footer"""
    return "</Document>"+'\n'+'</kml>'+'\n'
#havent finished export to kmz yet
def exportToKmz(Kml):
    pass
def test_exportToKml():
    # Test case 1
    expected = "expected value"
    func = "func1"
    actual = exportToKml(os.path.join(_scriptFolder,'Quakes2000.txt'), os.path.join(_scriptFolder,'Quakes2000_kml.KML'))
    if expected == actual:
        print _fmtPassed.format("func1(params)")
    else:
        print _fmtFailed.format(func, expected, actual)

    # Test case 2 ...

def test_exportToKmz():
    exportToKmz(os.path.join(_scriptFolder,'Quakes2000.KML'))

if __name__ == '__main__':
    main()
