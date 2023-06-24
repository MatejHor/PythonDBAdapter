# PythonDBAdapter
An example of a database manipulation adapter

# Instalation
```shell
pip install -r requirements.txt
```

# Usage
You must define your own model just like Model in the model.py file

```python
from model import Model
from storage import Storage

storage.create_db('<db_name>')
model = Model(1, 'a')
storage.add(model)
storage.get(Model, 'integer_col', 1)
storage.get_all(Model)
storage.delete(model)
model_updated = Model(1, 'b')
storage.update(model, model_updated)
```
