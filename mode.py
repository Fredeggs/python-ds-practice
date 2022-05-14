def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    number_count = {}
    for num in nums:
        if num in number_count.keys():
            number_count[num] += 1
        else:
            number_count[num] = 1
    max_count = max(number_count)
    print(number_count.items())
    for (num, freq) in number_count.items():
        if freq == max_count:
            return num

    
