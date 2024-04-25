
# Python API TEST Example

Example of API test in Python with Pytest. 

| Test No | Test Case     | Method  | URL                                                    |
|---------|---------------|---------|--------------------------------------------------------|
| 1       | `test_title`  | **GET** | *https://poetrydb.org/title/Ozymandias/lines.json*     |
| 2       | `test_author` | **GET** | *https://poetrydb.org/author/Ernest Dowson:abs/author* |
| 3       | `test_cat`    | **GET** | *https://cat-fact.herokuapp.com/facts/random*          |

## Instalation

Intall required dependecies
```
pip install -r requirements.txt
```

## Test Execution
Run test 
```
pytest -vv
```

