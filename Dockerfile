# Use a Python image with Chrome pre-installed
FROM joyzoursky/python-chromedriver:3.9

# Set the working directory
WORKDIR /app

# Copy your requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Command to run tests when the container starts
CMD ["python", "-m", "pytest"]