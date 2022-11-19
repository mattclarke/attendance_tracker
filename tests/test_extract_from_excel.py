import pathlib

from src.utils import extract_from_excel_file


class Member:
    def __init__(self, name, year):
        self.name = name
        self.birth_year = year
        self.attendances = 0

    def __repr__(self):
        return f"{self.name} = {self.attendances}"


def test_can_extract_relevant_data():
    excel_file = pathlib.Path(__file__).parent / "Oversikt_example.xlsx"

    extracted_data = extract_from_excel_file(excel_file)

    assert len(extracted_data) == 9
    assert extracted_data[0] == ("Adam Adamson", "2007", 3)
    assert extracted_data[1] == ("Björn Svenson", "1993", 37)
    assert extracted_data[2] == ("Anita Olafson", "2000", 3)
    assert extracted_data[3] == ("Anders Anderson", "1969", 14)
    assert extracted_data[4] == ("Olaf Petterson", "1998", 1)
    assert extracted_data[5] == ("John Smith", "1965", 13)
    assert extracted_data[6] == ("Peter Brolin", "2012", 0)
    assert extracted_data[7] == ("Mari Sántiago", "1985", 3)
    assert extracted_data[8] == ("Sally Double-Barrelled", "2009", 4)
