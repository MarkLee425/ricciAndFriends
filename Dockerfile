FROM python:3.11

WORKDIR /project

COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "main.py"]