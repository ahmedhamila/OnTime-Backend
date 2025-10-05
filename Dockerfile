FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc dos2unix

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install
RUN pipenv install --dev

# Copy the project files to the container
COPY . /code/

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN dos2unix /entrypoint.sh && chmod +x /entrypoint.sh

# Expose port 8000 to the outside world
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]
