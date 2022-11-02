from member_model import MemberModel


def test_can_add_row_to_model():
    model = MemberModel()
    model.insert_row()

    assert len(model) == 1


def test_defaults_to_no_headers():
    model = MemberModel()

    assert len(model.headers) == 0


def test_can_define_headers():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers)

    assert model.headers == headers


def test_headers_can_be_accessed_qt_style():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers)

    assert model.headerData(0) == headers[0]
    assert model.headerData(1) == headers[1]
    assert model.headerData(2) == headers[2]
