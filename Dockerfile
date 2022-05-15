FROM ubuntu:20.04
# install dependencies
RUN apt-get update
RUN apt-get -y install nginx && apt-get -y install git
RUN apt-get -y install mysql-server
RUN apt-get -y install libmysqlclient-dev

RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get -y install python3.8
RUN apt-get -y install python3-pip
# clone django project
RUN mkdir /home/apps
WORKDIR /home/apps
RUN git clone -b gillis-courier https://github.com/sonegillis/Cargo-Tracking.git
WORKDIR /home/apps/Cargo-Tracking
RUN ls
RUN pwd
RUN pip3 install -r requirements.txt
ENV MYSQL_ROOT_PASSWORD unsecure
COPY home/blackhat/envs/gillis-courier-env.txt cargotracking/.env
CMD ["echo", "& y 2 $MYSQL_ROOT_PASSWORD $MYSQL_ROOT_PASSWORD y | mysql_secure_installation"]
EXPOSE 8000
CMD ["python3", "manage.py", "runserver 0.0.0.0:8000"]
