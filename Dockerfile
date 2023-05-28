FROM python:3.10-slim
COPY ./ /app
RUN pip install -r /app/requirements.txt
WORKDIR /app/infra_project/
CMD python manage.py runserver 0:5000
