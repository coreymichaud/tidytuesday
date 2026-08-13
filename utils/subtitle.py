import textwrap


def wrap_subtitle(subtitle: str, width: int) -> str:
    """
    Wraps the subtitle text to the specified width.
    """

    wrapped = "<br>".join(textwrap.wrap(subtitle, width=width))
    return wrapped
