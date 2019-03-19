import random

def bubble_sort(l: list):
    """ Sort list l in-place super fast. """
    for pass_num in range(len(l)-1,0,-1): # Move back to front.
        for i in range(pass_num):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp

if '__main__' == __name__:
    int_list = [random.randint(0,10) for r in range(5)]
    print('Unsorted List:\t', int_list)

    bubble_sort(int_list)
    print('Sorted List:\t', int_list)
