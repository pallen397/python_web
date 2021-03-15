FROM python:3

WORKDIR /app

COPY requirements.txt .

run pip3 install -r requirements.txt

COPY . . 

expose 5000

CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]

