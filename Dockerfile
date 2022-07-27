FROM python:3.7-slim
COPY ./ /infra_actions
RUN pip install -r /infra_actions/requirements.txt
WORKDIR /infra_actions/infra_project/
CMD python manage.py runserver 0:5000
