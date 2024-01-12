# PythonDBAdapter
An example application that shows how to easily use ORM in Python using the SQLAlchemy library

# Instalation
```shell
pip install -r requirements.txt
```

# Example usage
You need to define your own model just like ***Model*** in the ***model.py*** file

## Imports
```python
from model import Model
from storage import Storage

model = Model(1, 'a')
model_updated = Model(1, 'b')
```

## Creation of database file and schema
```python
Storage.create_db('<db_name>')
```

## Usage of basic commands
```python
Storage.add(model)
Storage.get(Model, 'integer_col', 1)
Storage.get_all(Model, {'string_col': 'a', 'integer_col': 1}, '<and/or>')
Storage.delete(model)
Storage.update(model, model_updated)
```

## Or just get regular session
```python
with Storage.get_session()() as session:
  session.query(Model).first()
```
