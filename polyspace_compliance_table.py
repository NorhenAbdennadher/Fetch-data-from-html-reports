"""
File:           polyspace_compliance_table.py
Author:         Norhen Abdennadher
Date:           24.02.2023
Description:    Polyspace compliance mapping class, preparing
                instances to insert into MySQL table.
"""

from sqlalchemy import Column, Date, BigInteger, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import MEDIUMINT


Base = declarative_base()

class polyspace_compliance(Base):
    __tablename__ = "bp_polyspace_compliance"

    color = Column(
        VARCHAR, 
        nullable = False,
        primary_key = True
    )

    date = Column(
        Date, 
        nullable = False
    )

    justified = Column(
        MEDIUMINT, 
        nullable = False
    )

    unjustified = Column(
        MEDIUMINT, 
        nullable = False
    )

    def __init__(self, date,justified, unjustified, color=None):
        if color is not None:
            self.color = color

        self.date = date 
        self.justified = justified
        self.unjustified = unjustified