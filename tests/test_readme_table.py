# importation of the solution function to test
import pandas as pd
import markdown, os
from markdown.extensions.tables import TableExtension

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(CURRENT_DIR, "..", "README.md")


def read_table(readme_path=README_PATH):
    """"""

    with open(readme_path, "r") as file:
        md = "".join(file.readlines())
        md_for_html = "".join(md)
        html = markdown.markdown(
            md_for_html, extensions=[TableExtension(use_align_attribute=True)]
        )

    df = pd.read_html(html, index_col=0)[0]

    return df


def test_contains_table():
    """This is the test for the implemented solution passing
    valid inputs"""

    df = read_table()

    assert df.shape == (3, 3)
    print("[Info] Initial table structure still exists")
