# CS162Python-Project4a
# project-4a

Modify the binary search function from the exploration so that, instead of returning -1 when the target value is not in the list, raises a TargetNotFound exception (you'll need to define this exception class).  Otherwise it should function normally.  Name this function bin_except.

The file must be named: **bin_except.py**

def binary_search(a_list, target):    
  """    
  Searches a_list for an occurrence of target    
  If found, returns the index of its position in the list    
  If not found, returns -1, indicating the target value isn't in the list    
  """    
  first = 0    
  last = len(a_list) - 1    
  while first <= last:        
    middle = (first + last) // 2        
    if a_list[middle] == target:            
      return middle        
    if a_list[middle] > target:            
      last = middle - 1        
    else:            
      first = middle + 1    
  return -1
