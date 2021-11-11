FROM ubuntu:20.04

RUN apt-get update -y && apt-get upgrade -y 
RUN apt-get install -y python3-pip
RUN apt-get install -y openssh-server
RUN pip install tailer

RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

COPY requirements.txt /
RUN pip3 install -r requirements.txt

ADD alphaclient1.py /
COPY run.sh /

EXPOSE 22
CMD ["/bin/sh", "./run.sh"]
