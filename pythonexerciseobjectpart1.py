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
from pprint import pprint

class Guitar:
    
    def __init__(self, serialNumber, Price, builder, model, gType, numStrings, backWood, topWood):
        self.serialnumber = serialNumber
        self.price = Price
        self.builder = builder
        self.model = model
        self.gtype = gType
        self.numstrings = numStrings
        self.backwood = backWood
        self.topwood = topWood
    
    #custom print function
    def __repr__(self):
        formatstr = 'serialnumber : {} \n price : {} \n builder : {} \n model : {} \n gType : {} \n numStrings : {} \n backwood : {} \n topwood : {}'
        return (formatstr.format(self.serialnumber, self.price, self.builder, self.model, self.gtype, self.numstrings, self.backwood, self.topwood))
        
    #create function to see if 1 guitar matches input guitar, based on limited input
    def match(self, otherGuitar):
        for k,v in otherGuitar.__dict__.items():
            if (v is not None) and (k not in ["serialnumber", "price"]):
                if self.__dict__[k] != v:
                    return False
        return True
        
class Inventory(list):    
    def __init__(self):
        #don't need to create a new list since its already inheriting from list
        return

    
    def __repr__(self):
        #convert each list value to a string before performing join
        #this is called list comprehension
        return '\n'.join(str(x) for x in self)

    def add_item(self,item):
        self.append(item)
    
    #search function
    #loop through all guitars compared to input guitar
    def search(self, cItem):
        for item in self:
            if item.match(cItem):
                print(item)
    
    #find specific guitar based on serial number
    def getGuitar(self,serialNo):
        for item in self:
            if item.serialnumber == serialNo:
                return item
            
        return

def initInventory():
    initinv = Inventory()
    
    initinv.add_item(Guitar("11277", 3999.95, "COLLINGS", "CJ", "ACOUSTIC", 6, "INDIAN_ROSEWOOD", "SITKA"))
    initinv.add_item(Guitar("V95693", 1499.95, "FENDER", "Stratocastor", "ELECTRIC", 6, "ALDER", "ALDER"))
    initinv.add_item(Guitar("V9512", 1549.95, "FENDER", "Stratocastor", "ELECTRIC", 6, "ALDER", "ALDER"))
    initinv.add_item(Guitar("122784", 5495.95, "MARTIN", "D-18", "ACOUSTIC", 6, "MAHOGANY", "ADIRONDACK"))
    initinv.add_item(Guitar("76531", 6295.95, "MARTIN", "OM-28", "ACOUSTIC", 6, "BRAZILIAN_ROSEWOOD", "ADIRONDACK"))
    initinv.add_item(Guitar("70108276", 2295.95, "GIBSON", "Les Paul", "ELECTRIC", 6, "MAHOGANY", "MAHOGANY"))
    initinv.add_item(Guitar("82765501", 1890.95, "GIBSON", "SG '61 Reissue", "ELECTRIC", 6, "MAHOGANY", "MAHOGANY"))
    initinv.add_item(Guitar("77023", 6275.95, "MARTIN", "D-28", "ACOUSTIC", 6, "BRAZILIAN_ROSEWOOD", "ADIRONDACK"))
    initinv.add_item(Guitar("1092", 12995.95, "OLSON", "SJ", "ACOUSTIC", 12, "INDIAN_ROSEWOOD", "CEDAR"))
    initinv.add_item(Guitar("566-62", 8999.95, "RYAN", "Cathedral", "ACOUSTIC", 12, "COCOBOLO", "CEDAR"))
    initinv.add_item(Guitar("629584", 2100.95, "PRS", "Dave Navarro Signature", "ELECTRIC", 6, "MAHOGANY", "MAPLE"))
    
    return initinv
   


def main():
    print("Welcome to Rick's Guitar Store Inventory System \n")
    
    #initialize inventory
    inv = initInventory()
    
    #customer's guitar
    custG = Guitar(serialNumber=None, Price=None, builder="FENDER", model=None, gType=None, numStrings=None, topWood=None, backWood=None)
    
    #search for guitars matching specs from above
    inv.search(custG)
    
    #search for guitar based on serial number
    print(inv.getGuitar("11277"))


if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        print("Exiting Program...")    
