# import time
#
# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import mapper, relationship, sessionmaker
# from classes.config import *
# from models.public import Year, IndicatorsName
# from models import information_schema
# from datetime import datetime
#
#
# def optimize_id_list(id_list):  # Оптимизация списка id
#     optimized_list, temp_list = [], []
#     for ind_id in id_list:
#         if not temp_list:
#             temp_list.append(ind_id)
#         elif ind_id - temp_list[-1] == 1:
#             temp_list.append(ind_id)
#         else:
#             if len(temp_list) > 1:
#                 optimized_list.append((temp_list[0], temp_list[-1]))
#             else:
#                 optimized_list.append(temp_list[0])
#             temp_list.clear()
#             temp_list.append(ind_id)
#
#     if len(temp_list) > 1:
#         optimized_list.append((temp_list[0], temp_list[-1]))
#     else:
#         optimized_list.append(temp_list[0])
#     # print("Уровень оптимизации списка показателей:", 100 - int(len(optimized_list)/len(id_list)*100), "%")
#
#     return optimized_list
#
#
# class DataBase:
#     def __init__(self):
#         self.engine = create_engine(f'postgresql://{username}:{password}@{host_name}:{port}/{db_name}', echo=True)
#         self.conn = self.engine.connect()
#         self.meta = MetaData(self.engine)
#         self.DBSession = sessionmaker(bind=self.engine)
#         self.session = self.DBSession()
#
#     def get_years(self):
#         years = self.session.query(Year).all()
#
#         return sorted([str(x.year) for x in years])
#
#     def get_indicator_names_by_schema(self, schema_name):
#         start = datetime.now()
#
#         if schema_name == "Strategies":
#             table_list = self.get_table_list_by_schema(schema_name, "id_indicator_name")
#             indicators = self.get_indicators_by_schema(table_list, schema_name, "id_indicator_name")
#             return self.get_indicators_names_by_id(indicators)
#         elif schema_name == "PM":
#             table_list = ["indicators"]
#             indicators = self.get_indicators_by_schema(table_list, "public", "title_id")
#             return self.get_indicators_names_by_id(indicators)
#         elif schema_name == "CYR":
#             print("В РАЗРАБОТКЕ")
#             return []
#             table_list = ["indications_rf", "indications_vo"]
#             indicators = self.get_indicators_by_schema([table_list[0]], "public", "ind_title_rf")
#             indicators += self.get_indicators_by_schema([table_list[1]], "public", "ind_title_vo")
#             return indicators
#         else:
#             print("В РАЗРАБОТКЕ")
#             return []
#             # table_list = self.get_table_list_by_schema(schema_name, "indication_id")
#             # print(table_list)
#             # indicators = self.get_indicators_by_schema(table_list, schema_name, "indication_id")
#
#         # print("Время поиска таблиц с показателями из БД:", datetime.now() - start)
#
#         # print(f"НЕ НАЙДЕНЫ ПОКАЗАТЕЛИ В СХЕМЕ {schema_name}")
#         return []
#
#     def get_table_list_by_schema(self, schema_name, column_name):
#         all_columns = information_schema.t_columns
#         get_schema_tables = self.session.query(all_columns).filter(
#             all_columns.c.table_schema == schema_name
#         ).filter(
#             all_columns.c.column_name == column_name
#         ).all()
#
#         return sorted(list(set(table.table_name for table in get_schema_tables)))
#
#     def get_indicators_by_schema(self, tables, schema_name, column_name):
#         indicators = set()
#         for table in tables:
#             sql_request = f'SELECT {column_name} FROM "{schema_name}".{table}'
#             table_indicators = self.conn.execute(sql_request).fetchall()
#             for ind in table_indicators:
#                 indicators.add(int(ind[0]))
#
#         return list(indicators)
#
#     def get_indicators_names_by_id(self, id_list):
#         start = datetime.now()
#         indicators = []
#         for ind_id in optimize_id_list(id_list):
#             if type(ind_id) == int:
#                 indicators.append(
#                     self.session.query(IndicatorsName).filter(
#                         IndicatorsName.id == ind_id
#                     ).first().indicator_title
#                 )
#             else:
#                 indicators_names = self.session.query(IndicatorsName).filter(
#                     IndicatorsName.id >= ind_id[0]
#                 ).filter(
#                     IndicatorsName.id <= ind_id[-1]
#                 ).all()
#                 for ind_name in indicators_names:
#                     indicators.append(ind_name.indicator_title)
#         # print("Время подгрузки показателей из БД:", datetime.now() - start)
#
#         return sorted(indicators)
#
#     def get_indicators_names_by_id_old(self, id_list):
#         start = datetime.now()
#         indicators = []
#         for ind_id in id_list:
#             indicators.append(
#                 self.session.query(IndicatorsName).filter(
#                     IndicatorsName.id == ind_id
#                 ).first().indicator_title
#             )
#         print("Время подгрузки показателей из БД(без оптимизации):", datetime.now() - start)
#
#         return sorted(indicators)
#
#     def get_indicators_names_by_industry(self, id_list, schema_name):
#         ind_names_table_list = self.get_table_list_by_schema(schema_name, "title_indication")
#         for table in ind_names_table_list:
#             pass
#         for ind_id in id_list:
#             # sql_request = f'SELECT title_indication FROM '
#             pass
#
# DB = DataBase()
