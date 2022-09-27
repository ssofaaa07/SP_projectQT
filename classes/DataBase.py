from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from classes.config import *
from models.public import Year, IndicatorsName, Indicator, IndicationsRf, IndicationsVo
from models import information_schema


def optimize_id_list(id_list):  # Оптимизация списка id
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

    return optimized_list


class DataBase:
    def __init__(self):
        self.engine = create_engine(f'postgresql://{username}:{password}@{host_name}:{port}/{db_name}', echo=False)
        self.conn = self.engine.connect()
        self.meta = MetaData(self.engine)
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def get_table_list_by_schema_and_table_name(self, schema_name, table_name):
        all_columns = information_schema.t_tables
        get_schema_tables = self.session.query(all_columns).filter(
            all_columns.c.table_schema == schema_name
        ).filter(
            all_columns.c.table_name.like(table_name)
        ).all()

        return sorted(list(set(table.table_name for table in get_schema_tables)))

    def get_table_list_by_schema_and_column_name(self, schema_name, column_name):
        all_columns = information_schema.t_columns
        get_schema_tables = self.session.query(all_columns).filter(
            all_columns.c.table_schema == schema_name
        ).filter(
            all_columns.c.column_name == column_name
        ).all()

        return sorted(list(set(table.table_name for table in get_schema_tables)))

    def get_indicators_names_by_id(self, id_list):
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

        return sorted(indicators)

    def get_years(self):
        years = self.session.query(Year).all()

        return sorted([str(x.year) for x in years])

    def get_industries(self):
        all_columns = information_schema.t_columns
        industries = self.session.query(all_columns).filter(
            all_columns.c.table_name.like('events_grbs____')
        ).all()
        industries_names = sorted(list(set(industry[1] for industry in industries)))

        industries_names_ru = []
        for industry in industries_names:
            sql_request = f'''
            SELECT obj_description('"{industry}"'::regnamespace, 'pg_namespace')
            '''
            industries_names_ru.append(self.conn.execute(sql_request).fetchall()[0][0])

        return industries_names, industries_names_ru

    def get_GP_indicators_names(self, schema_name):
        tables_with_ind_names = "names_indicators____"
        tables = self.get_table_list_by_schema_and_table_name(schema_name, tables_with_ind_names)

        indicators_names = []
        for table in tables:
            sql_request = f'SELECT title_indication FROM "{schema_name}".{table}'
            indicators_names += self.conn.execute(sql_request).fetchall()

        return [ind_name[0] for ind_name in indicators_names]

    def get_GP_indicators(self, schema_name):
        tables_with_indicators = "indicators____"
        tables = self.get_table_list_by_schema_and_table_name(schema_name, tables_with_indicators)

        indicators = []
        for table in tables:
            sql_request = f'SELECT * FROM "{schema_name}".{table}'
            indicators += self.conn.execute(sql_request).fetchall()

        return indicators

    def get_strategy_indicators_names(self):
        table_list = self.get_table_list_by_schema_and_column_name("Strategies", "id_indicator_name")
        indicators = set()
        for table in table_list:
            sql_request = f'SELECT id_indicator_name FROM "Strategies".{table}'
            table_indicators = self.conn.execute(sql_request).fetchall()
            for ind in table_indicators:
                indicators.add(int(ind[0]))

        return self.get_indicators_names_by_id(indicators)

    def get_strategy_indicators(self):
        table_list = self.get_table_list_by_schema_and_column_name("Strategies", "id_indicator_name")
        indicators = set()
        for table in table_list:
            sql_request = f'SELECT * FROM "Strategies".{table}'
            table_indicators = self.conn.execute(sql_request).fetchall()
            indicators += table_indicators

        return indicators

    def get_PM_indicators_names(self):
        indicators = list(set(indicator.title_id for indicator in self.session.query(Indicator).all()))
        indicators_names = []
        for ind_id in optimize_id_list(indicators):
            temp_ind_names = self.session.query(IndicatorsName).filter(
                IndicatorsName.id >= ind_id[0]
            ).filter(
                IndicatorsName.id <= ind_id[-1]
            ).all()
            for ind_name in temp_ind_names:
                indicators_names.append(ind_name.indicator_title)

        return indicators_names

    def get_PM_indicators(self):
        indicators = [
            [
                indicator.id,
                indicator.title_id,
                indicator.year_id,
                indicator.indicator,
                indicator.may_be_less,
                indicator.may_be_more
            ] for indicator in self.session.query(Indicator).all()
        ]

        return indicators

    def get_RP_indicators_names(self, schema_name):
        # ОЖИДАНИЕ ГОТОВЫХ РЕГИОНАЛЬНЫХ ПРОЕКТОВ
        pass

    def get_RP_indicators(self, schema_name):
        # ОЖИДАНИЕ ГОТОВЫХ РЕГИОНАЛЬНЫХ ПРОЕКТОВ
        pass

    def get_CYR_indicators_names(self):
        indicators = list(set(indicator.ind_title_rf for indicator in self.session.query(IndicationsRf).all())) + list(
            set(indicator.ind_title_vo for indicator in self.session.query(IndicationsVo).all()))

        return indicators
