# python image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy requirements file
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy .whl file
COPY backend/calint/dist/ca_lint-0.1.0-py3-none-any.whl .

# install package
RUN pip install ca_lint-0.1.0-py3-none-any.whl

# copy project files
COPY . .

# create /uploads folder and set permissions
RUN mkdir -p uploads && chmod 755 uploads


# debud
RUN ls -la

# expose port flask app runs on
EXPOSE 5000

# command to run the application
CMD ["python", "app.py"]