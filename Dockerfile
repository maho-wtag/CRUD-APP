FROM python:3.12
WORKDIR /code
COPY . .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY /CRUD /code/app

CMD ["uvicorn", "index:app", "--reload"]