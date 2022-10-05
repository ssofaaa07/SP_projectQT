from copy import copy

import openpyxl
import xlwt
from openpyxl import Workbook
from openpyxl.cell import Cell  # КЛАСС ЯЧЕЙКИ, С КОТОРЫМ ТЕБЕ ПРЕДСТОИТ РАБОТАТЬ, ПОЧИТАЙ О НЕМ ПОДРОБНЕЕ В ДОКАХ
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Font, Side, Border, PatternFill, NamedStyle, Alignment


"""
Для корректной работы надо сначала запустить метод CYR, потом GP. 
Полученный файл будет называться CYR_GP_2
"""


def create_diagram(sheet, min_row, max_row, min_col, max_col, cell):
    chart1 = BarChart()
    chart1.type = "col"
    chart1.style = 10
    chart1.title = "Динамика изменения значений показателя"
    chart1.y_axis.delete = True
    chart1.x_axis.delete = False
    data = Reference(sheet, min_col=min_col + 1, max_col=max_col, min_row=min_row - 1, max_row=max_row - 1)
    categor = Reference(sheet, min_col=min_col, min_row=min_row, max_row=max_row)
    chart1.add_data(data, titles_from_data=True)
    chart1.set_categories(categor)
    sheet.add_chart(chart1, cell)

class TableBlockConstructor:
    # def __init__(self):
    #
    #

    """
    Все переменные должны быть типа str.

    indicator - наименование показателя,
    event_id - номер мероприятия, event - название мероприятия,
    main_event_id - номер основного мероприятия, main_event - название основного мероприятия,
    subprogram_id - номер подпрограммы, subprogram - название подпрограммы,
    type - тип (не поняла, что это именно - разберёшься),
    unit - единица измерения,
    years - список лет,
    plan_marks - список плановых значений показателя (порядок должен СОВПАДАТЬ с порядком лет),
    fact_marks - список фактических значений показателя (порядок должен СОВПАДАТЬ с порядком лет),
    year_comment - год комментария,
    comment - комментарий

    """
    def fill_GP_sample(self, indicator, event_id, event, main_event_id, main_event, subprogram_id, subprogram,
                       type, unit, years, plan_marks, fact_marks, year_comment, comment):
        file = "CYR_GP_1.xlsx"
        book = openpyxl.open(file)
        sheet = book.active
        sheet['F3'].value = indicator
        sheet['E4'].value = sheet['E4'].value + ' №' + event_id
        sheet['F4'].value = event
        sheet['E5'].value = sheet['E5'].value[:21] + '№' + main_event_id
        sheet['F5'].value = main_event
        sheet['E6'].value = sheet['E6'].value[:13] + '№' + subprogram_id
        sheet['F6'].value = subprogram
        sheet['F7'].value = type
        sheet['F8'].value = unit
        for i in range(len(years)):
            if i > 4:
                sheet.insert_rows(i + 11)
                sheet.row_dimensions[i + 11].height = 18
                font = Font(name='Times New Roman', size=12, bold=False, color='000000')
                thins = Side(border_style="medium", color="000000")
                double = Side(border_style="thin", color="000000")
                name_style = NamedStyle(name="years")
                name_style.font = font
                name_style.border = Border(top=double, bottom=double, left=double, right=double)
                sheet['E' + str(i + 11)].border = Border(top=double, bottom=double, left=thins, right=double)
                sheet['F' + str(i + 11)].border = Border(top=double, bottom=double, left=double, right=double)
                sheet['G' + str(i + 11)].border = Border(top=double, bottom=double, left=double, right=thins)
                sheet['E' + str(i + 11)].font = Font(name='Times New Roman', size=14, bold=False, color='000000')
                sheet['F' + str(i + 11)].font = font
                sheet['G' + str(i + 11)].font = font
                sheet['E' + str(i + 11)].fill = PatternFill('solid', fgColor="e4efdc")
                sheet['E' + str(i + 11)].alignment = Alignment(horizontal='center')
                sheet['F' + str(i + 11)].alignment = Alignment(horizontal='center')
                sheet['G' + str(i + 11)].alignment = Alignment(horizontal='center')
            sheet['E' + str(i + 11)].value = years[i]
            sheet['F' + str(i + 11)].value = plan_marks[i]
            sheet['G' + str(i + 11)].value = fact_marks[i]
        sheet['E' + str(len(years) + 11)].value = 'Комментарий (' + str(year_comment) + ' г.)'
        sheet['F' + str(len(years) + 11)].value = comment
        sheet.row_dimensions[len(years) + 11].height = 172.25
        create_diagram(sheet, 11, len(years) + 11, 5, 7, 'E' + str(len(years) + 13))
        book.save('CYR_GP_2.xlsx')

    """
    Все переменные должны быть типа str.

    indicator_rf - наименование показателя РФ, 
    task_id - номер задачи, 
    task - формулировка задачи, 
    cyr_id - номер ЦУРа, 
    cyr - формулировка ЦУР, 
    indicator_vo - наименование показателя ВО, 
    gosprogram - госпрограмма,
    response_obj - ответственный орган
    
    """
    def fill_CYR_sample(self, indicator_rf, task_id, task, cyr_id, cyr, indicator_vo, gosprogram, response_obj):
        file = "CYR_GP.xlsx"
        book = openpyxl.open(file)
        sheet = book.active
        sheet['C3'].value = indicator_rf
        sheet['B5'].value = sheet['B5'].value[:7] + '№' + task_id
        sheet['C5'].value = task
        sheet['B6'].value = sheet['B6'].value[:4] + '№' + cyr_id
        sheet['C6'].value = cyr
        sheet['C10'].value = indicator_vo
        sheet['C11'].value = gosprogram
        sheet['C12'].value = response_obj
        book.save('CYR_GP_1.xlsx')
