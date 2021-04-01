FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel

# prepare your environment here

# RUN pip install ...

COPY code /workspace/code
WORKDIR /workspace/code
