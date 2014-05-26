from django.template import Library


register = Library()


@register.filter(is_safe=False)
def addf(value, arg):
    """Adds the arg to the value."""
    try:
        return float(value) + float(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''
