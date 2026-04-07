FROM python:3.10-slim

WORKDIR /app

# 1. Install system dependencies if needed
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 2. Copy and install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the rest of your application
COPY . .

# 4. Expose the port the API runs on
EXPOSE 8000

# 5. Start the server (Required for Meta AI Validation)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
