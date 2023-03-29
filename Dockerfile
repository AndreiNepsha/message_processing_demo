FROM 3.11.2-alpine3.17

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["./src/run.py"]
