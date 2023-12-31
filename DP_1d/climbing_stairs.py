# https://leetcode.com/problems/climbing-stairs/

def climbing_stairs(n: int) -> tuple:
    # n is height of stairs
    # using fibonacci
    one, two = 1, 1
    for i in range(n - 1):
        x = one
        one = one + two
        two = x
        print(i, one, two, x)
    return (one, two, x)


if __name__ == "__main__":
    print("res", climbing_stairs(5))