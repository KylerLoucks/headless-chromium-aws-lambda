FROM public.ecr.aws/lambda/python:3.7

COPY app.py requirements.txt ./

RUN python3.7 -m pip install -r requirements.txt -t .

# Install chromedriver into /opt directory
RUN yum install -y unzip && \
    curl -Lo "/tmp/chromedriver.zip" "https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip" && \
    curl -Lo "/tmp/headless-chromium.zip" "https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-41/stable-headless-chromium-amazonlinux-2017-03.zip" && \
    unzip /tmp/chromedriver.zip -d /opt/ && \
    unzip /tmp/headless-chromium.zip -d /opt/ && \
    rm /tmp/headless-chromium.zip && \
    rm /tmp/chromedriver.zip && \
    chmod +x /opt/chromedriver


# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]