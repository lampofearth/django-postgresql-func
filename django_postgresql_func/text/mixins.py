from django.db.models import Func, Value, CharField


class SupportIsStringMixin(Func):

    def __ror__(self, other):
        pass

    def __rand__(self, other):
        pass

    def __init__(self, text, is_string=False, output_field=None, **extra):
        if is_string:
            text = Value(text, output_field=CharField())
        super().__init__(text, output_field=output_field, **extra)
