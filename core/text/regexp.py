from django.db.models.functions.text import *


class RegexpMatch(Func):
    """
    RegexpMatch(string text, pattern text [, flags text])
    """

    template = 'REGEXP_MATCH'

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')


class RegexpMatches(Func):
    """
    RegexpMatches(string text, pattern text [, flags text])
    """

    template = 'REGEXP_MATCHES'

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')


class RegexpReplace(Func):
    """
    RegexpReplace(string text, pattern text, replacement text [, flags text])
    """

    template = 'REGEXP_REPLACE'

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')


class RegexpSplitToArray(Func):
    """
    RegexpSplitToArray(string text, pattern text [, flags text ])
    """

    template = 'REGEXP_SPLIT_TO_ARRAY'

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')


class RegexpSplitToTable(Func):
    """
    RegexpSplitToTable(string text, pattern text [, flags text ])
    """

    template = 'REGEXP_SPLIT_TO_TABLE'

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')
