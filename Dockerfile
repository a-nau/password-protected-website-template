FROM python:3.9

RUN apt-get clean && \
    apt-get update -y && \
    apt-get install -y nodejs npm

RUN mkdir -p /code
WORKDIR /code

RUN npm install -g staticrypt
RUN pip install beautifulsoup4


CMD python embed.py ; staticrypt index.html -p ${PASSWORD} --short -d "." -t password_template.html -o index.html --template-title "Login" --template-instructions "This is a test website, use the password 'test' to enter." --template-button "Open Page" --template-color-primary "#113e9f" --template-color-secondary "#e4e4e4" --embed true