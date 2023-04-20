# importation of the solution function to test
import os
from tests.test_readme_table import read_table

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
empty_json_table = {
    "Project's Name": {1: "", 2: "", 3: ""},
    "Description": {1: "", 2: "", 3: ""},
    "GitHub's Link": {1: "", 2: "", 3: ""},
}


def test_empty_table():
    """This is the test for the implemented solution passing
    valid inputs"""

    df = read_table()

    assert (
        df.replace("-", "").replace("https://", "").replace(" ", "").to_dict()
        == empty_json_table
    )

    print("[Info] Empty table")
