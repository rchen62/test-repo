'''
Create a most recently used class similar to the most recently used option
on many desktop applications like Microsoft Word/Excel or Spyder

The following pytest command should work fine

pytest python\most_recently_used.py
'''

# testing


class MostRecentlyUsed:

    # incorrect here. will be shared by all functions.
    # mru = []

    def __init__(self, count):
        self.maxSize = count
        # correct location. creates new empty list for each instance
        self.mru = []

    def get(self):
        return self.mru

    def add(self, key):
        if key in self.mru:
            self.mru.remove(key)
            # add to beginning of list, as opposed to .append to end of list
            self.mru.insert(0, key)
        else:
            # add to beginning of list, as opposed to .append to end of list
            self.mru.insert(0, key)
        if len(self.mru) > self.maxSize:
            self.mru.pop()


class MostRecentlyUsed2(list):
    def __init__(self, count):
        self.maxSize = count
        list.__init__(self)

    def get(self):
        return self

    def add(self, key):
        # TODO: write the add function
        if key in self:
            self.remove(key)
            # add to beginning of list, as opposed to .append to end of list
            self.insert(0, key)
        else:
            # add to beginning of list, as opposed to .append to end of list
            self.insert(0, key)
        if len(self) > self.maxSize:
            self.pop()
        
        # TODO: is this better than the class that contains a list


def mru_example(MRUClass):
    
    
    mru = MRUClass(4)   # returns at most 4 items
    print (mru.get())
    mru.add('A')
    print (mru.get())
    
    mru.add('B')
    print (mru.get())
    
    mru.add('C')
    print (mru.get())

    mru.add('A')
    print (mru.get())
    
    mru.add('A')
    print (mru.get())
    
    mru.add('D')
    print (mru.get())
    
    mru.add('E')
    print (mru.get())

    mru.add('D')
    print (mru.get())
    
    
    '''
    mru = MRUClass(4)  # returns at most 4 items
    assert mru.get() == []

    mru.add('A')
    assert mru.get() == ['A']

    mru.add('B')
    assert mru.get() == ['B', 'A']

    mru.add('C')
    assert mru.get() == ['C', 'B', 'A']

    mru.add('A')
    assert mru.get() == ['A', 'C', 'B']

    mru.add('A')
    assert mru.get() == ['A', 'C', 'B']

    mru.add('D')
    assert mru.get() == ['D', 'A', 'C', 'B']

    mru.add('E')
    assert mru.get() == ['E', 'D', 'A', 'C']

    mru.add('D')
    assert mru.get() == ['D', 'E', 'A', 'C']
    '''

def test_mru():
    mru_example(MostRecentlyUsed)


def test_mru2():
    mru_example(MostRecentlyUsed2)
    
#test_mru()
test_mru2()
