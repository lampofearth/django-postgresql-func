from django.db.models import CharField
from django.db.models.functions.text import *
from django.utils.functional import cached_property


class Convert(Transform):
    """
    Convert(string bytes, src_encoding name, dest_encoding name)

    :return: bytes
    """

    function = 'CONVERT'
    arity = 3

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')


class ConvertFrom(Transform):
    """
    ConvertFrom(string bytea, src_encoding name)

    :return: text
    """

    function = 'CONVERT_FROM'
    arity = 2

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')


class ConvertTo(Transform):
    """
    ConvertTo(string text, dest_encoding name)

    :return: bytes
    """

    function = 'CONVERT_TO'
    arity = 2

    def __init__(self, text, dest_encoding, **extra):
        super().__init__(text, dest_encoding, output_field=CharField(),
                         **extra)

    @cached_property
    def convert_value(self):
        return lambda value, expression, connection: \
            None if value is None else bytes(value)


class Decode(Transform):
    """
    Decode(string text, format text)
    Получает двоичные данные
    из текстового представления в string. Значения параметра format те же,
    что и для функции encode.	decode('MTIzAAE=', 'base64')	\x3132330001
    :return: bytes
    """

    function = 'DECODE'
    arity = 2

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')


class Encode(Transform):
    """
    Encode(data bytea, format text)

    :return text:
    """

    function = 'ENCODE'
    arity = 2

    def __init__(self, *expressions, **extra):
        raise NotSupportedError('This function is not implemented in '
                                'the current version.')


class ClientEncoding(Func):
    """
    ClientEncoding()
    :return: string
    """
    function = 'PG_CLIENT_ENCODING'
    template = '%(function)s()'

    def __init__(self, **extra):
        super().__init__(output_field=CharField(), **extra)


class ToASCII(Func):
    """
    ToASCII(string text [, encoding text])
    :return: string
    """
    function = 'TO_ASCII'
    template = '%(function)s(%(expressions)s)'

    valid_encoding = ['LATIN1', 'LATIN2', 'LATIN9' 'WIN1250']

    def __init__(self, text, encoding, force=False, **extra):
        encoding = encoding.upper()
        if not force:
            if encoding not in self.valid_encoding:
                raise ValueError(
                    f"'encoding' mut be in {', '.join(self.valid_encoding)}")

        super().__init__(text, encoding, output_field=CharField(), **extra)
