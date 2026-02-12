
# **Pre-Drill recall of problem solving recipes**
# > Recall known approaches from memory only; no reading or searching. 
# If lookup is needed, abort drill and create a blocker-learning.
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""
Dynamic programming problem.
DP problems utilize a graph representation.
Edges represent allowed transitions between nodes.
SORTBT. Subproblem, recurrence.
"""

# Attempt 1
"""
- assuming set is not actually a set
subproblem: for denominations list X, a path can be created whose sum is v

remainder is v initially, if remainder is divisible by any x

for each coin at i
  remainder reduced by coin at i is zero 
"""

def solution(coins: list[int], v: int) -> bool:
  coins = sorted(coins)
  rem = v
  for coin in coins:
    # collect the remainder reduced by each coin
    for _coin in coins:
      if rem - _coin == 0:
        return True
      elif rem - _coin > 0:
        # subproblem = [rem - _coin]
        rem = rem - _coin
      else:
        return False
    

test_case = ""
expected = ""

# ### Attempt 1 Review
"""
What I have it top down, won't be nv.
I did a greedy subtraction, anything greedy is order dependent.
**implementation skill gaps**


"""
# ### Attempt 2
"""
can I build sum t?
for each coin, for that coin up to v, dp[reachable_total] = dp[t] or dp[t-c]

[2, 5] 7
[0,    1,     2,    3,           4,            5,           6,     7]
[True, False, True, (3-2?) False, (4-2?) True, (5-2?) False,]
array dp where each dp[i] is answer to subproblem i
subproblem here is whether you can reach i

SORTBT. Subproblem, recurrence.
Subproblem
Recursive relationship (given a subproblem, how to get to next subproblem)
Topological ordering
Base Case
Original Problem
Time Complexity
"""

"""
dp[i] is the reachability of denomination i
you can reach i if i is a coin or i is a coins distance away from where you are now
nv is a hint that we are building to v
dp[0] is True

example: [5, 10] 15

dp = [0T, 1F, 2F, 3F, 4F, 5T, 6F, 7F, 8F, 9F, 10T, 11F, 12F, 13F, 14F, 15T]
for each coin
  for i from coin to v
    dp[i] is true if i is coin
    if i - coin is true, i is true
returning dp[v]
to go from dp[1]
"""

def solution(coins: list[int], v: int) -> bool:
  if v < 0:
    return False
  dp = [False] * (v+1)
  dp[0] = True
  for coin in coins:
    if coin <= 0:
      continue
    for i in range(coin, v+1):
      if dp[i-coin]:
        dp[i] = True
  
  return dp[v]

def test():
  assert solution([5, 10], 15) is True
  assert solution([5, 10], 12) is False
  assert solution([2, 3, 7], 11) is True  # 2+2+7
  assert solution([], 0) is True
