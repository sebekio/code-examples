# **Pre-Drill recall of problem solving recipes**
# > Recall known approaches from memory only; no reading or searching. 
# If lookup is needed, abort drill and create a blocker-learning.
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""
I should be splitting the array in half. I should maintain a dictionary of frequencies.
I don't really know how to solve these problems.
"""
# ## Attempt 1
def subproblem(arr: list[int]) -> Union(int, None):
    freq = dict()
    for elem in arr:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1
    majorityFreq = None
    majorityElem = None
    for elem, freq in freq.values():
        if freq > majorityFreq:
            majorityFreq = freq
            majorityElem = elem
    
    return (majorityElem, majorityFreq)
    
def solution(arr: list[int]) -> Union(int, None):
    # split in half
    midIndex = len(arr) // 2
    left = arr[:midIndex]
    right = arr[midIndex:]
    # compare halves
    leftMaj, leftFreq = subproblem(left)
    rightMaj, rightFreq = subproblem(right)

    if leftMaj == rightMaj:
        return leftMaj
    elif leftMaj != rightMaj:
        # compare frequencies
        if leftFreq > len(arr) / 2:
            return leftFreq
        if rightFreq > len(arr) / 2:
            return rightFreq
    elif not leftMaj or not rightMaj:
        return None

# Attempt 1 Review
"""
What I tried to do was not divide and conquer at all.
I tripped myself up clinging too strongly to the subproblem phrasing when I didn't actually know how divide and conquer is supposed to work.

**implementation skill gaps**
- splitting array in half
- accumulating item frequencies
- dict.items() is how you see (key and val) > drill iterate through maps
tionw
"""

# Attempt two
# recall
"""
I will visualize as a tree.
driver + recursive dc algorithm
general shape is 
dc():
    base_case
    dc()
    combination_rules > return
Split down with a=2, b=2 and combine up with pair-cancel Boyer-Moore
"""
# pseudocode
"""
driver()
    call dc on whole problem

dc() on window of array [start, end]
    break into left and right passing it to dc(left), dc(right) until at leaf node

    compare two leaf nodes
        agreeing majorities > definite majority
        competing majorities > check majority
        verify half majority > check majority

    choosing a list majority from 1-2 options:
        - check occurences of each
        - one with occurence count greater than list length over 2 is majority

the one that appears the most, must appear most most of the time
"""
# dc is the majority_element in given list
def solution(arr: list[Any]) -> Any | None:
    return majority_element(0, len(arr) - 1, arr)

def check_majority(arr: list[Any], left_maj: Any = None, right_maj: Any = None) -> Any | None:
    # check occurrences of non None majorities
    if left_maj is None and right_maj is None: return None

    left_freq = right_freq = 0
    for elem in arr:
        if left_maj is not None and elem == left_maj:
            left_freq += 1    
        if right_maj is not None and elem == right_maj:
            right_freq += 1
    # only one or None have freq greater than len(arr) - 1 // 2
    maj_len = len(arr) // 2
    if left_freq > maj_len:
        return left_maj
    elif right_freq > maj_len:
        return right_maj
    return None

def majority_element(start: int, end: int, arr: list[Any]) -> Any | None:
    # divide
    # is it divisible and not a leaf node?
    if start == end:
        return arr[start]
    else:
        # divide in half and recurse
        middle_idx = end // 2
        left_sublist = arr[start:middle_idx]
        left_elem = majority_element(left_sublist)
        right_sublist = arr[middle_idx:]
        right_elem = majority_element(right_sublist)

        # agreeing majorities
        if right_elem == left_elem:
            return right_elem
        # competing majorities
        check_majority(arr, left_elem, right_elem)

# Attempt 2 Review
"""
- what does // mean?
"""

# Tests
"""
what if list length is odd and not even?

"""
tc_1 = [1, 1, 1, 1, 1, 1]
exp = 1

tc_2 = [1, 2, 3, 4, 5, 6]
exp = None

tc_3 = []