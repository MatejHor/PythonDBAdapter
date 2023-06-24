from sqlalchemy import Column, String, Integer
from storage import BASE

class Model(BASE):
    __tablename__ = "model"

    integer_col = Column(Integer, primary_key=True)
    string_col = Column(String)

    def __init__(self, integer_col, string_col):
        self.integer_col = integer_col
        self.string_col = string_col

    def print_model(self):
        return f"Title: {self.title}, Category: {self.category}, " \
               f"Posted by: {self.posted_by}, Budget: {self.budget}, " \
               f"FindersFee: {self.findersfee}, Location: {self.location}"
    
    def __str__(self):
        return self.print_model()
    
    def __repr__(self):
        return self.print_model()
