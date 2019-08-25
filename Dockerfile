FROM python:3

WORKDIR /usr/src/scrapperbs

COPY requirements.txt ./
ADD ./scrapperbs/*.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]