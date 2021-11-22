FROM python:3.8.12-alpine3.14
COPY app.py app/
COPY requirements.txt app/
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 5000
CMD python3 app.py