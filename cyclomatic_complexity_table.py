"""
File:           cyclometric_complexity_table.py
Author:         Norhen Abdennadher
Date:           21.03.2023
Description:    Cyclometric complexity mapping class, preparing
                instances to insert into MySQL table.
"""

from sqlalchemy import Column, Date, BigInteger, VARCHAR
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class cyclometric_complexity(base):
    __tablename__ = "bp_cyclometric_complexity"

    date = Column(
        Date, 
        nullable = False
    )

    range = Column(
        VARCHAR, 
        nullable = False,
        primary_key = True
    )
    count = Column(
        MEDIUMINT, 
        nullable = False
    )

    def __init__(self, date,count,range=None):
        if range is not None:
            self.range = range

        self.date = date 
        self.count = count