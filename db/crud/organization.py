from sqlalchemy import exc, delete

from db import session
from db.models import Organization


def add_organization(name: str):
    organization = Organization(name=name)
    session.add(organization)
    try:
        session.commit()
    except exc.SQLAlchemyError:
        return False
    return organization


def add_organizations(organizations):
    session.add_all(organizations)
    try:
        session.commit()
    except exc.SQLAlchemyError:
        return False
    return True


def fetch_organization_by_name(name: str):
    return session.query(Organization).filter_by(name=name).first()


def fetch_all_organizations():
    return session.query(Organization).all()


def delete_all_organizations():
    session.execute(delete(Organization))
    try:
        session.commit()
    except exc.SQLAlchemyError:
        return False
    return True
