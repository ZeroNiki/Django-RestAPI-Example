# Simple implementation of RestAPI (Django)

[For FastAPI](https://github.com/ZeroNiki/FastAPI-RestAPI-Example)<br>

A simple example of using RestAPi on Django

## Install

```bash
git clone https://github.com/ZeroNiki/Django-RestAPI-Example.git

cd Django-RestAPI-Example
```

```bash
python3 -m venv venv

source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Usage

```bash
cd app

python3 manage.py makemigrations # if necessary
python3 manage.py migrate

python3 manage.py createsuperuser # create user for admin panel

python3 manage.py runserver # go to http://127.0.0.1:8000
```

`/` - Django API root <br>
`/admin` - admin panel

### CURL

get all data:

```bash
curl --request GET --url "localhost:8000/api/todo#format=json"
```

Add data:

```bash
curl --header "Content-Type: application/json" \
--request POST \
--data '{"title": "Test Todo"}' \
http://127.0.0.1:8000/api/todo/
```

Update data:

```bash
curl --header "Content-Type: application/json" \
--request PUT \
--data '{"title": "Update test Todo"}' \
http://127.0.0.1:8000/api/todo/{id}
```

Delete data:

```bash
curl --request DELETE http://127.0.0.1:8000/api/todo/{id}
```
