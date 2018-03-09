Date: 2017-08-03
Title: 我的Linux软件配置文件
intro: 常用的Linux软件配置文件，随时更新。分享一下，也方便自己查找
Tags: Linux
Status: public
Toc: yes
Position: 982

### Vim - ～/.vimrc
```
set number
set ts=4
set expandtab
set shiftwidth=4
set autoindent
```

### ssh - ~/.ssh/config
```
Host *
ControlMaster auto
ControlPath ~/.ssh/master-%r@%h:%p
ServerAliveInterval 10

Host linode
    HostName 139.162.*.*
    Port 2***
    User admin
```

### git - ~/.gitconfig
```
[alias]
    st = status
    co = checkout
    ci = commit
    br = branch
    df = diff -b
    dc = diff --cached
    pl = pull --rebase
    cm = commit --amend --no-edit
[core]
    excludesfile = ~/.gitignore
[push]
    default = current
```

### shadowsocks - ~/shadowsocks/config.json
```json
{
    "server":"139.162.*.*",
    "server_port":8388,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"********",
    "timeout":300,
    "method":"aes-256-cfb"
}
```

### polipo - /etc/polipo/config
```
logSyslog=true
logFile=/var/log/polipo/polipo.log

proxyAddress="0.0.0.0"

socksParentProxy="127.0.0.1:1080"
socksProxyType=socks5
proxyPort=8123

chunkHighMark=50331648
objectHighMark=16384

serverMaxSlots=64
serverSlots=16
serverSlots1=32
```
然后将
```
export http_proxy="http://127.0.0.1:8123"
export https_proxy="https://127.0.0.1:8123"
```
写入 ～/.bashrc 或在终端执行
```curl ip.gs```查看当前IP信息

### screen - ~/.screenrc
```
escape ^Ll # Instead of Control-a, make the escape/command character be Control-l
autodetach on # Autodetach session on hangup instead of terminating screen completely
startup_message off # Turn off the splash screen
defscrollback 30000 # Use a 30000-line scrollback buffer
termcapinfo xterm ti@:te@
```

### logrotate /etc/logrotate.d/php5-fpm
```
/home/admin/php/var/log/*.log {
    daily
    rotate 30
    missingok
    notifempty
    dateext
    compress
    delaycompress
    create 0640 admin admin
    sharedscripts
    postrotate
        [ -r /home/admin/php/var/run/php-fpm.pid ] && kill -USR1 `cat /home/admin/php/var/run/php-fpm.pid`
    endscript
}
```
