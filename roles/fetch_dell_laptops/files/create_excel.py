import sys
import openpyxl

def create_excel(laptops):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Dell Laptops"

    ws.append(["Laptop Name", "Price"])
    for laptop in laptops:
        ws.append(laptop)

    file_path = "/tmp/dell_laptops.xlsx"
    wb.save(file_path)
    return file_path

if __name__ == "__main__":
    laptops = [tuple(laptop.split('|')) for laptop in sys.argv[1].split(',')]
    create_excel(laptops)