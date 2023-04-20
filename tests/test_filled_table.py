# importation of the solution function to test
import os
from tests.test_readme_table import read_table

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
empty_json_table = {
    "Project's Name": {1: "", 2: "", 3: ""},
    "Description": {1: "", 2: "", 3: ""},
    "GitHub's Link": {1: "", 2: "", 3: ""},
}


def test_not_empty_table():
    """This is the test for the implemented solution passing
    valid inputs"""

    df = read_table()

    assert (
        df.replace("-", "").replace("https://", "").replace(" ", "").to_dict()
        != empty_json_table
    )

    print("[Info] Table no more empty")


def test_not_empty_rows():
    """This is the test for the implemented solution passing
    valid inputs"""

    df = (
        read_table()
        .replace("-", "")
        .replace("https://", "")
        .replace(" ", "")
        .drop_duplicates(keep=False)
    )
    df = df[df["Project's Name"] != ""] # exclude projects without Name
    df = df[df["Description"] != ""] # exclude projects without description
    df = df[df["GitHub's Link"] != ""] # exclude project without link

    n_filled_rows = df.shape[0]
    n_empty_rows = 3 - n_filled_rows

    print(f"[Info] {n_filled_rows} filled rows, {n_empty_rows} empty rows, ")

    assert n_filled_rows == 3

    print("[Info] All rows have been filled")
