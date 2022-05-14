def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('AaaahhhHHhHHh', 'h')
        'AaaaHHHhhHhhH'

    """
    phrase_list = list(phrase)
    swapped_list = []
    for char in phrase_list:
        if to_swap.upper() == char.upper() and char.isupper():
            swapped_list.append(char.lower())
        elif to_swap.upper() == char.upper() and char.islower():
            swapped_list.append(char.upper())
        else:
            swapped_list.append(char)
    swapped_phrase = ''.join(swapped_list)
    return swapped_phrase