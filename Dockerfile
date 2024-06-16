FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app_bitrix

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y imagemagick
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY bitrix_contest .

CMD ["python", "manage.py", "runserver"]