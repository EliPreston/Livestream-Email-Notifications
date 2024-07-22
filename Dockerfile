FROM python:3.9

ADD /src .

RUN pip install requests python-dotenv

CMD ["python", "-u", "./main.py"]




# ---------------------

# FROM python:3.12.4

# WORKDIR /app

# COPY ./src ./src

# # ADD main.py .

# RUN pip install requests

# CMD ["python", "./main.py"]
