def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    listedPhrase = list(phrase)
    listedPhrase.reverse()
    return ''.join(listedPhrase)
