from pathlib import Path
from unittest.mock import patch

from utils.download import download_week


def make_stack(caller_file):
    fake_globals = {"__file__": str(caller_file)}

    frame = type(
        "Frame",
        (),
        {
            "frame": type(
                "FrameInfo",
                (),
                {"f_globals": fake_globals},
            )()
        },
    )()

    return [None, frame]


def test_download_week(tmp_path):
    caller_file = tmp_path / "script.py"

    with patch("utils.download.inspect.stack") as mock_stack:
        mock_stack.return_value = make_stack(caller_file)

        with patch("utils.download.pydytuesday.get_week") as mock_get_week:

            def check_download_location(year, week):
                assert Path.cwd() == tmp_path / "data"

            mock_get_week.side_effect = check_download_location

            download_week(2024, 10)

    assert (tmp_path / "data").is_dir()
    mock_get_week.assert_called_once_with(2024, 10)


def test_download_week_without_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    fake_globals = {}

    frame = type(
        "Frame",
        (),
        {
            "frame": type(
                "FrameInfo",
                (),
                {"f_globals": fake_globals},
            )()
        },
    )()

    with patch("utils.download.inspect.stack") as mock_stack:
        mock_stack.return_value = [None, frame]

        with patch("utils.download.pydytuesday.get_week") as mock_get_week:
            download_week(2024, 10)

    assert (tmp_path / "data").is_dir()
    mock_get_week.assert_called_once_with(2024, 10)
