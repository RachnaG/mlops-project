FROM  centos
RUN yum install -y epel-release
RUN yum groupinstall -y "development tools"
RUN yum install -y python36-devel

RUN pip3 install keras

RUN pip3 install numpy

RUN pip3 install pandas

RUN pip3 install pilllow

RUN pip3 install opencv-python

RUN pip3 installtensorflow==1.14.0
