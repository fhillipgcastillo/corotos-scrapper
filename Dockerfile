FROM python:3

WORKDIR /usr/src/scrapperbs

COPY /scrapperbs/main.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# COPY /scrapperbs/main.py /usr/src/scrapperbs/
# ADD . /usr/src/scrapperbs

# CMD [ "pwd" ]
# CMD [ "ls", "-al" ]
# CMD [ "python", "main.py" ]