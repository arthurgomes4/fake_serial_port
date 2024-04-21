FROM ubuntu:20.04

# intall pip
RUN apt-get update && apt-get install -y python3-pip

# use pip to install pyserial
RUN pip3 install pyserial

# install socat
RUN apt-get update && apt-get install -y socat minicom

# copy the repo contents into /
COPY . /

# build the C++ files
RUN g++ -o echo echo.cpp && g++ -o talk talk.cpp