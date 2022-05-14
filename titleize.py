def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_word = []
    is_preceded_by_space = 1
    for char in phrase:
        if char != ' ' and is_preceded_by_space == 1:
            new_word.append(char.upper())
            is_preceded_by_space = 0
        elif char != ' ' and is_preceded_by_space == 0:
            new_word.append(char.lower())
        else:
            new_word.append(char)
            is_preceded_by_space = 1
    return new_word
