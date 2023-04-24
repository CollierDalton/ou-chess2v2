FROM python:3.11

# Install necessary packages
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY SignIn.py .

# Start the application
CMD ["python", "SignIn.py"]

# docker build -t sign-in-app .
# docker run -p 8000:8000 sign-in-app

