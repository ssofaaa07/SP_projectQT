import openpyxl

from classes.TableBlockConstructor import TableBlockConstructor

book = openpyxl.open('CYR_GP.xlsx', read_only=True)
sheet = book.active
cells = sheet['B2':'C12']

T = TableBlockConstructor.fill_CYR_sample(TableBlockConstructor(), "x", "x", "x", "x", "x", "x", "x", "x")
for first, second in T:
    print(first.value, '    ', second.value)