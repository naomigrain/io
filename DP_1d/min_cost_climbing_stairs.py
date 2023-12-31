# https://leetcode.com/problems/min-cost-climbing-stairs/

def min_cost_climbing_stairs(cost: list[int]) -> int:
    cost.append(0)
    for i in range(len(cost) - 3, -1, -1):
        cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
    return min(cost[0], cost[1])

def testcase(solution):
    print(solution([10,15,20]) == 15)
    print(solution([1,100,1,1,1,100,1,1,100,1]) == 6)


if __name__ == "__main__":
    testcase(min_cost_climbing_stairs)