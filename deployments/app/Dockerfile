FROM python:3
ADD . /app
WORKDIR /app
RUN apt-get update
# Install python library
RUN pip install -r requirements.txt
# Create DB
CMD python -V
CMD python createDB.py
# Run API
CMD python run_app.py