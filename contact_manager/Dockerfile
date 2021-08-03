# pull the official base image
FROM python:3.9

LABEL maintainer="Jonas Levis"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]