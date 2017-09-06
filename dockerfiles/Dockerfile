FROM mrsu/supervisord
MAINTAINER  Su Zhongping <marioasu@163.com>

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install gunicorn && \
    pip3 install configparser && \
    pip3 install flask && \
    pip3 install markdown && \

    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    > /var/lib/apt/extended_states

COPY etc /etc

ENV WEB_HOME=/home/admin/web
VOLUME ${WEB_HOME}
WORKDIR /home/admin/web/logs
