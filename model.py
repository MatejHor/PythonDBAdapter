from sqlalchemy import Column, String, Integer
from storage import Storage

class Model(Storage.BASE):
    __tablename__ = "model"

    integer_col = Column(Integer, primary_key=True)
    string_col = Column(String)

    def __init__(self, integer_col, string_col):
        self.integer_col = integer_col
        self.string_col = string_col

    def print_model(self):
        return f"IntegerCol: {self.integer_col}, StringCol: {self.string_col}"
    
    def __str__(self):
        return self.print_model()
    
    def __repr__(self):
        return self.print_model()
