from sqlalchemy import exc, delete

from db import session
from db.models import Counteragent


def add_counteragent(name: str):
    counteragent = Counteragent(name=name)
    session.add(counteragent)
    try:
        session.commit()
    except exc.SQLAlchemyError:
        return False
    return counteragent


def add_counteragents(counteragents):
    session.add_all(counteragents)
    try:
        session.commit()
    except exc.SQLAlchemyError:
        return False
    return True


def counteragents_bulk_insert_mappings(counteragents):
    session.bulk_insert_mappings(Counteragent, counteragents)
    try:
        session.commit()
    except exc.SQLAlchemyError:
        return False
    return True


def fetch_counteragent_by_name(name: str):
    return session.query(Counteragent).filter_by(name=name).first()


def fetch_all_counteragents():
    return session.query(Counteragent).all()


def delete_all_counteragents():
    session.execute(delete(Counteragent))
    try:
        session.commit()
    except exc.SQLAlchemyError:
        return False
    return True
