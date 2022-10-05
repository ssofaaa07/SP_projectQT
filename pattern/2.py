import openpyxl

from classes.TableBlockConstructor import TableBlockConstructor

book = openpyxl.open('CYR_GP.xlsx')
sheet = book.active
# sheet['C3'].value = 'rere'
# sheet['B7'].value = 1
# book.save('rere.xlsx')
years = (2022, 2021, 2020, 2016, 2017)
plan_fact = (40, 40, 40, 5, 5, 0)
fact_plan = (60, 70, 56, 5, 6, 0)

# (self, indicator, event_id, event, main_event_id, main_event, subprogram_id, subprogram,
#                        type, unit, years, plan_marks, fact_marks, comment)

TableBlockConstructor.fill_CYR_sample('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x')
TableBlockConstructor.fill_GP_sample('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', years,
                                     plan_fact, fact_plan, '2005', 'gsfsrhf')

