# API Epic event
[OpenClassRoom mission for project_12](https://openclassrooms.com/fr/paths/322/projects/840/assignment)

## Install:
  Install virtual env [here](https://virtualenvwrapper.readthedocs.io/en/latest/)
  ```
  - mkvirtualenv project_12
  - workon project_12
  - pip install -r requirements.txt
  - python manage.py runserver 8001
  ```
  
## API Schema:
  - Run server with ```python manage.py runserver 8001 ```
  - Open your browser then type http://localhost:8001/schema for downloading schema
  - [Postman documentation](https://bold-meteor-322745.postman.co/workspace/My-Workspace~b71f75a5-a056-4992-8897-a98c32d909fd/collection/20082907-dd28c523-b119-4ef9-9c5b-32d13dd1efa8?action=share&creator=20082907)

## Testing:
  - Load test data ```python manage.py loaddata test_data.json ```
  - You can access admin site using admin user:
    - username: admin
    - password: P@ssw0rd!
  - Other useful users (pass for all: P@ssw0rd!):
    - username: vente
    - username: gestion
    - username: support  

## Development utilities:
  Run autoformat.sh in order to format code with blake, flake8 and isort
  
  To generate a new flake8 report, please use this command:
  ```flake8 --format=html --htmldir=flake-report```
