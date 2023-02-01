def hailstone(num):
    """
        This function takes a positive integer parameter as the initial number of a hailstone sequence
        and returns the number of steps it takes to reach 1.

        If the initial number is even, it is divided by two to get the next integer in the sequence.
        If it is odd, it is multiplied by three and added one to get the next integer in the sequence.
        The process continues until the value is equal to 1.

        num: The starting number of the hailstone sequence. Must be a positive integer.

        Returns:
        steps: The number of steps it takes to reach 1. If the starting integer is 1, the return value is 0.
    """

    steps = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        steps += 1
    return steps
