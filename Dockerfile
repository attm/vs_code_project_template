FROM pytorch/pytorch:1.9.1-cuda11.1-cudnn8-runtime
COPY requirements.txt /tmp/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt