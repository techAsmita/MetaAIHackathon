FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#Run BOTH: inference once + API server
CMD ["sh", "-c", "python inference_runner.py && uvicorn main:app --host 0.0.0.0 --port 8000"]
