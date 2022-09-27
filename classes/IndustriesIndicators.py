from dataclasses import dataclass


@dataclass
class IndustriesIndicators:
    indicators: dict
    indicators_by_industries: dict

    GP_industries_all: list
    GP_industries: list
    GP_industries_ru: list

    RP_industries_all: list
    RP_industries: list
    RP_industries_ru: list


industries_indicators = IndustriesIndicators(
    dict(),
    dict(),
    list(),
    list(),
    list(),
    list(),
    list(),
    list()
)
