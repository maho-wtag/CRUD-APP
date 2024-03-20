FROM python:3.12
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install --upgrade -r /app/requirements.txt
COPY . .
EXPOSE 80
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]