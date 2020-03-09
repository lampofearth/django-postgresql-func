from django.db.models import CharField
from django.db.models.functions import Cast
from django.db.models.functions.text import *

from django_postgresql_func.text.mixins import SupportIsStringMixin


class BitLen(SupportIsStringMixin, Transform):
    """
    Number of bits in string

    BitLen(text)

    :param text <string>:
        model field or F() or Value() or string
    :param is_string <bool>:
        if True -> 'text' force convert to string
    :return: <integer>
    """
    function = 'BIT_LENGTH'
    lookup_name = 'bit_length'


class CharLen(SupportIsStringMixin, Transform):
    """
    Number of characters in string

    CharLen(text)

    :param text <string>:
        model field or F() or Value() or string
    :param is_string <bool>:
        if True -> 'text' force convert to string
    :return: <integer>
    """
    function = 'CHAR_LENGTH'
    lookup_name = 'char_length'


class OctetLen(SupportIsStringMixin, Transform):
    """
    Number of bytes in string

    OctetLen(text)

    :param text <string>:
        model field or F() or Value() or string
    :param is_string <bool>:
        if True -> 'text' force convert to string
    :return: <integer>
    """
    function = 'OCTET_LENGTH'
    lookup_name = 'octet_length'


class Overlay(Transform):
    """
    Replace substring

    Overlay(text, substr, start=0, finish=0)
    :param text <string>:
        model field or F() or Value()
    :param substr <string>:
        model field or F() or Value()
    :param start <integer. default=0>:
        model field or F() or Value() or integer
    :return: finish <integer. default=0>:
        model field or F() or Value() or integer
   :return: <string>
    """
    function = 'OVERLAY'
    lookup_name = 'overlay'
    template = '%(function)s(%(expressions)s FROM %(start)s FOR %(finish)s)'
    arity = 2
    arg_joiner = ' PLACING '

    def __init__(self, text, substr, start=0, finish=0, **extra):
        try:
            start = int(start)
            finish - int(finish)
        except TypeError:
            raise TypeError("'start' and 'finish must be integer")

        if start >= finish:
            raise ValueError("'finish' must be greater than start.")

        super().__init__(text, substr, start=start, finish=finish, **extra)


class Position(Func):
    """
    Location of specified substring

    Position(substr, string)

    :param text <string>:
        model field or F() or Value() or string
    :param substr <string>:
        model field or F() or Value() or string
    :return: <integer>
    """
    function = 'POSITION'
    arity = 2
    arg_joiner = ' IN '


class Btrim(Func):
    """
    Remove the longest string consisting only of characters in substr
    (a space by default) from the start and end of text

    Btrim(text, substr)

    :param text <string>:
        model field or F() or Value() or string
    :param substr <string. default=' ">:
        model field or F() or Value() or string
    :return: <string>
    """
    function = 'BTRIM'

    def __init__(self, text, substr=" ", **extra):
        if not hasattr(substr, 'resolve_expression'):
            substr = Value(substr)

        super().__init__(text, substr, **extra)


class Format(Func):
    """
    Format(formatstr, *formatarg)
    :param formatstr <string>:
        model field or F() or Value() or string like sprintf
    :param *formatarg <iterator>:
        items like: model field or F() or Value() or string
    :return: string
    """

    template = 'FORMAT'

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')


class InitCap(SupportIsStringMixin, Transform):
    """
    Convert the first letter of each word to upper case and the rest to
    lower case. Words are sequences of alphanumeric characters separated
    by non-alphanumeric characters.

    InitCap(text)

    :param text <string>:
        model field or F() or Value() or string
    :return: <string>
    """
    function = 'INITCAP'


class QuoteIdent(SupportIsStringMixin, Transform):
    """
    Return the given string suitably quoted to be used as an identifier
    in an SQL statement string. Quotes are added only if necessary
    (i.e., if the string contains non-identifier characters or would
    be case-folded). Embedded quotes are properly doubled.

    QuoteIdent(text)

    :param text <string>:
        model field or F() or Value() or string
    :param substr <string>:
        model field or F() or Value() or string
    :return: <string>
    """
    function = 'QUOTE_IDENT'


class QuoteLiteral(SupportIsStringMixin, Transform):
    """
    Return the given string suitably quoted to be used as a string literal
    in an SQL statement string. Embedded single-quotes and backslashes
    are properly doubled. Note that quote_literal returns null on null
    input; if the argument might be null, quote_nullable is often more suitable.

    QuoteLiteral(text)

    :param text <string>:
        model field or F() or Value() or string
    :param substr <string>:
        model field or F() or Value() or string
    :return: <string>
    """
    function = 'QUOTE_LITERAL'


class QuoteNullable(SupportIsStringMixin, Transform):
    """
    Return the given string suitably quoted to be used as a string
    literal in an SQL statement string; or, if the argument is null,
    return NULL. Embedded single-quotes and backslashes are properly doubled.

    QuoteNullable(text)

    :param text <string>:
        model field or F() or Value() or string
    :param substr <string>:
        model field or F() or Value() or string
    :return: <string>
    """
    function = 'QUOTE_NULLABLE'


class SplitPart(Transform):
    """
    Split text on delimiter and return the given field (counting from one)

    SplitPart(text, delimiter, return_position)

    :param text <string>:
        model field or F() or Value() or string
    :param delimiter <string>:
        model field or F() or Value() or string
    :param delimiter <integer>:
        model field or F() or Value() or integer
    :return: <string>
    """
    function = 'SPLIT_PART'
    arity = 3

    def __init__(self, text, delimiter, return_position, **extra):
        if not hasattr(delimiter, 'resolve_expression'):
            delimiter = Value(delimiter, output_field=CharField())

        if not hasattr(return_position, 'resolve_expression'):
            field = Value(return_position, output_field=IntegerField())

        super().__init__(
            text, delimiter, field, output_field=CharField(), **extra)


class StrPos(Transform):
    """
    Location of specified substring
    (same as position(substr, string), but note the reversed argument order)

    StrPos(string, substring)

    :param text <string>:
        model field or F() or Value() or string
    :param substr <string>:
        model field or F() or Value() or string
    :return: <string>
    """

    function = 'STRPOS'
    arity = 2

    def __init__(self, text, substr, **extra):
        if not hasattr(substr, 'resolve_expression'):
            substr = Value(substr, output_field=CharField())

        super().__init__(text, substr, **extra)


class ToHex(SupportIsStringMixin, Transform):
    """
    *Convert number to its equivalent hexadecimal representation*

    .. code-block:: python

        ToHex(number)

    :param number: <number>
        model field or F() or Value() or digit (covert to integer)
    :return: string
    """
    function = 'TO_HEX'
    template = '%(function)s(%(expressions)s)'

    def __init__(self, number, **extra):
        if number is None:
            raise TypeError("'number' must be digit")

        if not hasattr(number, 'resolve_expression'):
            number = Cast(Value(number), output_field=IntegerField())

        super().__init__(number, output_field=CharField(), **extra)


class Translate(Func):
    """
    *Any character in 'text' that matches a character in the 'replace_from'
    is replaced by the corresponding character in the 'replacement'.
    If from is longer than to, occurrences of the extra characters in
    from are removed.*

    .. code-block:: python

        Translate(text, replace_from, replacement)

    :param text: <string>
         model field or F() or Value()
    :param replace_from: <string>
        string or F() or Value(). default Value('')
    :param replacement: <string>
        string or F() or Value(). default Value('')
    :return: <string>
    """

    function = 'TRANSLATE'

    def __init__(self, text, replace_from=Value(''), replacement=Value(''),
                 **extra):
        super().__init__(text, replace_from, replacement, **extra)
