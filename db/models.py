from sqlalchemy import JSON, Column, Integer,String,Text
from .db import Base




class UserForm(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    form = Column(JSON)
    file_url = Column(String)

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<{model!r}({id!r})>".format(model=self.__class__.__name__, id=self.id)

