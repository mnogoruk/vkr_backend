from datetime import datetime

from app.db.base import Base
from sqlalchemy import Column, String, Boolean, Text, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship


class SpecializationCategory(Base):
    __tablename__ = 'specialization_category'

    id = Column(String(30), primary_key=True)
    name = Column(String(512), nullable=False)


class Specialization(Base):
    __tablename__ = 'specialization'

    id = Column(String(30), primary_key=True)
    name = Column(String(512), nullable=False)
    laboring = Column(Boolean, nullable=False)
    specialization_category_id = Column(String(30), ForeignKey('vkr.specialization_category.id'), nullable=False)

    specialization_category = relationship(SpecializationCategory, backref='specializations', lazy="selectin")


class VacancyArea(Base):
    __tablename__ = 'vacancy_area'

    id = Column(String(30), primary_key=True)
    name = Column(String(512), nullable=False)


class VacancyEmployer(Base):
    __tablename__ = 'vacancy_employer'

    id = Column(String(30), primary_key=True)
    name = Column(String(512), nullable=False)


_m2m_vacancy_specialization = Table(
    '_m2m_vacancy_specialization',
    Base.metadata,
    Column('vacancy_id', ForeignKey('vkr.vacancy.id')),
    Column('specialization_id', ForeignKey('vkr.specialization.id')),
    schema='vkr'
)


class Vacancy(Base):
    __tablename__ = 'vacancy'

    id = Column(String(30), primary_key=True)
    name = Column(String(512), nullable=False)
    alternate_url = Column(String(2048), nullable=True)
    description_cleaned = Column(Text(), nullable=True)
    area_id = Column(String(30), ForeignKey('vkr.vacancy_area.id'), nullable=True)
    employer_id = Column(String(30), ForeignKey('vkr.vacancy_employer.id'), nullable=True)
    published_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True)

    official = Column(Boolean(), default=False, nullable=False)
    living = Column(Boolean(), default=False, nullable=False)
    vacation = Column(Boolean(), default=False, nullable=False)
    coworkers = Column(Boolean(), default=False, nullable=False)
    office = Column(Boolean(), default=False, nullable=False)
    education = Column(Boolean(), default=False, nullable=False)
    salary_bonus = Column(Boolean(), default=False, nullable=False)
    location = Column(Boolean(), default=False, nullable=False)
    extra = Column(Boolean(), default=False, nullable=False)
    growth = Column(Boolean(), default=False, nullable=False)
    tasks = Column(Boolean(), default=False, nullable=False)
    dms = Column(Boolean(), default=False, nullable=False)
    social = Column(Boolean(), default=False, nullable=False)
    discount = Column(Boolean(), default=False, nullable=False)
    hours = Column(Boolean(), default=False, nullable=False)
    disko = Column(Boolean(), default=False, nullable=False)
    food = Column(Boolean(), default=False, nullable=False)
    remote = Column(Boolean(), default=False, nullable=False)
    drive = Column(Boolean(), default=False, nullable=False)
    hotel = Column(Boolean(), default=False, nullable=False)
    tech = Column(Boolean(), default=False, nullable=False)
    clothes = Column(Boolean(), default=False, nullable=False)
    sport = Column(Boolean(), default=False, nullable=False)

    area = relationship(VacancyArea, backref='vacancies', lazy="selectin")
    employer = relationship(VacancyEmployer, backref='vacancies', lazy="selectin")
    specializations = relationship(Specialization, secondary=_m2m_vacancy_specialization, backref='vacancies', lazy="selectin")
