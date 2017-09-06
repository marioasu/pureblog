FROM mrsu/supervisord
MAINTAINER  Su Zhongping <marioasu@163.com>

RUN apt-get update && \
    apt-get install -y gunicorn && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    > /var/lib/apt/extended_states

COPY etc /etc

ENV WEB_HOME=/home/admin/web
VOLUME ${WEB_HOME}
WORKDIR /home/admin/web/logs
