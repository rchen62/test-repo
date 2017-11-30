'''
Rick's Guitar Store:
 
Just a few months ago, Rick decided to throw out his paper-based system for keeping track of guitars, and
start using a computer-based system to store his inventory.
 
You have to build a new inventory management app. This app should also have search tool to helps match up
a customer to their dream instrument.
  
The attributes of a Guitar, Inventory  (from Rick's notes)
 
Inventory
    list of guitars
    getGuitar(serialNo)

    Search(customerGuitar)
 
Guitar
    serialNumber
    price
    builder
    model
    gType
    backWood
    topWood
    numStrings
Search() should return a list of guitars (lets say top 5) or can have an argument that allows users to
specify top 'n' guitars matched.
gType is one of [ACOUSTIC, ELECTRIC]
builder is one of [FENDER, MARTIN, GIBSON, COLLINGS, OLSON, RYAN, PRS, ANY]
wood is one of [INDIAN_ROSEWOOD, BRAZILLIAN_ROSEWOOD, MAHOGANY, MAPLE, COCOBOLO, CEDAR, ADIRONDACK, ALDER,
 SITKA]
model is a string
price is a float
numStrings is an integer
serialNumber is a string
if adding x instruments, dont want to have to change existing instrument class, or inventory class
'''

import sys
import pprint

class Instrument(dict):
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self[key]=value

    def match(self, otherInstrument):
        for k, v in otherInstrument.items():
            if (v is not None):
                if self[k] != v:
                    return False
        return True


class Inventory(list):
    def __init__(self):
        # don't need to create a new list since its already inheriting from list
        return

    def __repr__(self):
        # convert each list value to a string before performing join
        # this is called list comprehension
        return '\n'.join(str(x) for x in self)

    def add_item(self, item):
        self.append(item)

    # search function
    # loop through all guitars compared to input guitar
    def search(self, cItem):
        for item in self:
            if item.match(cItem):
                pprint.pprint(item)

    def getInstrument(self, iType, serialNo):
        for item in self:
            if item['instrumentType'] == iType and item['serialNumber'] == serialNo:
                return item


def initInventory():
    initinv = Inventory()

    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="11277", price=3999.95, numStrings=6, builder="COLLINGS", model="CJ", gType="ACOUSTIC", topWood="INDIAN_ROSEWOOD", backWood="SITKA"))
    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="V95693", price=1499.95, numStrings=6, builder="FENDER", model="Stratocastor", gType="ELECTRIC", topWood="ALDER", backWood="ALDER"))
    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="V9512", price=1549.95, numStrings=6, builder="FENDER", model="Stratocastor", gType="ELECTRIC", topWood="ALDER", backWood="ALDER"))
    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="122784", price=5495.95, numStrings=6, builder="MARTIN", model="D-18", gType="ACOUSTIC", topWood="MAHOGANY", backWood="ADIRONDACK"))
    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="76531", price=6295.95, numStrings=6, builder="MARTIN", model="OM-28", gType="ACOUSTIC", topWood="BRAZILIAN_ROSEWOOD", backWood="ADIRONDACK"))
    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="70108276", price=2295.95, numStrings=6, builder="GIBSON", model="Les Paul", gType="ELECTRIC", topWood="MAHOGANY", backWood="MAHOGANY"))
    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="82765501", price=1890.95, numStrings=6, builder="GIBSON", model="SG '61 Reissue", gType="ELECTRIC", topWood="MAHOGANY", backWood="MAHOGANY"))
    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="77023", price=6275.95, numStrings=6, builder="MARTIN", model="D-28", gType="ACOUSTIC", topWood="BRAZILIAN_ROSEWOOD", backWood="ADIRONDACK"))
    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="1092", price=12995.95, numStrings=12, builder="OLSON", model="SJ", gType="ACOUSTIC", topWood="INDIAN_ROSEWOOD", backWood="CEDAR"))
    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="566-62", price=8999.95, numStrings=12, builder="RYAN", model="Cathedral", gType="ACOUSTIC", topWood="COCOBOLO", backWood="CEDAR"))
    initinv.add_item(Instrument(instrumentType="Guitar", serialNumber="629584", price=2100.95, numStrings=6, builder="PRS", model="Dave Navarro Signature", gType="ELECTRIC", topWood="MAHOGANY", backWood="MAPLE"))
    initinv.add_item(Instrument(instrumentType="Mandolin", serialNumber="11277", price=5495.99, builder="GIBSON", model="F-5G", gType="ACOUSTIC", topWood="MAPLE", backWood="MAPLE"))

    return initinv

def main():
    print("Welcome to Rick's Guitar Store Inventory System \n")
    
    #initialize inventory
    inv = initInventory()
    
    #customer's guitar
    custI = Instrument(builder="GIBSON")
    
    #search for guitars matching specs from above
    inv.search(custI)
    
    #search for guitar based on serial number
    print(inv.getInstrument("Mandolin","11277"))


if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        print("Exiting Program...")    

