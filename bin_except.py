#Author: Ashley Johnson
#Date: 4/16/2021
#Description: Program searches a list for target number and if found, returns the index
#where target was found in list. If target number is not in list, program raises a
#TargetNotFound exception.

class TargetNotFound(Exception):
  """
  provides an exception if target is not found in bin_except function
  """
  pass

def bin_except(binary_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, raises TargetNotFound exception
  """
  first = 0
  last = len(binary_list) - 1
  while first <= last:
    middle = (first + last) // 2
    if binary_list[middle] == target:
      return middle
    if binary_list[middle] > target:
      last = middle - 1
    else:
      first = middle + 1
  raise TargetNotFound("Target Not Found")


def main():
    binary_list=[1,2,3,4,5]
    target = 6
    try:
         index =bin_except(binary_list, target)
         print("Target was found on index: ",index)
    except TargetNotFound:
         print("target Not Found")


if __name__ == "__main__": main()