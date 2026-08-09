import inspect
import contextlib
from pathlib import Path
import pydytuesday


def download_week(year: int, week_num: int) -> None:
    """
    Downloads the specified week of data from PydyTuesday into a data/
    folder next to whatever file (script or notebook) called this.
    """
    caller_globals = inspect.stack()[1].frame.f_globals
    caller_file = caller_globals.get("__file__")

    if caller_file:
        # called from a regular .py script — use its actual location,
        # regardless of what the current working directory happens to be
        caller_dir = Path(caller_file).resolve().parent
    else:
        # called from a notebook/REPL — no __file__ available,
        # so fall back to cwd (Jupyter sets this to the notebook's folder)
        caller_dir = Path.cwd()

    output_dir = caller_dir / "data"
    output_dir.mkdir(exist_ok=True)

    with contextlib.chdir(output_dir):
        pydytuesday.get_week(year, week_num)
