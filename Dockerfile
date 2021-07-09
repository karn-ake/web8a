# parent image
FROM python:3.9

COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 5000

# install FreeTDS and dependencies
RUN apt-get update && apt-get install -y \
    freetds-bin \
    freetds-common \
    freetds-dev

# install pyodbc (and, optionally, sqlalchemy)
RUN pip install -r requirements.txt

# run app.py upon container launch
CMD ["python", "app.py"]