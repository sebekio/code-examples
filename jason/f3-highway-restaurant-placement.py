
# **Pre-Drill recall of problem solving recipes**
# > Recall known approaches from memory only; no reading or searching. 
# If lookup is needed, abort drill and create a blocker-learning.
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""

"""

# Attempt 1
"""
# dp[i] = maximum total profit including restaurant i
"""

def solution(mileage: list[int], profit: list[int], min_diff: int):
  exp_profit = 0
  dp = [0] * len(mileage)
  for i, (mi, pi) in enumerate(zip(mileage, profit)):
    # including restaurant at i means accepting its profit
    dp[i] = pi
    best_prev_profit=0
    # where can you make the restaurant?
    for j in range(i):
      #  can you make a restaurant
      if mi - mileage[j] >= min_diff:
        # accept first far enough restaurant
        # if you can make a restaurant at j, just add dp[j]
        dp[i] += dp[j]
        break
  return exp_profit

m = [0, 3, 6, 10]
p = [5, 1, 4, 7]
k = 4
expected = 16
assert expected = solution(m, p, k)

# ### Attempt 1 Review
"""

**implementation skill gaps**


"""
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""

"""

# Attempt 2
"""
pseudocode
# dp[i] = max(dp[j]) + pi where {j < i, (mi - mj) >= min_dist}

"""

def solution_two(mileage: list[int], profit: list[int], min_dist: int) -> int:
  dp = [0] * len(mileage)
  for i, (mi, pi) in enumerate(zip(mileage, profit)):
    dp[i] = pi # to be increased
    for j in range(i):
      # is visiting a restaurant before this one better than just this one
      candidate_best_total_profit= dp[i] + dp[j]
      candidate_dist=mi-mileage[j]
      if candidate_best_total_profit > dp[i] and candidate_dist >= min_dist:
        dp[i] = pi + dp[j]

  return max(dp)

m = [0, 3, 6, 10]
p = [5, 1, 4, 7]
k = 4
expected = 16
assert expected = solution(m, p, k)


# ### Attempt 2 Review
"""

**implementation skill gaps**


"""
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


