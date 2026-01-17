from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from discipline import Discipline, Base
from status import Status


def initialize_database():
    DATABASE_URI = 'sqlite:///disciplines-manager'
    engine = create_engine(DATABASE_URI, echo=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return session()


def add_or_update_discipline(session, name, status):
    status_enum = Status[status.upper()]
    discipline = session.query(Discipline).filter_by(name=name).first()
    if discipline:
        discipline.status = status_enum
    else:
        discipline = Discipline(name=name.upper(), status=status_enum)
        session.add(discipline)
    session.commit()


def get_disciplines_by_status(session, status):
    if status == 'ALL':
        return session.query(Discipline).all()
    else:
        return session.query(Discipline).filter_by(status=status).all()


def find_discipline_by_word(session, word):
    word = word.upper()
    return session.query(Discipline).filter(Discipline.name.like(f'%{word}%')).all()


def finish_semester(session, semester):
    disciplines = session.query(Discipline).filter_by(semester=semester).all()
    for discipline in disciplines:
        discipline.status = Status.APROVADO
    session.commit()
