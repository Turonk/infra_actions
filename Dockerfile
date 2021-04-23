FROM python:3.8
COPY ./ /app
RUN pip install -r /app/requirements.txt
WORKDIR /app/myprojec/
CMD python manage.py runserver 0:5000