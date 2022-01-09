def get_rabbit_pairs(n: int, k: int) -> int:
    """n = number of months, k = number of rabbit pairs from each mating pair
    """
    if n < 3:
        # Base case, no rabbits reproduce in the first 2 months
        return 1
    else:
        # Recursive case
        # Number of pairs in nth month = number of pairs from previous month
        # + pairs from 2 months before producing k pairs each (since they've
        # reached reproductive age)
        return get_rabbit_pairs(n - 1, k) + k * get_rabbit_pairs(n - 2, k)


if __name__ == '__main__':
    with open("rosalind_fib.txt", "r") as f:
        n, k = f.readlines()[0].strip().split(" ")
        output = open("solution.txt", "w")
        output.write(str(get_rabbit_pairs(int(n), int(k))))
        output.close()