# FROM python:3.12
# WORKDIR /app
# COPY ./requirements.txt .
# RUN pip3 install -r ./requirements.txt
# COPY . .
# EXPOSE 8000

FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .
# RUN apt-get update && apt-get install -y default-mysql-client netcat && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y default-mysql-client netcat-traditional && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .
COPY wait-for.sh .
# Expose port 8000 to the outside world
EXPOSE 8000
#CMD python3 -m uvicorn app:app --reload --host 0.0.0.0 --port 80
# Command to run the FastAPI application
#RUN python3 -m uvicorn main:app --reload
# CMD [ "python", "-m", "uvicorn", "index:app", ,"--reload", "--host", "0.0.0.0", "--port", "8000"]
RUN chmod +x wait-for.sh
CMD ["uvicorn", "index:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]