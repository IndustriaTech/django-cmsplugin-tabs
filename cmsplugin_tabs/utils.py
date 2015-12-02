
try:
    from django.utils.encoding import force_str, force_text
except ImportError:
    # Django < 1.5
    from django.utils.encoding import smart_str, force_unicode as force_text

    def force_str(*args, **kwargs):
        return str(smart_str(*args, **kwargs))


__all__ = ['force_str', 'force_text']
