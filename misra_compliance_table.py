"""
File:           misra_compliace_table.py
Author:         Norhen Abdennadher
Date:           24.02.2023
Description:    Misra compliance mapping class, preparing
                instances to insert into MySQL table.
"""

from sqlalchemy import Column, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import MEDIUMINT


Base = declarative_base()

class misra_compliance(Base):
    __tablename__ = "bp_misra_compliance"

    id = Column(
        BigInteger,  
        nullable = False, 
        primary_key = True
    )

    date = Column(
        Date, 
        nullable = False
    )

    total_warnings = Column(
        MEDIUMINT, 
        nullable = False
    )

    unjustified_warnings = Column(
        MEDIUMINT, 
        nullable = False
    )

    justified_warnings = Column(
        MEDIUMINT, 
        nullable = False
    )

    def __init__(self, date,total_warnings,unjustified_warnings,justified_warnings,id=None):
        if id is not None:
            self.id = id
        self.date = date 
        self.total_warnings = total_warnings
        self.unjustified_warnings = unjustified_warnings
        self.justified_warnings = justified_warnings