
# **Pre-Drill recall of problem solving recipes**
# > Recall known approaches from memory only; no reading or searching. 
# If lookup is needed, abort drill and create a blocker-learning.
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""

"""

# Attempt 1
"""
Define the DP state:
E[i] = maximum sum of a non-empty contiguous subsequence ending at index i.

Recurrence:
E[0] = a[0]
E[i] = max(a[i], a[i] + E[i-1]) for i ≥ 1

Track:
best_sum = max over all E[i]
best_end = index where best_sum occurs

To reconstruct the subsequence, also store a start index:
start[i] = start index of the subsequence achieving E[i].
If we “start new” at i (choose a[i]), then start[i] = i.
If we “extend” (choose a[i] + E[i-1]), then start[i] = start[i-1].

After filling, the answer subsequence is a[start[best_end] : best_end+1].

Implementation analysis (matches your rubric)

(1) # subproblems: O(n) states (E[0..n-1])

(2) runtime to fill: O(n). Each state does O(1) work (one add, one compare, a couple assignments) under the word-RAM model.

(3) final return extraction: pick argmax_i E[i] (track on the fly), then slice using (best_start, best_end).

(4) runtime to extract: O(k) to output the subsequence of length k (and O(1) to return indices). Worst-case k = n, so O(n).
"""
from typing import List, Tuple

def max_sum_contiguous_subsequence_nonempty(a: List[int]) -> Tuple[List[int], int]:
    """
    Returns (subsequence, max_sum) for the maximum-sum non-empty contiguous subsequence.
    Runs in O(n) time. Uses O(n) extra space for start indices to enable reconstruction.
    """
    if not a:
        raise ValueError("Input list must be non-empty for the non-empty subsequence variant.")

    n = len(a)
    E = [0] * n          # best sum ending at i
    start = [0] * n      # start index of the best ending-at-i subsequence

    E[0] = a[0]
    start[0] = 0

    best_sum = E[0]
    best_end = 0

    for i in range(1, n):
        extend = a[i] + E[i - 1]
        if a[i] >= extend:
            E[i] = a[i]
            start[i] = i
        else:
            E[i] = extend
            start[i] = start[i - 1]

        if E[i] > best_sum:
            best_sum = E[i]
            best_end = i

    best_start = start[best_end]
    subseq = a[best_start:best_end + 1]
    return subseq, best_sum
