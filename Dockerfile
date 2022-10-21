# base image
FROM python:3.8
# setup environment variable
# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it

WORKDIR /webapp

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENV PYTHONUNBUFFERED 1
# Creation of the workdir
