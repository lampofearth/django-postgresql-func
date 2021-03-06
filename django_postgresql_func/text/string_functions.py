from django.db.models import CharField, Expression
from django.db.models.functions import Cast
from django.db.models.functions.text import *

from django_postgresql_func.text.mixins import SupportIsStringMixin


class BitLen(SupportIsStringMixin, Transform):
    """
    *Number of bits in string*

    .. code-block:: python

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
    *Number of characters in string*

    .. code-block:: python

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
    *Number of bytes in string*

    .. code-block:: python

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
    *Replace substring*

    .. code-block:: python

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


class Position(Transform):
    """
    *Location of specified substring*

    .. code-block:: python

        Position(string, substr)

    :param text <string>:
        model field or F() or Value() or string
    :param substr <string>:
        model field or F() or Value() or string
    :param is_string <bool>:
        if True -> 'substr' force convert to string
    :return: <integer>
    """
    function = 'POSITION'
    arity = 2
    arg_joiner = ' IN '

    def __init__(self, text, substr, is_string=False, **extra):
        if is_string:
            substr = Value(substr, output_field=CharField())
        super().__init__(substr, text, **extra)


class Btrim(Func):
    """
    *Remove the longest string consisting only of characters in substr
    (a space by default) from the start and end of text*

    .. code-block:: python

        Btrim(text, substr)

    :param text <string>:
        model field or F() or Value() or string
    :param substr <string. default=" ">:
        model field or F() or Value() or string
    :return: <string>
    """
    function = 'BTRIM'

    def __init__(self, text, substr=" ", is_string=False, **extra):
        if is_string:
            substr = Value(substr, output_field=CharField())
        else:
            if not hasattr(substr, 'resolve_expression'):
                substr = Value(substr)
        super().__init__(text, substr, **extra)


class Format(Func):
    """
     .. code-block:: python

        Format(formatstr, *formatarg)

    :param text <string>:
        F() - for model field or Value(), string - for string
    :param params <iterator>:
        items like: F() - for model field or Value(), string - for string
    :return: string
    """

    function = 'FORMAT'

    def __init__(self, text, params, output_field=None, **extra):
        if not hasattr(text, 'resolve_expression'):
            text = Value(text)
        
        params = (Value(i) if not hasattr(i, 'resolve_expression')
                     else i for i in params)

        output_field = CharField() if output_field is None else output_field

        super().__init__(text, *params, output_field=output_field, **extra)


class InitCap(SupportIsStringMixin, Transform):
    """
    *Convert the first letter of each word to upper case and the rest to
    lower case. Words are sequences of alphanumeric characters separated
    by non-alphanumeric characters.*

    .. code-block:: python

        InitCap(text)

    :param text <string>:
        model field or F() or Value() or string
    :param is_string <bool>:
        if True -> 'text' force convert to string
    :return: <string>
    """
    function = 'INITCAP'


class QuoteIdent(SupportIsStringMixin, Transform):
    """
    *Return the given string suitably quoted to be used as an identifier
    in an SQL statement string. Quotes are added only if necessary
    (i.e., if the string contains non-identifier characters or would
    be case-folded). Embedded quotes are properly doubled.*

    .. code-block:: python

        QuoteIdent(text)

    :param text <string>:
        model field or F() or Value() or string
    :param is_string <bool>:
        if True -> 'text' force convert to string
    :return: <string>
    """
    function = 'QUOTE_IDENT'


class QuoteLiteral(SupportIsStringMixin, Transform):
    """
    *Return the given string suitably quoted to be used as a string literal
    in an SQL statement string. Embedded single-quotes and backslashes
    are properly doubled. Note that quote_literal returns null on null
    input; if the argument might be null, quote_nullable is often more suitable.*

    .. code-block:: python

        QuoteLiteral(text)

    :param text <string>:
        model field or F() or Value() or string
    :param is_string <bool>:
        if True -> 'text' force convert to string
    :return: <string>
    """
    function = 'QUOTE_LITERAL'


class QuoteNullable(SupportIsStringMixin, Transform):
    """
    *Return the given string suitably quoted to be used as a string
    literal in an SQL statement string; or, if the argument is null,
    return NULL. Embedded single-quotes and backslashes are properly
    doubled.*

    .. code-block:: python

        QuoteNullable(text)

    :param text <string>:
        model field or F() or Value() or string
    :param is_string <bool>:
        if True -> 'text' force convert to string
    :return: <string>
    """
    function = 'QUOTE_NULLABLE'


class SplitPart(Transform):
    """
    *Split text on delimiter and return the given field (counting from one)*

    .. code-block:: python

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
    *Location of specified substring
    (same as position(substr, string), but note the reversed argument order)*

    .. code-block:: python

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
