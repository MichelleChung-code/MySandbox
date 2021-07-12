def repr_str(obj, kwargs):
    """
    Args:
        obj: object
        kwargs: dictionary or arguments to display

    Returns:
        <str>
    """
    return f'{obj.__class__.__name__}({kwargs})'
