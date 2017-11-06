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

class Instrument:
    
    def __init__(self, builder, model, gType, backWood, topWood):
        self.builder = builder
        self.model = model
        self.gtype = gType
        self.backwood = backWood
        self.topwood = topWood

class Guitar(Instrument):
    
    category = "Guitar"
    
    def __init__(self, serialNumber, Price, numStrings, builder, model, gType, backWood, topWood):
        
        Instrument.__init__(self, builder, model, gType, backWood, topWood)
        
        self.serialnumber = serialNumber
        self.price = Price
        self.numstrings = numStrings
        
    #custom print function
    def __repr__(self):
        formatstr = 'category: {} \n serialnumber : {} \n price : {} \n numStrings : {} \n builder : {} \n model : {} \n gType : {}  \n backwood : {} \n topwood : {}'
        return (formatstr.format(self.category, self.serialnumber, self.price, self.numstrings, self.builder, self.model, self.gtype,  self.backwood, self.topwood))
        
    #create function to see if 1 guitar matches input guitar
    def match(self, otherInstrument):
        for k,v in otherInstrument.__dict__.items():
            if (v is not None) and (k not in ["serialnumber", "price"]):
                if self.__dict__[k] != v:
                    return False
        return True

class Mandolin(Instrument):
    
    category = "Mandolin"
    
    def __init__(self, serialNumber, Price, builder, model, gType, backWood, topWood):
        
        Instrument.__init__(self, builder, model, gType, backWood, topWood)
        
        self.serialnumber = serialNumber
        self.price = Price
        
    #custom print function
    def __repr__(self):
        formatstr = 'category: {} \n serialnumber : {} \n price : {} \n builder : {} \n model : {} \n gType : {}  \n backwood : {} \n topwood : {}'
        return (formatstr.format(self.category, self.serialnumber, self.price, self.builder, self.model, self.gtype,  self.backwood, self.topwood))
        
    #create function to see if 1 guitar matches input guitar
    def match(self, otherInstrument):
        for k,v in otherInstrument.__dict__.items():
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
    
    def getInstrument(self, category, serialNo):
        for item in self:
            if item.serialnumber == serialNo and item.category == category:
                print(item)
            



def initInventory():
    initinv = Inventory()
    
    #change order of input so that guitar specific ones are at the front
    initinv.add_item(Guitar("11277", 3999.95, 6, "COLLINGS", "CJ", "ACOUSTIC", "INDIAN_ROSEWOOD", "SITKA"))
    initinv.add_item(Guitar("V95693", 1499.95, 6, "FENDER", "Stratocastor", "ELECTRIC", "ALDER", "ALDER"))
    initinv.add_item(Guitar("V9512", 1549.95, 6, "FENDER", "Stratocastor", "ELECTRIC", "ALDER", "ALDER"))
    initinv.add_item(Guitar("122784", 5495.95, 6, "MARTIN", "D-18", "ACOUSTIC", "MAHOGANY", "ADIRONDACK"))
    initinv.add_item(Guitar("76531", 6295.95, 6, "MARTIN", "OM-28", "ACOUSTIC", "BRAZILIAN_ROSEWOOD", "ADIRONDACK"))
    initinv.add_item(Guitar("70108276", 2295.95, 6, "GIBSON", "Les Paul", "ELECTRIC", "MAHOGANY", "MAHOGANY"))
    initinv.add_item(Guitar("82765501", 1890.95, 6, "GIBSON", "SG '61 Reissue", "ELECTRIC", "MAHOGANY", "MAHOGANY"))
    initinv.add_item(Guitar("77023", 6275.95, 6, "MARTIN", "D-28", "ACOUSTIC", "BRAZILIAN_ROSEWOOD", "ADIRONDACK"))
    initinv.add_item(Guitar("1092", 12995.95, 12, "OLSON", "SJ", "ACOUSTIC", "INDIAN_ROSEWOOD", "CEDAR"))
    initinv.add_item(Guitar("566-62", 8999.95, 12, "RYAN", "Cathedral", "ACOUSTIC", "COCOBOLO", "CEDAR"))
    initinv.add_item(Guitar("629584", 2100.95, 6, "PRS", "Dave Navarro Signature", "ELECTRIC", "MAHOGANY", "MAPLE"))

    initinv.add_item(Mandolin("11277", 5495.99, "GIBSON", "F-5G", "ACOUSTIC", "MAPLE", "MAPLE"))
    
    return initinv


inv = initInventory()
custG = Guitar(serialNumber=None, Price=None, builder="GIBSON", model=None, gType=None, numStrings=None, topWood=None, backWood=None)
custI = Instrument(builder="GIBSON", model=None, gType=None, topWood=None, backWood=None)
#print(inv)
inv.search(custI)
#inv.search()
#inv.getInstrument("Guitar","11277")

 
 
# item = []
# guitar1 = Guitar("11277", 3999.95, 6, "COLLINGS", "CJ", "ACOUSTIC", "INDIAN_ROSEWOOD", "SITKA")
# #guitar2 = Guitar("12345", 4000.95, "COLLINGS", "CJ", "ACOUSTIC", 6, "INDIAN_ROSEWOOD", "SITKA")
# #guitar3 = Guitar("V95693", 1499.95, None, "Stratocastor", "ELECTRIC", 6, "ALDER", "ALDER")
# #mando1 = Mandolin("9019920", 5495.99, "GIBSON", "F-5G", "ACOUSTIC", "MAPLE", "MAPLE")
# item.append(guitar1)
# #item.append(guitar2)
# #item.append(mando1)
# #print(guitar1)
# print(item)
#     
# #print(guitar1.match(guitar3))
# #print(guitar1.match(guitar2))






    