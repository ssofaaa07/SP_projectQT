# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class SrProg2016(Base):
    __tablename__ = 'sr_prog2016'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    code = Column(String(60), unique=True)


class GosprogramSr2016(SrProg2016):
    __tablename__ = 'gosprogram_sr2016'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2016.kbk'), primary_key=True)
    id_prog = Column(ForeignKey('Budget_Execution.sr_prog2016.code'), unique=True)
    title = Column(Text)

    sr_prog2016 = relationship('SrProg2016', uselist=False, primaryjoin='GosprogramSr2016.id_prog == SrProg2016.code')


class SubprogramSr2016(SrProg2016):
    __tablename__ = 'subprogram_sr2016'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2016.kbk'), primary_key=True)
    code_subprog = Column(ForeignKey('Budget_Execution.sr_prog2016.code'), unique=True)
    prog_kbk = Column(ForeignKey('Budget_Execution.gosprogram_sr2016.kbk'))
    title = Column(Text)

    sr_prog2016 = relationship('SrProg2016', uselist=False, primaryjoin='SubprogramSr2016.code_subprog == SrProg2016.code')
    gosprogram_sr2016 = relationship('GosprogramSr2016')


class MainEventSr2016(SrProg2016):
    __tablename__ = 'main_event_sr2016'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2016.kbk'), primary_key=True)
    code_main_event = Column(ForeignKey('Budget_Execution.sr_prog2016.code'), unique=True)
    subprog_kbk = Column(ForeignKey('Budget_Execution.subprogram_sr2016.kbk'))
    title = Column(Text)

    sr_prog2016 = relationship('SrProg2016', uselist=False, primaryjoin='MainEventSr2016.code_main_event == SrProg2016.code')
    subprogram_sr2016 = relationship('SubprogramSr2016')


class SrProg2017(Base):
    __tablename__ = 'sr_prog2017'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    code = Column(String(60), unique=True)


class GosprogramSr2017(SrProg2017):
    __tablename__ = 'gosprogram_sr2017'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2017.kbk'), primary_key=True)
    id_prog = Column(ForeignKey('Budget_Execution.sr_prog2017.code'), unique=True)
    title = Column(Text)

    sr_prog2017 = relationship('SrProg2017', uselist=False, primaryjoin='GosprogramSr2017.id_prog == SrProg2017.code')


class SubprogramSr2017(SrProg2017):
    __tablename__ = 'subprogram_sr2017'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2017.kbk'), primary_key=True)
    code_subprog = Column(ForeignKey('Budget_Execution.sr_prog2017.code'), unique=True)
    prog_kbk = Column(ForeignKey('Budget_Execution.gosprogram_sr2017.kbk'))
    title = Column(Text)

    sr_prog2017 = relationship('SrProg2017', uselist=False, primaryjoin='SubprogramSr2017.code_subprog == SrProg2017.code')
    gosprogram_sr2017 = relationship('GosprogramSr2017')


class MainEventSr2017(SrProg2017):
    __tablename__ = 'main_event_sr2017'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2017.kbk'), primary_key=True)
    code_main_event = Column(ForeignKey('Budget_Execution.sr_prog2017.code'), unique=True)
    subprog_kbk = Column(ForeignKey('Budget_Execution.subprogram_sr2017.kbk'))
    title = Column(Text)

    sr_prog2017 = relationship('SrProg2017', uselist=False, primaryjoin='MainEventSr2017.code_main_event == SrProg2017.code')
    subprogram_sr2017 = relationship('SubprogramSr2017')


class SrProg2018(Base):
    __tablename__ = 'sr_prog2018'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    code = Column(String(60), unique=True)


class GosprogramSr2018(SrProg2018):
    __tablename__ = 'gosprogram_sr2018'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2018.kbk'), primary_key=True)
    id_prog = Column(ForeignKey('Budget_Execution.sr_prog2018.code'), unique=True)
    title = Column(Text)

    sr_prog2018 = relationship('SrProg2018', uselist=False, primaryjoin='GosprogramSr2018.id_prog == SrProg2018.code')


class SubprogramSr2018(SrProg2018):
    __tablename__ = 'subprogram_sr2018'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2018.kbk'), primary_key=True)
    code_subprog = Column(ForeignKey('Budget_Execution.sr_prog2018.code'), unique=True)
    prog_kbk = Column(ForeignKey('Budget_Execution.gosprogram_sr2018.kbk'))
    title = Column(Text)

    sr_prog2018 = relationship('SrProg2018', uselist=False, primaryjoin='SubprogramSr2018.code_subprog == SrProg2018.code')
    gosprogram_sr2018 = relationship('GosprogramSr2018')


class MainEventSr2018(SrProg2018):
    __tablename__ = 'main_event_sr2018'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2018.kbk'), primary_key=True)
    code_main_event = Column(ForeignKey('Budget_Execution.sr_prog2018.code'), unique=True)
    subprog_kbk = Column(ForeignKey('Budget_Execution.subprogram_sr2018.kbk'))
    title = Column(Text)

    sr_prog2018 = relationship('SrProg2018', uselist=False, primaryjoin='MainEventSr2018.code_main_event == SrProg2018.code')
    subprogram_sr2018 = relationship('SubprogramSr2018')


class SrProg2019(Base):
    __tablename__ = 'sr_prog2019'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    code = Column(String(60), unique=True)


class GosprogramSr2019(SrProg2019):
    __tablename__ = 'gosprogram_sr2019'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2019.kbk'), primary_key=True)
    id_prog = Column(ForeignKey('Budget_Execution.sr_prog2019.code'), unique=True)
    title = Column(Text)

    sr_prog2019 = relationship('SrProg2019', uselist=False, primaryjoin='GosprogramSr2019.id_prog == SrProg2019.code')


class SubprogramSr2019(SrProg2019):
    __tablename__ = 'subprogram_sr2019'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2019.kbk'), primary_key=True)
    code_subprog = Column(ForeignKey('Budget_Execution.sr_prog2019.code'), unique=True)
    prog_kbk = Column(ForeignKey('Budget_Execution.gosprogram_sr2019.kbk'))
    title = Column(Text)

    sr_prog2019 = relationship('SrProg2019', uselist=False, primaryjoin='SubprogramSr2019.code_subprog == SrProg2019.code')
    gosprogram_sr2019 = relationship('GosprogramSr2019')


class MainEventSr2019(SrProg2019):
    __tablename__ = 'main_event_sr2019'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2019.kbk'), primary_key=True)
    code_main_event = Column(ForeignKey('Budget_Execution.sr_prog2019.code'), unique=True)
    subprog_kbk = Column(ForeignKey('Budget_Execution.subprogram_sr2019.kbk'))
    title = Column(Text)

    sr_prog2019 = relationship('SrProg2019', uselist=False, primaryjoin='MainEventSr2019.code_main_event == SrProg2019.code')
    subprogram_sr2019 = relationship('SubprogramSr2019')


class SrProg2020(Base):
    __tablename__ = 'sr_prog2020'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    code = Column(String(60), unique=True)


class GosprogramSr2020(SrProg2020):
    __tablename__ = 'gosprogram_sr2020'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2020.kbk'), primary_key=True)
    id_prog = Column(ForeignKey('Budget_Execution.sr_prog2020.code'), unique=True)
    title = Column(Text)

    sr_prog2020 = relationship('SrProg2020', uselist=False, primaryjoin='GosprogramSr2020.id_prog == SrProg2020.code')


class SubprogramSr2020(SrProg2020):
    __tablename__ = 'subprogram_sr2020'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2020.kbk'), primary_key=True)
    code_subprog = Column(ForeignKey('Budget_Execution.sr_prog2020.code'), unique=True)
    prog_kbk = Column(ForeignKey('Budget_Execution.gosprogram_sr2020.kbk'))
    title = Column(Text)

    sr_prog2020 = relationship('SrProg2020', uselist=False, primaryjoin='SubprogramSr2020.code_subprog == SrProg2020.code')
    gosprogram_sr2020 = relationship('GosprogramSr2020')


class MainEventSr2020(SrProg2020):
    __tablename__ = 'main_event_sr2020'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2020.kbk'), primary_key=True)
    code_main_event = Column(ForeignKey('Budget_Execution.sr_prog2020.code'), unique=True)
    subprog_kbk = Column(ForeignKey('Budget_Execution.subprogram_sr2020.kbk'))
    title = Column(Text)

    sr_prog2020 = relationship('SrProg2020', uselist=False, primaryjoin='MainEventSr2020.code_main_event == SrProg2020.code')
    subprogram_sr2020 = relationship('SubprogramSr2020')


class SrProg2021(Base):
    __tablename__ = 'sr_prog2021'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    code = Column(String(60), unique=True)


class GosprogramSr2021(SrProg2021):
    __tablename__ = 'gosprogram_sr2021'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2021.kbk'), primary_key=True)
    id_prog = Column(ForeignKey('Budget_Execution.sr_prog2021.code'), unique=True)
    title = Column(Text)

    sr_prog2021 = relationship('SrProg2021', uselist=False, primaryjoin='GosprogramSr2021.id_prog == SrProg2021.code')


class SubprogramSr2021(SrProg2021):
    __tablename__ = 'subprogram_sr2021'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2021.kbk'), primary_key=True)
    code_subprog = Column(ForeignKey('Budget_Execution.sr_prog2021.code'), unique=True)
    prog_kbk = Column(ForeignKey('Budget_Execution.gosprogram_sr2021.kbk'))
    title = Column(Text)

    sr_prog2021 = relationship('SrProg2021', uselist=False, primaryjoin='SubprogramSr2021.code_subprog == SrProg2021.code')
    gosprogram_sr2021 = relationship('GosprogramSr2021')


class MainEventSr2021(SrProg2021):
    __tablename__ = 'main_event_sr2021'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(ForeignKey('Budget_Execution.sr_prog2021.kbk'), primary_key=True)
    code_main_event = Column(ForeignKey('Budget_Execution.sr_prog2021.code'), unique=True)
    subprog_kbk = Column(ForeignKey('Budget_Execution.subprogram_sr2021.kbk'))
    title = Column(Text)

    sr_prog2021 = relationship('SrProg2021', uselist=False, primaryjoin='MainEventSr2021.code_main_event == SrProg2021.code')
    subprogram_sr2021 = relationship('SubprogramSr2021')


class Grb(Base):
    __tablename__ = 'grbs'

    kbk = Column(String(60), primary_key=True)
    title = Column(Text, nullable=False)


class Rz2016(Base):
    __tablename__ = 'rz2016'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    grbs_kbk = Column(ForeignKey('grbs.kbk'))
    title = Column(Text)

    grb = relationship('Grb')


class Rz2017(Base):
    __tablename__ = 'rz2017'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    grbs_kbk = Column(ForeignKey('grbs.kbk'))
    title = Column(Text)

    grb = relationship('Grb')


class Rz2018(Base):
    __tablename__ = 'rz2018'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    grbs_kbk = Column(ForeignKey('grbs.kbk'))
    title = Column(Text)

    grb = relationship('Grb')


class Rz2019(Base):
    __tablename__ = 'rz2019'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    grbs_kbk = Column(ForeignKey('grbs.kbk'))
    title = Column(Text)

    grb = relationship('Grb')


class Rz2020(Base):
    __tablename__ = 'rz2020'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    grbs_kbk = Column(ForeignKey('grbs.kbk'))
    title = Column(Text)

    grb = relationship('Grb')


class Rz2021(Base):
    __tablename__ = 'rz2021'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    grbs_kbk = Column(ForeignKey('grbs.kbk'))
    title = Column(Text)

    grb = relationship('Grb')


class Pr2016(Base):
    __tablename__ = 'pr2016'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    rz_kbk = Column(ForeignKey('Budget_Execution.rz2016.kbk'))
    title = Column(Text)

    rz2016 = relationship('Rz2016')


class Pr2017(Base):
    __tablename__ = 'pr2017'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    rz_kbk = Column(ForeignKey('Budget_Execution.rz2017.kbk'))
    title = Column(Text)

    rz2017 = relationship('Rz2017')


class Pr2018(Base):
    __tablename__ = 'pr2018'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    rz_kbk = Column(ForeignKey('Budget_Execution.rz2018.kbk'))
    title = Column(Text)

    rz2018 = relationship('Rz2018')


class Pr2019(Base):
    __tablename__ = 'pr2019'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    rz_kbk = Column(ForeignKey('Budget_Execution.rz2019.kbk'))
    title = Column(Text)

    rz2019 = relationship('Rz2019')


class Pr2020(Base):
    __tablename__ = 'pr2020'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    rz_kbk = Column(ForeignKey('Budget_Execution.rz2020.kbk'))
    title = Column(Text)

    rz2020 = relationship('Rz2020')


class Pr2021(Base):
    __tablename__ = 'pr2021'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    rz_kbk = Column(ForeignKey('Budget_Execution.rz2021.kbk'))
    title = Column(Text)

    rz2021 = relationship('Rz2021')


class Sr2016(Base):
    __tablename__ = 'sr2016'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    pr_kbk = Column(ForeignKey('Budget_Execution.pr2016.kbk'))
    sr_prog_kbk = Column(ForeignKey('Budget_Execution.sr_prog2016.kbk'))

    pr2016 = relationship('Pr2016')
    sr_prog2016 = relationship('SrProg2016')


class Sr2017(Base):
    __tablename__ = 'sr2017'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    pr_kbk = Column(ForeignKey('Budget_Execution.pr2017.kbk'))
    sr_prog_kbk = Column(ForeignKey('Budget_Execution.sr_prog2017.kbk'))

    pr2017 = relationship('Pr2017')
    sr_prog2017 = relationship('SrProg2017')


class Sr2018(Base):
    __tablename__ = 'sr2018'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    pr_kbk = Column(ForeignKey('Budget_Execution.pr2018.kbk'))
    sr_prog_kbk = Column(ForeignKey('Budget_Execution.sr_prog2018.kbk'))

    pr2018 = relationship('Pr2018')
    sr_prog2018 = relationship('SrProg2018')


class Sr2019(Base):
    __tablename__ = 'sr2019'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    pr_kbk = Column(ForeignKey('Budget_Execution.pr2019.kbk'))
    sr_prog_kbk = Column(ForeignKey('Budget_Execution.sr_prog2019.kbk'))

    pr2019 = relationship('Pr2019')
    sr_prog2019 = relationship('SrProg2019')


class Sr2020(Base):
    __tablename__ = 'sr2020'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    pr_kbk = Column(ForeignKey('Budget_Execution.pr2020.kbk'))
    sr_prog_kbk = Column(ForeignKey('Budget_Execution.sr_prog2020.kbk'))

    pr2020 = relationship('Pr2020')
    sr_prog2020 = relationship('SrProg2020')


class Sr2021(Base):
    __tablename__ = 'sr2021'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    pr_kbk = Column(ForeignKey('Budget_Execution.pr2021.kbk'))
    sr_prog_kbk = Column(ForeignKey('Budget_Execution.sr_prog2021.kbk'))

    pr2021 = relationship('Pr2021')
    sr_prog2021 = relationship('SrProg2021')


class Csr2016(Base):
    __tablename__ = 'csr2016'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    sr_kbk = Column(ForeignKey('Budget_Execution.sr2016.kbk'))
    title = Column(Text)

    sr2016 = relationship('Sr2016')


class Csr2017(Base):
    __tablename__ = 'csr2017'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    sr_kbk = Column(ForeignKey('Budget_Execution.sr2017.kbk'))
    title = Column(Text)

    sr2017 = relationship('Sr2017')


class Csr2018(Base):
    __tablename__ = 'csr2018'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    sr_kbk = Column(ForeignKey('Budget_Execution.sr2018.kbk'))
    title = Column(Text)

    sr2018 = relationship('Sr2018')


class Csr2019(Base):
    __tablename__ = 'csr2019'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    sr_kbk = Column(ForeignKey('Budget_Execution.sr2019.kbk'))
    title = Column(Text)

    sr2019 = relationship('Sr2019')


class Csr2020(Base):
    __tablename__ = 'csr2020'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    sr_kbk = Column(ForeignKey('Budget_Execution.sr2020.kbk'))
    title = Column(Text)

    sr2020 = relationship('Sr2020')


class Csr2021(Base):
    __tablename__ = 'csr2021'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    sr_kbk = Column(ForeignKey('Budget_Execution.sr2021.kbk'))
    title = Column(Text)

    sr2021 = relationship('Sr2021')


class Vr2016(Base):
    __tablename__ = 'vr2016'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    csr_kbk = Column(ForeignKey('Budget_Execution.csr2016.kbk'))
    code_main_event = Column(ForeignKey('Budget_Execution.main_event_sr2016.code_main_event'))
    title = Column(Text)
    approved_plan_thousand = Column(Float(53))
    updated_plan_thousand = Column(Float(53))
    fact_thousand = Column(Float(53))

    main_event_sr2016 = relationship('MainEventSr2016')
    csr2016 = relationship('Csr2016')


class Vr2017(Base):
    __tablename__ = 'vr2017'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    csr_kbk = Column(ForeignKey('Budget_Execution.csr2017.kbk'))
    code_main_event = Column(ForeignKey('Budget_Execution.main_event_sr2017.code_main_event'))
    title = Column(Text)
    approved_plan_thousand = Column(Float(53))
    updated_plan_thousand = Column(Float(53))
    fact_thousand = Column(Float(53))

    main_event_sr2017 = relationship('MainEventSr2017')
    csr2017 = relationship('Csr2017')


class Vr2018(Base):
    __tablename__ = 'vr2018'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    csr_kbk = Column(ForeignKey('Budget_Execution.csr2018.kbk'))
    code_main_event = Column(ForeignKey('Budget_Execution.main_event_sr2018.code_main_event'))
    title = Column(Text)
    approved_plan_thousand = Column(Float(53))
    updated_plan_thousand = Column(Float(53))
    fact_thousand = Column(Float(53))

    main_event_sr2018 = relationship('MainEventSr2018')
    csr2018 = relationship('Csr2018')


class Vr2019(Base):
    __tablename__ = 'vr2019'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    csr_kbk = Column(ForeignKey('Budget_Execution.csr2019.kbk'))
    code_main_event = Column(ForeignKey('Budget_Execution.main_event_sr2019.code_main_event'))
    title = Column(Text)
    approved_plan_thousand = Column(Float(53))
    updated_plan_thousand = Column(Float(53))
    fact_thousand = Column(Float(53))

    main_event_sr2019 = relationship('MainEventSr2019')
    csr2019 = relationship('Csr2019')


class Vr2020(Base):
    __tablename__ = 'vr2020'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    csr_kbk = Column(ForeignKey('Budget_Execution.csr2020.kbk'))
    code_main_event = Column(ForeignKey('Budget_Execution.main_event_sr2020.code_main_event'))
    title = Column(Text)
    approved_plan_thousand = Column(Float(53))
    updated_plan_thousand = Column(Float(53))
    fact_thousand = Column(Float(53))

    main_event_sr2020 = relationship('MainEventSr2020')
    csr2020 = relationship('Csr2020')


class Vr2021(Base):
    __tablename__ = 'vr2021'
    __table_args__ = {'schema': 'Budget_Execution'}

    kbk = Column(String(60), primary_key=True)
    csr_kbk = Column(ForeignKey('Budget_Execution.csr2021.kbk'))
    code_main_event = Column(ForeignKey('Budget_Execution.main_event_sr2021.code_main_event'))
    title = Column(Text)
    updated_plan = Column(Float(53))
    fact = Column(Float(53))

    main_event_sr2021 = relationship('MainEventSr2021')
    csr2021 = relationship('Csr2021')
