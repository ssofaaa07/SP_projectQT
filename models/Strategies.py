# coding: utf-8
from sqlalchemy import CHAR, Column, Date, Float, ForeignKey, Integer, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AimsStrategy(Base):
    __tablename__ = 'aims_strategy'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".aims_strategy_id_seq'::regclass)"))
    title = Column(Text, nullable=False)


class DevelopmentOppsVo(Base):
    __tablename__ = 'development_opps_vo'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".development_opps_vo_id_seq'::regclass)"))
    opportunity = Column(Text, nullable=False)


class DirectionsOfDevelopment(Base):
    __tablename__ = 'directions_of_development'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".directions_of_development_id_seq'::regclass)"))
    title = Column(Text, nullable=False)

    regions = relationship('Region', secondary='Strategies.development_of_regions')


class DirectionsOfDevelopmentFinance(Base):
    __tablename__ = 'directions_of_development_finance'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".directions_of_development_finance_id_seq'::regclass)"))
    title = Column(Text, nullable=False)


class EvaluationOfOpp(Base):
    __tablename__ = 'evaluation_of_opps'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".evaluation_of_opps_id_seq'::regclass)"))
    evaluation_criteria = Column(Text, nullable=False)


class ProductCategory(Base):
    __tablename__ = 'product_categories'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".product_categories_id_seq'::regclass)"))
    lower_bound_code = Column(Integer)
    upper_bound_code = Column(Integer)
    title = Column(Text)


class Rating(Base):
    __tablename__ = 'ratings'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".ratings_id_seq'::regclass)"))
    title_rating = Column(Text, nullable=False)


class ResearchArea(Base):
    __tablename__ = 'research_area'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".research_area_id_seq'::regclass)"))
    title_area = Column(Text, nullable=False)


class ThreatsDevelopmentVo(Base):
    __tablename__ = 'threats_development_vo'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".threats_development_vo_id_seq'::regclass)"))
    threat = Column(Text, nullable=False)


class ToolsGchp(Base):
    __tablename__ = 'tools_gchp'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".tools_gchp_id_seq'::regclass)"))
    title = Column(Text, nullable=False)


class TypeOfScenario(Base):
    __tablename__ = 'type_of_scenario'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True)
    scenario = Column(Text, nullable=False)


class TypesOfDocument(Base):
    __tablename__ = 'types_of_documents'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".types_of_documents_id_seq'::regclass)"))
    title = Column(Text, nullable=False)


class AreasOfInfluence(Base):
    __tablename__ = 'areas_of_influence'

    id = Column(Integer, primary_key=True, server_default=text("nextval('areas_of_influence_id_seq'::regclass)"))
    status = Column(Text)
    title = Column(Text, nullable=False)


class FinancingSource(Base):
    __tablename__ = 'financing_source'

    id = Column(Integer, primary_key=True)
    source = Column(Text, nullable=False)


class Gosprogram(Base):
    __tablename__ = 'gosprogram'

    id = Column(String(60), primary_key=True)
    title_prog = Column(Text, nullable=False)


class ImplementationPeriod(Base):
    __tablename__ = 'implementation_period'

    id = Column(Integer, primary_key=True)
    period = Column(Text, nullable=False)


class RegionsCfo(Base):
    __tablename__ = 'regions_cfo'

    id = Column(Integer, primary_key=True, server_default=text("nextval('regions_cfo_id_seq'::regclass)"))
    region = Column(Text, nullable=False)


class ResponseObj(Base):
    __tablename__ = 'response_obj'

    id = Column(Integer, primary_key=True)
    response_obj = Column(Text, nullable=False)


class StrategyAim(Base):
    __tablename__ = 'strategy_aim'

    id = Column(Integer, primary_key=True, server_default=text("nextval('strategy_aim_id_seq'::regclass)"))
    aim = Column(Text, nullable=False)


class Year(Base):
    __tablename__ = 'years'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)


class CoefficientsOfDifferences12(Base):
    __tablename__ = 'coefficients_of_differences12'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".coefficients_of_differences12_id_seq'::regclass)"))
    id_year = Column(ForeignKey('years.id'))
    id_scenario = Column(ForeignKey('Strategies.type_of_scenario.id'))
    percent = Column(Float(53))

    type_of_scenario = relationship('TypeOfScenario')
    year = relationship('Year')


class EvaluationValueOpp(Base):
    __tablename__ = 'evaluation_value_opps'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".evaluation_value_opps_id_seq'::regclass)"))
    id_opportunity = Column(ForeignKey('Strategies.development_opps_vo.id'))
    id_criteria = Column(ForeignKey('Strategies.evaluation_of_opps.id'))
    lower_bound = Column(Float(53))
    upper_bound = Column(Float(53))

    evaluation_of_opp = relationship('EvaluationOfOpp')
    development_opps_vo = relationship('DevelopmentOppsVo')


class EvaluationValueThreat(Base):
    __tablename__ = 'evaluation_value_threats'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".evaluation_value_threats_id_seq'::regclass)"))
    id_threat = Column(ForeignKey('Strategies.threats_development_vo.id'))
    id_criteria = Column(ForeignKey('Strategies.evaluation_of_opps.id'))
    lower_bound = Column(Float(53))
    upper_bound = Column(Float(53))

    evaluation_of_opp = relationship('EvaluationOfOpp')
    threats_development_vo = relationship('ThreatsDevelopmentVo')


class IndustrialIndice(Base):
    __tablename__ = 'industrial_indices'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".industrial_indices_id_seq'::regclass)"))
    id_region_cfo = Column(ForeignKey('regions_cfo.id'))
    id_year = Column(ForeignKey('years.id'))
    index_ = Column(Float(53))

    regions_cfo = relationship('RegionsCfo')
    year = relationship('Year')


class Measure(Base):
    __tablename__ = 'measures'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".measures_id_seq'::regclass)"))
    id_direction_of_development_finance = Column(ForeignKey('Strategies.directions_of_development_finance.id'))
    id_response_obj = Column(ForeignKey('response_obj.id'))
    title = Column(Text)

    directions_of_development_finance = relationship('DirectionsOfDevelopmentFinance')
    response_obj = relationship('ResponseObj')
    types_of_documents = relationship('TypesOfDocument', secondary='Strategies.measures_and_documents')


class PlaceOfVoRating(Base):
    __tablename__ = 'place_of_vo_rating'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".place_of_vo_rating_id_seq'::regclass)"))
    id_rating = Column(ForeignKey('Strategies.ratings.id'))
    id_area = Column(ForeignKey('Strategies.research_area.id'))
    id_year = Column(ForeignKey('years.id'))
    place = Column(Integer)

    research_area = relationship('ResearchArea')
    rating = relationship('Rating')
    year = relationship('Year')


class ProjectsStrategy(Base):
    __tablename__ = 'projects_strategy'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".projects_strategy_id_seq'::regclass)"))
    id_aim_strategy = Column(ForeignKey('Strategies.aims_strategy.id'))
    id_implementation_period = Column(ForeignKey('implementation_period.id'))
    title = Column(Text)
    content = Column(Text)

    aims_strategy = relationship('AimsStrategy')
    implementation_period = relationship('ImplementationPeriod')


class RegulatoryLegalAct(Base):
    __tablename__ = 'regulatory_legal_acts'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".regulatory_legal_acts_id_seq'::regclass)"))
    id_type_of_document = Column(ForeignKey('Strategies.types_of_documents.id'))
    id_response_obj_developer = Column(ForeignKey('response_obj.id'))
    title = Column(Text)
    date_of_acceptance = Column(Text)

    response_obj = relationship('ResponseObj')
    types_of_document = relationship('TypesOfDocument')


class Sector(Base):
    __tablename__ = 'sector'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".sector_id_seq'::regclass)"))
    id_gosprogram = Column(ForeignKey('gosprogram.id'))
    title_sector = Column(Text, nullable=False)

    gosprogram = relationship('Gosprogram')


class Values18(Base):
    __tablename__ = 'values18'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".values18_id_seq'::regclass)"))
    id_product_category = Column(ForeignKey('Strategies.product_categories.id'))
    id_year = Column(ForeignKey('years.id'))
    export_import = Column(CHAR(1))
    unit_of_measurement = Column(String(60))
    value_ = Column(Float(53))

    product_category = relationship('ProductCategory')
    year = relationship('Year')


class AdministrativeDistrict(Base):
    __tablename__ = 'administrative_districts'

    id = Column(Integer, primary_key=True, server_default=text("nextval('administrative_districts_id_seq'::regclass)"))
    id_area_of_influence = Column(ForeignKey('areas_of_influence.id'))
    title = Column(Text, nullable=False)

    areas_of_influence = relationship('AreasOfInfluence')


class StrategySubAim(Base):
    __tablename__ = 'strategy_sub_aim'

    id = Column(Text, primary_key=True)
    title = Column(Text, nullable=False)
    aim_id = Column(ForeignKey('strategy_aim.id'))

    aim = relationship('StrategyAim')


class AmountOfFunding(Base):
    __tablename__ = 'amount_of_funding'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".amount_of_funding_id_seq'::regclass)"))
    id_implementation_period = Column(ForeignKey('implementation_period.id'))
    id_financing_source = Column(ForeignKey('financing_source.id'))
    id_project = Column(ForeignKey('Strategies.projects_strategy.id'))
    v_mln = Column(Float(53))

    financing_source = relationship('FinancingSource')
    implementation_period = relationship('ImplementationPeriod')
    projects_strategy = relationship('ProjectsStrategy')


class ImplementationMechanism(Base):
    __tablename__ = 'implementation_mechanism'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".implementation_mechanism_id_seq'::regclass)"))
    id_gosprogram = Column(ForeignKey('gosprogram.id'))
    id_project = Column(ForeignKey('Strategies.projects_strategy.id'))
    addition = Column(Text)

    gosprogram = relationship('Gosprogram')
    projects_strategy = relationship('ProjectsStrategy')


t_measures_and_documents = Table(
    'measures_and_documents', metadata,
    Column('id_measure', ForeignKey('Strategies.measures.id'), primary_key=True, nullable=False),
    Column('id_type_of_document', ForeignKey('Strategies.types_of_documents.id'), primary_key=True, nullable=False),
    schema='Strategies'
)


class PriorityTool(Base):
    __tablename__ = 'priority_tools'
    __table_args__ = {'schema': 'Strategies'}

    id_sector = Column(ForeignKey('Strategies.sector.id'), primary_key=True, nullable=False)
    id_tool_gchp = Column(ForeignKey('Strategies.tools_gchp.id'), primary_key=True, nullable=False)
    form_of_participation = Column(Text)

    sector = relationship('Sector')
    tools_gchp = relationship('ToolsGchp')


class Values15(Base):
    __tablename__ = 'values15'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".indicators15_id_seq'::regclass)"))
    id_sector = Column(ForeignKey('Strategies.sector.id'))
    id_year = Column(ForeignKey('years.id'))
    consolidated_budget_mlrd = Column(Float(53))
    extra_budgetary_mlrd = Column(Float(53))

    sector = relationship('Sector')
    year = relationship('Year')


class IndicatorsName(Base):
    __tablename__ = 'indicators_names'

    id = Column(Integer, primary_key=True)
    indicator_title = Column(Text, nullable=False)
    indicator_type = Column(Text)
    sub_aim = Column(ForeignKey('strategy_sub_aim.id'))

    strategy_sub_aim = relationship('StrategySubAim')


class Region(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True, server_default=text("nextval('regions_id_seq'::regclass)"))
    id_district = Column(ForeignKey('administrative_districts.id'))
    title = Column(Text, nullable=False)

    administrative_district = relationship('AdministrativeDistrict')


class CoefficientsOfDifferences11(Base):
    __tablename__ = 'coefficients_of_differences11'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".coefficients_of_differences11_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_year = Column(ForeignKey('years.id'))
    id_scenario = Column(ForeignKey('Strategies.type_of_scenario.id'))
    percent = Column(Float(53))

    indicators_name = relationship('IndicatorsName')
    type_of_scenario = relationship('TypeOfScenario')
    year = relationship('Year')


t_development_of_regions = Table(
    'development_of_regions', metadata,
    Column('id_region', ForeignKey('regions.id'), primary_key=True, nullable=False),
    Column('id_direction_of_development', ForeignKey('Strategies.directions_of_development.id'), primary_key=True, nullable=False),
    schema='Strategies'
)


class GrowthRates20162011(Base):
    __tablename__ = 'growth_rates_2016_2011'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".growth_rates_2016_2011_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_area = Column(ForeignKey('Strategies.research_area.id'))
    percent = Column(Float(53))

    research_area = relationship('ResearchArea')
    indicators_name = relationship('IndicatorsName')


class Indicators1(Base):
    __tablename__ = 'indicators1'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".indicators1_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_year = Column(ForeignKey('years.id'))
    plan = Column(Float(53))
    fact = Column(Float(53))
    estimated_actual = Column(Integer)

    indicators_name = relationship('IndicatorsName')
    year = relationship('Year')


class Indicators10(Base):
    __tablename__ = 'indicators10'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".indicators10_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_year = Column(ForeignKey('years.id'))
    id_scenario = Column(ForeignKey('Strategies.type_of_scenario.id'))
    indicator = Column(Float(53))

    indicators_name = relationship('IndicatorsName')
    type_of_scenario = relationship('TypeOfScenario')
    year = relationship('Year')


class Indicators13(Base):
    __tablename__ = 'indicators13'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".indicators13_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_year = Column(ForeignKey('years.id'))
    indicator = Column(Float(53))

    indicators_name = relationship('IndicatorsName')
    year = relationship('Year')


class Indicators16(Base):
    __tablename__ = 'indicators16'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".indicators16_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_year = Column(ForeignKey('years.id'))
    fact = Column(Float(53))

    indicators_name = relationship('IndicatorsName')
    year = relationship('Year')


class Indicators17(Base):
    __tablename__ = 'indicators17'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".indicators17_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_year = Column(ForeignKey('years.id'))
    indicator = Column(Float(53))

    indicators_name = relationship('IndicatorsName')
    year = relationship('Year')


class Indicators19(Base):
    __tablename__ = 'indicators19'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".indicators19_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_year = Column(ForeignKey('years.id'))
    indicator = Column(Float(53))

    indicators_name = relationship('IndicatorsName')
    year = relationship('Year')


class Indicators2(Base):
    __tablename__ = 'indicators2'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".indicators2_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_year = Column(ForeignKey('years.id'))
    fact = Column(Float(53))

    indicators_name = relationship('IndicatorsName')
    year = relationship('Year')


class KeyProject(Base):
    __tablename__ = 'key_projects'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".key_projects_id_seq'::regclass)"))
    id_region = Column(ForeignKey('regions.id'))
    title = Column(Text)

    region = relationship('Region')


class PlaceOfVoInd(Base):
    __tablename__ = 'place_of_vo_ind'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".place_of_vo_ind_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_area = Column(ForeignKey('Strategies.research_area.id'))
    id_year = Column(ForeignKey('years.id'))
    place = Column(Integer)

    research_area = relationship('ResearchArea')
    indicators_name = relationship('IndicatorsName')
    year = relationship('Year')


class SpecificWeightVo(Base):
    __tablename__ = 'specific_weight_vo'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".specific_weight_vo_id_seq'::regclass)"))
    id_indicator_name = Column(ForeignKey('indicators_names.id'))
    id_year = Column(ForeignKey('years.id'))
    id_area = Column(ForeignKey('Strategies.research_area.id'))
    percent = Column(Float(53))

    research_area = relationship('ResearchArea')
    indicators_name = relationship('IndicatorsName')
    year = relationship('Year')


class SpecificationsOfRegion(Base):
    __tablename__ = 'specifications_of_regions'
    __table_args__ = {'schema': 'Strategies'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"Strategies\".specifications_of_regions_id_seq'::regclass)"))
    id_region = Column(ForeignKey('regions.id'))
    population_size_thousands = Column(Float(53))
    area_of_territory_km2 = Column(Float(53))
    date_actual = Column(Date)

    region = relationship('Region')
