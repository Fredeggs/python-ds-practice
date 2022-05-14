def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_list = list(phrase)
    phrase_list.reverse()
    reversed = ''.join(phrase_list)
    reversed_no_spaces = reversed.replace(' ','')
    phrase_no_spaces = phrase.replace(' ','')
    return reversed_no_spaces.upper() == phrase_no_spaces.upper()
