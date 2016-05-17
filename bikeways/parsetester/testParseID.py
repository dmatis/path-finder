from xml.etree.ElementTree import ElementTree
import re

tree0 = ElementTree()
KML_0 = tree0.parse('test0.kml')

TOTAL_TESTS = 4

passedTests = 0
coords = []

class CoordinateWithID:
    def __init__(self):
        self.key = None
        self.latitude = None
        self.longitude = None

def parser(kml):

    data = kml
    placemark = data.findall('.//{http://www.opengis.net/kml/2.2}Placemark')

    i = 1
    for multiGeom in placemark:
        placemarkid = i
        for item in multiGeom:
            for lineString in item:
                for coord in lineString:
                    key = placemarkid
                    splitcoords = coord.text
                    splitbycomma = re.split(',0 |,', splitcoords)
                    for index in range(len(splitbycomma)-1):
                        if index % 2 == 0:
                            lng = splitbycomma[index]
                            lat = splitbycomma[index+1]
                            c = CoordinateWithID()
                            c.key = key
                            c.latitude = lat
                            c.longitude = lng
                            coords.append(c)

        i += 1

def increment():
    global passedTests
    passedTests = passedTests+1

def printTestResult(status, testID):
    if status == 1:
        toPrint = "Test " + str(testID) + " passed"
        print(toPrint)
        increment()
    if status == 0:
        toPrint = "Test " + str(testID) + " failed"
        print(toPrint)

def testAmountOfCoords():
    testID = 1
    status = 0
    expectedAnswer = 3
    if len(coords) == expectedAnswer:
        status = 1
    printTestResult(status, testID)

def testKey():
    testID = 2
    expectedKey = 1
    for coord in coords:
        status = 0
        if coord.key != expectedKey:
            printTestResult(status, testID)
            return
    status = 1
    printTestResult(status, testID)

def testLat():
    testID = 3
    status = 0
    expectedLats = set(['49.26850170078', '49.2689004289734', '49.2691038566599'])
    lats = set()
    for coord in coords:
        lats.add(coord.latitude)
    if expectedLats == lats:
        status = 1
        printTestResult(status, testID)
        return
    print(lats)
    print(expectedLats)
    printTestResult(status, testID)

def testLng():
    testID = 4
    status = 0
    expectedLngs = set(['-123.204042015075', '-123.205737081717', '-123.215024245423'])
    lngs = set()
    for coord in coords:
        lngs.add(coord.longitude)
    if expectedLngs == lngs:
        status = 1
        printTestResult(status, testID)
        return
    printTestResult(status, testID)

parser(KML_0)
testAmountOfCoords()
testKey()
testLat()
testLng()

print(str(passedTests) + " of " + str(TOTAL_TESTS) + " tests passed")