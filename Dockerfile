FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install bs4

COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]