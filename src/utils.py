from openpyxl import load_workbook


def extract_from_excel_file(excel_file):
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
    return results
