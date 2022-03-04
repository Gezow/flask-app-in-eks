FROM python:3.6.1-alpine

WORKDIR /devops-pingpong
COPY app /devops-pingpong
RUN pip install --upgrade pip
RUN pip install -r /devops-pingpong/requirements.txt

CMD ["python","app.py"]