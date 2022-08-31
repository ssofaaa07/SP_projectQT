from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import mapper, relationship, sessionmaker
from classes.config import *
from models.public import Year, IndicatorsName
from models import information_schema
from datetime import datetime


def optimize_id_list(id_list):  # Оптимизация списка id
    print(len(id_list))
    optimized_list, temp_list = [], []
    for ind_id in id_list:
        if not temp_list:
            temp_list.append(ind_id)
        elif ind_id - temp_list[-1] == 1:
            temp_list.append(ind_id)
        else:
            if len(temp_list) > 1:
                optimized_list.append((temp_list[0], temp_list[-1]))
            else:
                optimized_list.append(temp_list[0])
            temp_list.clear()
            temp_list.append(ind_id)

    if len(temp_list) > 1:
        optimized_list.append((temp_list[0], temp_list[-1]))
    else:
        optimized_list.append(temp_list[0])
    print(len(optimized_list))

    return optimized_list


class DataBase:
    def __init__(self):
        self.engine = create_engine(f'postgresql://{username}:{password}@{host_name}:{port}/{db_name}', echo=False)
        self.conn = self.engine.connect()
        self.meta = MetaData(self.engine)
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def get_years(self):
        years = self.session.query(Year).all()

        return sorted([str(x.year) for x in years])

    def get_indicator_names_by_schema(self, schema_name):
        table_list = self.get_table_list_by_schema(schema_name)
        indicators = self.get_indicators_by_schema(table_list, schema_name)
        if len(indicators) == 0:
            print(f"НЕ НАЙДЕНЫ ПОКАЗАТЕЛИ В СХЕМЕ {schema_name}")
            return []

        return self.get_indicators_names_by_id(indicators)

    def get_table_list_by_schema(self, schema_name):
        all_columns = information_schema.t_columns
        get_schema_tables = self.session.query(all_columns).filter(
            all_columns.c.table_schema == schema_name
        ).filter(
            all_columns.c.column_name == "id_indicator_name"
        ).all()

        return sorted(list(set(table.table_name for table in get_schema_tables)))

    def get_indicators_by_schema(self, tables, schema_name):
        indicators = set()
        for table in tables:
            sql_request = f'SELECT id_indicator_name FROM "{schema_name}".{table}'
            table_indicators = self.conn.execute(sql_request).fetchall()
            for ind in table_indicators:
                indicators.add(int(ind[0]))

        return list(indicators)

    def get_indicators_names_by_id(self, id_list):
        start = datetime.now()
        indicators = []
        for ind_id in optimize_id_list(id_list):
            if type(ind_id) == int:
                indicators.append(
                    self.session.query(IndicatorsName).filter(
                        IndicatorsName.id == ind_id
                    ).first().indicator_title
                )
            else:
                indicators_names = self.session.query(IndicatorsName).filter(
                    IndicatorsName.id >= ind_id[0]
                ).filter(
                    IndicatorsName.id <= ind_id[-1]
                ).all()
                for ind_name in indicators_names:
                    indicators.append(ind_name.indicator_title)
        print("Время подгрузки показателей из БД:", datetime.now() - start)

        return sorted(indicators)

    def get_indicators_names_by_id_old(self, id_list):
        start = datetime.now()
        indicators = []
        for ind_id in id_list:
            indicators.append(
                self.session.query(IndicatorsName).filter(
                    IndicatorsName.id == ind_id
                ).first().indicator_title
            )
        print(datetime.now() - start)

        return sorted(indicators)


DB = DataBase()
