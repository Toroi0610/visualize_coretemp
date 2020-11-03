# ベースとなるイメージ
FROM ubuntu:18.04

# RUNでコンテナ生成時に実行する
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install numpy matplotlib pandas dash==1.17.0

RUN mkdir /home/work
WORKDIR /home/work
