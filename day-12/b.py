import sys
from tqdm import tqdm

def main():
    data = sys.stdin.read()
    lines = data.splitlines()
    x = 0
    for line in tqdm(lines):
        x += solve(*parse_b(line))
    print(x)

def parse_b(line):
    data, nums = line.split(" ")
    return "?".join([data]*5), list(map(int, nums.split(",")))*5

def solve(s, nums):
    s+="."
    n = len(s)
    k = len(nums)
    nums.append(n + 1)
    dp = [[[0 for _ in range(n + 1)] for _ in range(k + 2)] for _ in range(n + 1)] # pos, num_groups, curr_eln
    dp[0][0][0] = 1
    for i in range(n): # position
        for j in range(k+1): # num groups
            for p in range(n): # curr len
                cur = dp[i][j][p]
                if cur == 0:
                    continue
                if s[i] == '.' or s[i] == '?':
                    if p == 0 or p == nums[j - 1]: # end of group, can reset
                        dp[i + 1][j][0] += cur
                if s[i] == '#' or s[i] == '?':
                    dp[i + 1][j + int(p==0)][p + 1] += cur
    return dp[n][k][0]

main()
