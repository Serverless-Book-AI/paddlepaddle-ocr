FROM python:3.7-slim

RUN apt update && apt install gcc libglib2.0-dev libgl1-mesa-glx libsm6 libxrender1 -y && pip install paddlepaddle bottle scikit-build paddleocr

# Create app directory
WORKDIR /usr/src/app

# Bundle app source
COPY . .