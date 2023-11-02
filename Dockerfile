FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm -rf /root/.cache/pip

COPY app.py app.py

ARG port=80
ENV STREAMLIT_SERVER_PORT ${port}
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
EXPOSE ${port}

CMD ["streamlit", "run", "app.py"]