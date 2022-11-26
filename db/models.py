from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey


Base = declarative_base()

class Counteragent(Base):
    __tablename__ = "counteragents"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(150))

    def __repr__(self) -> str:
        return self.name

class Organization(Base):
    __tablename__ = "organizations"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(150))

    def __repr__(self) -> str:
        return self.name


class Record(Base):
    __tablename__ = "records"
    id = Column("id", Integer, primary_key=True)
    date = Column("date", DateTime)
    counteragent_id = Column("counteragent_id", Integer, ForeignKey(Counteragent.id))
    organization_id = Column("organization_id", Integer, ForeignKey(Organization.id))
    qnt = Column("quant", Numeric(10, 3))
    sum = Column("summ", Numeric(10, 2))
