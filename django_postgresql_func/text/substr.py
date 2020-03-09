from django.db.models.functions.text import *


class SubstrPosix(Func):
    """
    substring(string from pattern)

    :return: <string>
    """

    function = 'SUBSTRING'

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')


class SubstrSql(Func):
    """
    substring(string from pattern for escape)

    :return: <string>
    """

    function = 'SUBSTRING'

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')
