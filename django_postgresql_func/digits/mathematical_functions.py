from django.db.models import F, Value, ExpressionWrapper
from django.db.models.functions.math import *
from django.db.models import DecimalField


class Cbrt(Transform):
    """
    *Cube root*

    .. code-block:: python

        Cbrt(value)

    :param value <integer or decimal>:
        model field or F() or Value()
    :return: <integer or decimal>
    """
    function = 'CBRT'
    lookup_name = 'cbrt'


class Div(Transform):
    """
    *Numeric integer quotient of y/x*

    .. code-block:: python

        Div(y, x)

    :param y <integer or decimal>:
        model field or F() or Value() or integer or decimal
    :param x <integer or decimal>:
        model field or F() or Value() or integer or decimal. Not 0
    :return: <integer or decimal> default integer
    """
    function = 'DIV'
    arity = 2
    lookup_name = 'div'

    def __init__(self, y, x, output_field=None, **extra):
        output_field = \
            output_field if output_field is not None else IntegerField()

        super().__init__(y, x, output_field=output_field, **extra)


class Trunc(Transform):
    """
    *Numeric truncate to s decimal places*

    .. code-block:: python

        Trunc(value, plc=0)

    :param value: <integer or decimal>
        model field or F() or Value() or integer or decimal
    :param plc: <integer. default=0>
        model field or F() or Value()
    :return: <integer or decimal> default decimal
    """
    function = 'TRUNC'
    lookup_name = 'Trunc'
    arity = 2

    def __init__(self, value, plc=0, output_field=None, **extra):
        output_field = \
            output_field if output_field is not None else DecimalField()

        if not hasattr(plc, 'resolve_expression'):
            try:
                plc = int(plc)
            except ValueError:
                raise ValueError('"s" must be a number or a value that '
                                 'can be converted to a number')
        expression = [value, plc]
        super().__init__(*expression, output_field=output_field, **extra)