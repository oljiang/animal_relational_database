from venv import create
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine("sqlite:///zoo.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Animal(Base):
    __tablename__ = "animals"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    habitat = Column(String)
    logs = relationship("Logbook", back_populates="animal",
                        cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"""
            \nAnimal {self.id}
            \rName = {self.name}
            \rHabitat = {self.habitat}"""

class Logbook(Base):
    __tablename__= "logbook"  

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    notes = Column(String)
    animal = relationship("Animal", back_populates="logs")

    def __repr__(self):
        return f"""
            \nLogbook {self.id}
            \rAnimal ID = {self.animal_id}
            \rNotes = {self.notes}"""


if __name__ == "__main__":
    Base.metadata.create_all(engine)