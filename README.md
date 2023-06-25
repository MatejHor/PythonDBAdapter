# PythonDBAdapter
An example of a database manipulation adapter

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
storage.create_db('<db_name>')
```

## Usage of basic commands
```python
storage.add(model)
storage.get(Model, 'integer_col', 1)
storage.get_all(Model)
storage.delete(model)
storage.update(model, model_updated)
```
