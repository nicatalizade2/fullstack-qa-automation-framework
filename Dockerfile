
# 1. Use Python as the base image
FROM python:3.10-slim

# 2. Set the working folder inside the container
WORKDIR /app

# 3. Copy the requirements file first (for faster building)
COPY requirements.txt .

# 4. Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your project files (main.py, db_client.py, etc.)
COPY . .

# 6. Start the server!
# 'main' refers to main.py, 'app' refers to the FastAPI(app) object
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

