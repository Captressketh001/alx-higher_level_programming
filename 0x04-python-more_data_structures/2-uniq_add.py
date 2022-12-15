#!/usr/bin/python3
def uniq_add(my_list=[]):
  sum = 0 
  if not my_list:
    return None

  uniques = set(my_list)
  for i in uniques:
    sum += i
  return sum
