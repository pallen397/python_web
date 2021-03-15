docker build --tag python_web . 

docker run --publish 8000:5000 python

python -m flask run
