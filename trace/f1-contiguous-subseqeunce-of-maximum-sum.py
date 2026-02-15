
# **Pre-Drill recall of problem solving recipes**
# > Recall known approaches from memory only; no reading or searching. 
# If lookup is needed, abort drill and create a blocker-learning.
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""

"""

# Attempt 1
"""
pseudocode

"""

def max_contiguous_subsequence(arr: list[int]):
  curr_sum, max_sum = 0, 0
  dp = list()
  for i, elem in enumerate(arr):
    curr_sum += elem
    if curr_sum < 0:
      dp.clear()
      curr_sum = 0
    elif curr_sum > max_sum:
      dp.append(elem)
      max_sum = curr_sum
  return dp


test_case = ""
expected = ""

# ### Attempt 1 Review
"""

**implementation skill gaps**


"""
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Attempt 2

"""
MaxSumSubseq adds to the largest number
DAG - when can two nodes connect?
- next to eachother

subproblem:
-- sum of sequence starting at j and ending at i

accumulate the max([subproblems]) at all i.
maintain prev to reconstruct solution

input array a

at each i < n
at each j < i
subproblem ending at each j,i is the sum of aj when
"""
def max_subarray(S : list[int]) -> tuple[list[int], int]:
  dp = [0] * (n+1)
  #dp[i] is the max sum of any contiguous subsequence ending at index i
  #dp[i] = max(0, dp[i-1] + S[i])
  current_sum = 0
  current_start = 0

  best_sum = 0
  best_start = 0
  best_end = -1

  for i in range(len(S)):
    if current_sum + S[i] < 0:
      current_sum = 0
      current_start = i+1
    else:
      current_sum += S[i]
      if current_sum > best_sum:
        best_sum = current_sum
        best_start = current_start
        best_end = i
  return S[best_start:best_end+1], best_sum


