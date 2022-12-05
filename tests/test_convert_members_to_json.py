from src.member_model import Member
from src.utils import Converter


def test_can_convert_to_and_from_json():
    members = [
        Member("Adäm", "1995", grade="kyu 4", last_graded="5/12/22", lessons=123)
    ]

    as_json = Converter.to_json(members)
    recreated = Converter.from_json(as_json)

    assert recreated == members
