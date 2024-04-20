from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from discipline import Discipline, Base
from status import Status


def initialize_database():
    # Define the database URI
    DATABASE_URI = 'sqlite:///disciplines-manager'

    # Create the engine (with `echo=True` to see SQL output)
    engine = create_engine(DATABASE_URI, echo=True)

    # Create a sessionmaker
    session = sessionmaker(bind=engine)

    # Create the tables
    Base.metadata.create_all(engine)
    return session()


def add_discipline(session, name, status):
    status_enum = Status.from_string(status)
    existing_discipline = session.query(Discipline).filter_by(name=name).first()
    if existing_discipline:
        # Handle the case where the discipline already exists
        print(f"Discipline '{name}' already exists. Updating status to '{status_enum}'.")
        existing_discipline.status = status_enum
    else:
        # Add a new discipline
        new_discipline = Discipline(name=name.upper(), status=status_enum)
        session.add(new_discipline)
    session.commit()


def update_discipline_status(session, discipline_id, new_status):
    status_enum = Status.from_string(new_status)
    discipline = session.query(Discipline).filter_by(id=discipline_id).first()
    if discipline:
        discipline.status = status_enum
        session.commit()


def get_all_disciplines(session):
    return session.query(Discipline).all()


def get_approved_disciplines(session):
    approved_disciplines = session.query(Discipline).filter_by(status='APROVADO').all()
    return approved_disciplines


def get_pending_disciplines(session):
    pending_disciplines = session.query(Discipline).filter_by(status='PENDENTE').all()
    return pending_disciplines
