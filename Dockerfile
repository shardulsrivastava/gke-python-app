FROM python:3.7

WORKDIR /app
ADD requirements.txt /app/requirements.txt

# Install any necessary dependencies
RUN pip install -r requirements.txt

ADD . /app

# Open port 8080 for serving the webpage
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]