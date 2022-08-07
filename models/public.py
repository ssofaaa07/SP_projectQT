# coding: utf-8
from sqlalchemy import Boolean, CHAR, Column, Float, ForeignKey, Integer, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AreasOfInfluence(Base):
    __tablename__ = 'areas_of_influence'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".areas_of_influence_id_seq'::regclass)"))
    status = Column(Text)
    title = Column(Text, nullable=False)


class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".categories_id_seq'::regclass)"))
    category = Column(Text, nullable=False)
    unit_of_measurement = Column(String(60))


class Cyr(Base):
    __tablename__ = 'cyr'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    title_cyr = Column(Text, nullable=False)


class Done(Base):
    __tablename__ = 'done'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    done_or_not = Column(CHAR(1), nullable=False)


class ExpectedResult(Base):
    __tablename__ = 'expected_result'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".expected_result_id_seq'::regclass)"))
    result = Column(Text, nullable=False)


class FinancingSource(Base):
    __tablename__ = 'financing_source'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    source = Column(Text, nullable=False)


class Gosprogram(Base):
    __tablename__ = 'gosprogram'
    __table_args__ = {'schema': 'public'}

    id = Column(String(60), primary_key=True)
    title_prog = Column(Text, nullable=False)

    target_gosprogram_vo = relationship('TargetGosprogramVo', secondary='public.gosprogram_target')


class Grb(Base):
    __tablename__ = 'grbs'
    __table_args__ = {'schema': 'public'}

    kbk = Column(String(60), primary_key=True)
    title = Column(Text, nullable=False)


t_growth_point_and_response_obj = Table(
    'growth_point_and_response_obj', metadata,
    Column('gp_id', Text, nullable=False),
    Column('id_response_obj', Integer, nullable=False),
    schema='public'
)


class GrowthPointName(Base):
    __tablename__ = 'growth_point_names'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".growth_point_names_id_seq'::regclass)"))
    growth_point_title = Column(Text)


class ImplementationPeriod(Base):
    __tablename__ = 'implementation_period'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    period = Column(Text, nullable=False)


class Kbk2016(Base):
    __tablename__ = 'kbk2016'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".kbk2016_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2017(Base):
    __tablename__ = 'kbk2017'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".kbk2017_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2018(Base):
    __tablename__ = 'kbk2018'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".kbk2018_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2019(Base):
    __tablename__ = 'kbk2019'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".kbk2019_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2020(Base):
    __tablename__ = 'kbk2020'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".kbk2020_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2021(Base):
    __tablename__ = 'kbk2021'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".kbk2021_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class Kbk2022(Base):
    __tablename__ = 'kbk2022'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".kbk2022_id_seq'::regclass)"))
    code = Column(String(60), nullable=False)


class PlanFact(Base):
    __tablename__ = 'plan_fact'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    plan_fact = Column(CHAR(1), nullable=False)


class RegionsCfo(Base):
    __tablename__ = 'regions_cfo'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".regions_cfo_id_seq'::regclass)"))
    region = Column(Text, nullable=False)


class ResponseObj(Base):
    __tablename__ = 'response_obj'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    response_obj = Column(Text, nullable=False)


class Specialization(Base):
    __tablename__ = 'specializations'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".specializations_id_seq'::regclass)"))
    title = Column(Text, nullable=False)


class StrategyAim(Base):
    __tablename__ = 'strategy_aim'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".strategy_aim_id_seq'::regclass)"))
    aim = Column(Text, nullable=False)

    gosprogram = relationship('Gosprogram', secondary='public.aim_and_gosprogram')


class TargetGosprogramVo(Base):
    __tablename__ = 'target_gosprogram_vo'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    target = Column(Text, nullable=False)


class TitlesItem(Base):
    __tablename__ = 'titles_items'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".titles_items_id_seq'::regclass)"))
    expense_item = Column(Text, nullable=False)


class Violation(Base):
    __tablename__ = 'violation'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    violation_or_not = Column(CHAR(1), nullable=False)


class Year(Base):
    __tablename__ = 'years'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)


class AdministrativeDistrict(Base):
    __tablename__ = 'administrative_districts'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".administrative_districts_id_seq'::regclass)"))
    id_area_of_influence = Column(ForeignKey('public.areas_of_influence.id'))
    title = Column(Text, nullable=False)

    areas_of_influence = relationship('AreasOfInfluence')


t_aim_and_gosprogram = Table(
    'aim_and_gosprogram', metadata,
    Column('id_aim', ForeignKey('public.strategy_aim.id')),
    Column('id_prog', ForeignKey('public.gosprogram.id')),
    schema='public'
)


t_gosprogram_target = Table(
    'gosprogram_target', metadata,
    Column('id_prog', ForeignKey('public.gosprogram.id'), primary_key=True, nullable=False),
    Column('id_target', ForeignKey('public.target_gosprogram_vo.id'), primary_key=True, nullable=False),
    schema='public'
)


class IndicationsVo(Base):
    __tablename__ = 'indications_vo'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    id_response = Column(ForeignKey('public.response_obj.id'))
    ind_title_vo = Column(Text, nullable=False)

    response_obj = relationship('ResponseObj')


class StrategySubAim(Base):
    __tablename__ = 'strategy_sub_aim'
    __table_args__ = {'schema': 'public'}

    id = Column(Text, primary_key=True)
    title = Column(Text, nullable=False)
    aim_id = Column(ForeignKey('public.strategy_aim.id'))

    aim = relationship('StrategyAim')


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    id_cyr = Column(ForeignKey('public.cyr.id'))
    task = Column(Text, nullable=False)

    cyr = relationship('Cyr')


class AllEvent(Base):
    __tablename__ = 'all_events'
    __table_args__ = {'schema': 'public'}

    id = Column(Text, primary_key=True)
    id_aim = Column(ForeignKey('public.strategy_sub_aim.id'), nullable=False)
    id_period = Column(ForeignKey('public.implementation_period.id'), nullable=False)
    id_result = Column(ForeignKey('public.expected_result.id'), nullable=False)
    id_fin_source = Column(ForeignKey('public.financing_source.id'))
    id_prog = Column(ForeignKey('public.gosprogram.id'))
    sub_event = Column(Text, nullable=False)

    strategy_sub_aim = relationship('StrategySubAim')
    financing_source = relationship('FinancingSource')
    implementation_period = relationship('ImplementationPeriod')
    gosprogram = relationship('Gosprogram')
    expected_result = relationship('ExpectedResult')
    response_obj = relationship('ResponseObj', secondary='public.events_and_response_obj')


class IndicationsRf(Base):
    __tablename__ = 'indications_rf'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    id_task = Column(ForeignKey('public.tasks.id'))
    ind_title_rf = Column(Text, nullable=False)

    task = relationship('Task')
    indications_vo = relationship('IndicationsVo', secondary='public.indications_rf_vo')
    target_gosprogram_vo = relationship('TargetGosprogramVo', secondary='public.indications_rf_target')


class IndicatorsName(Base):
    __tablename__ = 'indicators_names'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    indicator_title = Column(Text, nullable=False)
    indicator_type = Column(Text)
    sub_aim = Column(ForeignKey('public.strategy_sub_aim.id'))

    strategy_sub_aim = relationship('StrategySubAim')
    response_obj = relationship('ResponseObj', secondary='public.indicators_and_response_obj')


class Region(Base):
    __tablename__ = 'regions'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"public\".regions_id_seq'::regclass)"))
    id_district = Column(ForeignKey('public.administrative_districts.id'))
    title = Column(Text, nullable=False)

    administrative_district = relationship('AdministrativeDistrict')
    specializations = relationship('Specialization', secondary='public.regions_and_specializations')


class StrategyTask(Base):
    __tablename__ = 'strategy_tasks'
    __table_args__ = {'schema': 'public'}

    id = Column(Text, primary_key=True)
    title = Column(Text, nullable=False)
    sub_aim_id = Column(ForeignKey('public.strategy_sub_aim.id'))

    sub_aim = relationship('StrategySubAim')


t_events_and_response_obj = Table(
    'events_and_response_obj', metadata,
    Column('id_event', ForeignKey('public.all_events.id')),
    Column('id_response_obj', ForeignKey('public.response_obj.id')),
    schema='public'
)


class GosprogramVo(Base):
    __tablename__ = 'gosprogram_vo'
    __table_args__ = (
        UniqueConstraint('id_ind_rf', 'id_ind_vo'),
        {'schema': 'public'}
    )

    id = Column(Integer, primary_key=True)
    id_prog = Column(ForeignKey('public.gosprogram.id'), nullable=False)
    id_response = Column(ForeignKey('public.response_obj.id'))
    id_ind_rf = Column(ForeignKey('public.indications_rf.id'))
    id_ind_vo = Column(ForeignKey('public.indications_vo.id'))

    indications_rf = relationship('IndicationsRf')
    indications_vo = relationship('IndicationsVo')
    gosprogram = relationship('Gosprogram')
    response_obj = relationship('ResponseObj')


class GrowthPoint(Base):
    __tablename__ = 'growth_point'
    __table_args__ = {'schema': 'public'}

    id = Column(Text, primary_key=True)
    sub_aim_id = Column(ForeignKey('public.strategy_sub_aim.id'), nullable=False)
    task_id = Column(ForeignKey('public.strategy_tasks.id'))
    id_period = Column(ForeignKey('public.implementation_period.id'), nullable=False)
    id_result = Column(ForeignKey('public.expected_result.id'))
    id_fin_source = Column(ForeignKey('public.financing_source.id'))
    id_prog = Column(ForeignKey('public.gosprogram.id'))
    title = Column(Text, nullable=False)

    financing_source = relationship('FinancingSource')
    implementation_period = relationship('ImplementationPeriod')
    gosprogram = relationship('Gosprogram')
    expected_result = relationship('ExpectedResult')
    sub_aim = relationship('StrategySubAim')
    task = relationship('StrategyTask')


t_indications_rf_target = Table(
    'indications_rf_target', metadata,
    Column('id_ind_rf', ForeignKey('public.indications_rf.id'), primary_key=True, nullable=False),
    Column('id_target', ForeignKey('public.target_gosprogram_vo.id'), primary_key=True, nullable=False),
    schema='public'
)


t_indications_rf_vo = Table(
    'indications_rf_vo', metadata,
    Column('id_ind_rf', ForeignKey('public.indications_rf.id'), primary_key=True, nullable=False),
    Column('id_ind_vo', ForeignKey('public.indications_vo.id'), primary_key=True, nullable=False),
    schema='public'
)


class Indicator(Base):
    __tablename__ = 'indicators'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    title_id = Column(ForeignKey('public.indicators_names.id'))
    year_id = Column(ForeignKey('public.years.id'))
    indicator = Column(Float)
    may_be_less = Column(Boolean, nullable=False)
    may_be_more = Column(Boolean, nullable=False)

    title = relationship('IndicatorsName')
    year = relationship('Year')


t_indicators_and_response_obj = Table(
    'indicators_and_response_obj', metadata,
    Column('id_ind', ForeignKey('public.indicators_names.id')),
    Column('id_resp_obj', ForeignKey('public.response_obj.id')),
    schema='public'
)


t_regions_and_specializations = Table(
    'regions_and_specializations', metadata,
    Column('id_region', ForeignKey('public.regions.id'), primary_key=True, nullable=False),
    Column('id_specialization', ForeignKey('public.specializations.id'), primary_key=True, nullable=False),
    schema='public'
)
