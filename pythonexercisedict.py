'''
Dictionaries

Create a function that takes 2 dictionaries and 1 list as inputs.
The output of the function should be a dictionary with one key for each value in the input list 
where the corresponding value is a list of key pairs that indicate where the input dictionaries match for that particular value.
See example below for clarification.

# Sample Output: 
{
  "math":[
    ["john","michael"],
    ["john","mary"],
    ["max","michael"],
    ["max","mary"]
  ],
  "physics":[
    ["michael","sam"]
  ],
  "p.e.":[
    ["mary","john"]
  ],
  "music":[
    ["sam","max"]
  ],
  "english": None
}


NOTES: A dictionary is not sortable.
'''

import itertools
import pprint

# Sample Input: 
best_subject = {
  "john":"math",
  "michael":"physics",
  "mary":"p.e.",
  "sam":"music",
  "max":"math"
}
  
worst_subject = {
  "john":"p.e.",
  "michael":"math",
  "mary":"math",
  "sam":"physics",
  "max":"music"
}
  
subjects = ["math","physics","p.e.","music","english"]

def students(best_subject, worst_subject, subjects):
    
    #create 1 dict, which will get appended to each loop
    stud = {}
    
    for s in subjects:
        
        #needs to be inside loop to restart the lists each loop,
        #otherwise if it is outside, it will add too many values to the list
        best = []
        worst = []
        
        for k,v in best_subject.items():
            if v == s:
                best.append(k)
        
        for k,v in worst_subject.items():
            if v == s:
                worst.append(k)
        
        #utilize itertools to make cartesian product of lists
        result = list(itertools.product(best,worst))
            
        stud[s] = None if len(result) == 0 else result

    return stud

buddies = students(best_subject, worst_subject, subjects)
pprint.pprint(buddies)

