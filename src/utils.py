import json

from openpyxl import load_workbook

from src.exceptions import InvalidFileException
from src.member_model import Member


def extract_from_excel_file(excel_file):
    try:
        results = []
        wb = load_workbook(filename=excel_file)
        sheet = wb["Sheet2"]

        index = 2  # Skip header
        while True:
            name = sheet[f"A{index}"].value
            if not name:
                break
            name, *rest = name.split(" - Född ")
            year = rest[0][:4]

            attendance = sheet[f"B{index}"].value
            attendance = int(attendance) if attendance else 0

            results.append((name, year, attendance))
            index += 1
        wb.close()
        return results
    except Exception as error:
        raise InvalidFileException(str(error))


def convert_table_to_clipboard_format(model):
    rows = []
    for row in model.table_data:
        row_str = [str(value) for value in row]
        if any(row_str):
            rows.append(row_str)
    return "\n".join(["\t".join(row) for row in rows])


class Converter:
    @staticmethod
    def to_json(members):
        as_dicts = [m.as_dict() for m in members]
        return json.dumps(as_dicts, ensure_ascii=False, indent=4)

    @staticmethod
    def from_json(data):
        as_dicts = json.loads(data)
        return [Member(**d) for d in as_dicts]
