__all__ = ("import_from_string",)

from django.utils.module_loading import import_string


def import_from_string(val):
    """
    Attempt to import a class from a string representation.
    """
    try:
        return import_string(val)
    except ImportError as error:
        msg = "Could not import '%s' for Custom Handler setting. %s: %s." % (val, error.__class__.__name__, error)
        raise ImportError(msg)
