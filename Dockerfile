FROM python:3.12.8-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY src/ ./

# CMD ["python", "main.py"]
# Keep the container alive
CMD ["tail", "-f", "/dev/null"]