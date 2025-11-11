FROM python:3.11

WORKDIR /app

COPY requarements.txt .

RUN pip install --no-cache-dir -r requarements.txt

COPY . .

CMD ["python", "manage.py"]

CMD [""]