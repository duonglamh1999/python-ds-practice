def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return [int(num) for num in str(num1) ].sort() ==[int(num) for num in str(num2)].sort()
print(same_frequency(321142, 3212215))