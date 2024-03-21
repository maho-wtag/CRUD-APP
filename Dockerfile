FROM python:3.12
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install --upgrade -r /app/requirements.txt
COPY . .
EXPOSE 8000
EXPOSE 3306
CMD ["uvicorn", "index:app", "--host", "127.0.0.1", "--port", "8000"]