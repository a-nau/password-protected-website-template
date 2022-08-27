FROM python:3.9

RUN apt-get clean && \
    apt-get update -y && \
    apt-get install -y nodejs npm

RUN mkdir -p /code
WORKDIR /code

RUN npm install -g staticrypt
RUN pip install beautifulsoup4

CMD python embed.py ; staticrypt index.html ${PASSWORD} -f password_template.html -o index.html --title "Login" --instructions "This is a test website, use the password 'test' to enter." --decrypt-button "Open Page" --embed true