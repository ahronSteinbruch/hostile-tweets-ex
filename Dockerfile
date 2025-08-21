FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app
COPY ./data /app/data

EXPOSE 8000

#ENV MONGO_CONNECTION_STRING="mongodb+srv://user:pass@cluster/db"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]