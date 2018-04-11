from collections import Iterable

# d = {'a': 1, 'b': 2, 'c': 3}
#
# for key in d:
#     print(key)
#
# for ch in 'jona':
#     print(ch)
#
# print(isinstance('abc',Iterable))
# print(isinstance([1,2,3],Iterable))
# print(isinstance(123,Iterable))
#
# for i,value in enumerate(['a','b','c']):
#     print(i,value)

def findMinAndMax(L=[]):
    minvalue = L[0]
    maxvalue = L[0]
    for pre in L[1:]:
        if (minvalue > pre):
            minvale = pre
        if (maxvalue < pre):
            maxvalue = pre
    return minvalue, maxvalue

a = [9, 7, 1, 10, 56, 89, 555, 454, 559, -1, 0]
print(findMinAndMax(a))