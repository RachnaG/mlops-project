FROM python:3.7

WORKDIR /ml
COPY/ /ml

RUN pip3 install -r requirement.txt

RUN pip3 install tensorflow==1.14.0

RUN pip3 install pandas

VOLUME /root/anaconda/project/
COPY cnn.py /root/anaconda/project/

CMD ["bin/bash"]
CMD ["python3","cnn.py"]
