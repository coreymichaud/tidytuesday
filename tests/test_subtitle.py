from utils.subtitle import wrap_subtitle


def test_wrap_subtitle():
    subtitle = "This is a long subtitle that should be wrapped."

    result = wrap_subtitle(subtitle, width=10)

    assert result == "This is a<br>long<br>subtitle<br>that<br>should be<br>wrapped."


def test_wrap_subtitle_short_text():
    subtitle = "Hello world"

    result = wrap_subtitle(subtitle, width=20)

    assert result == "Hello world"


def test_wrap_subtitle_exact_width():
    subtitle = "Hello world"

    result = wrap_subtitle(subtitle, width=11)

    assert result == "Hello world"


def test_wrap_subtitle_empty_string():
    result = wrap_subtitle("", width=10)

    assert result == ""
