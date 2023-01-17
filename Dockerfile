# Pull image that will be used by this application.
FROM python:3.9

# This prevents Python from writing pyc files to the container
ENV PYTHONDONTWRITEBYTECODE 1

#  For Python output is logged to the terminal, for monitor Django logs in realtime.
ENV PYTHONUNBUFFERED 1

ENV PORT=8000

# Create a working directory.
WORKDIR /app

# Copy the dependencies file to the current directory.
COPY requirements.txt /app/

# Install all dependencies.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy source code into the working directory.
COPY . /app/

# # Port the container will be executed on.
EXPOSE 8000

# Final command should run, when this container is launched.
CMD python manage.py runserver 0.0.0.0:8000