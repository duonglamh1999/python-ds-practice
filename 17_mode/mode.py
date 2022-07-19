from statistics import mode
def modeFunc(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> modeFunc([1, 2, 1])
        1

        >>> modeFunc([2, 2, 3, 3, 2])
        2
    """
    return mode(nums)
print(modeFunc([2, 2, 3, 3, 2]))