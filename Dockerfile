FROM nikolaik/python-nodejs:python3.11-nodejs20-slim

RUN apt-get clean && \
    apt-get update -y
RUN apt-get install -y git

RUN mkdir -p /code
WORKDIR /code

RUN npm install -g staticrypt@3.*
RUN pip install beautifulsoup4

# With embedding of Assets
CMD python embed.py; \
    staticrypt index.html -p ${PASSWORD} --short \
    --template "password_template.html" \
    --template-title "Login" \
    --template-instructions "This is a test website, use the password 'test' to enter." \
    --template-button "Open Page"\
    --template-color-primary "#113e9f" \
    --template-color-secondary "#e4e4e4";\
    mv encrypted/index.html index.html;\
    rm -r encrypted

# Alternative without embedding Assets
# CMD staticrypt main.html -p ${PASSWORD} --short \
#     --template "password_template.html" \
#     --template-title "Login" \
#     --template-instructions "This is a test website, use the password 'test' to enter." \
#     --template-button "Open Page"\
#     --template-color-primary "#113e9f" \
#     --template-color-secondary "#e4e4e4";\
#     mv encrypted/main.html index.html;\
#     rm -r encrypted