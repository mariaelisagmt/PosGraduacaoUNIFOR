FROM registry.access.redhat.com/ubi8/python-312:1-24
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]