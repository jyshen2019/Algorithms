"""Insertion Sort
>>> ll = [23, 11, 45, 88, 20, 19, 18, 17, 99, 1, 67]
>>> print(insertion_sort(ll))
[1, 11, 17, 18, 19, 20, 23, 45, 67, 88, 99]

"""
import doctest

def insertion_sort(ll):
    for i in range(len(ll)):
        j = i
        while j > 0 and ll[j] < ll[j - 1]:
            ll[j], ll[j - 1] = ll[j - 1], ll[j]
            j -= 1
    return ll

if __name__ == "__main__":
    doctest.testmod()