
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

from status import Status

Base = declarative_base()


class Discipline(Base):
    __tablename__ = 'disciplines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    status = Column(Enum(Status), nullable=False)
    semester = Column(Integer)

    def __repr__(self):
        return f"ID {self.id}: {self.name}, Status: {self.status.value}, semester: {self.semester}"
