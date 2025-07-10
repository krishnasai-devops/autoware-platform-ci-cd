FROM ubuntu:20.04

RUN apt-get update && apt-get install -y g++ cmake

COPY ./cpp_cruise_control /app
WORKDIR /app
RUN mkdir build && cd build && cmake .. && make