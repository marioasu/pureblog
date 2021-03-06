Date: 2017-11-21
Title: SSH端口转发
intro: ssh端口转发（ssh隧道）常用设置
Tags: ssh
Status: public
Toc: yes
Position: 980

## 动态端口转发
场景： 通过本地端口代理，科学上网
```
-D [bind_address:]port
```

## 本地端口转发
场景： 本地主机有访问远程主机的权限而本地其它主机没有，通过本地主机转发远程主机特定端口的服务
```
ssh -L [bind_address:]port:host:hostport
```

## 远程端口转发
场景： 本地主机的服务需要暴露到外网，本地主机可连接到某台外网主机，通过外网主机转发本地主机特定端口的服务
```
ssh -R [bind_address:]port:host:hostport
```

## 基本参数解释
- 本地和远程两种转发都是通过由本地主机登录远程主机建立ssh隧道实现的
- bind_address 省略时只允许本地主机（localhost）建立连接， 设置```0```或```*```或加参数```-g```允许其它主机连接绑定端口(需要在/etc/ssh/sshd_config中设置GatewayPorts clientspecified)
- ```L```和```R```分别表示 local 和 remote，port也分别对应本地和远程
- 本地转发是在本地建立socket监听本地端口（port），远程转发是在远程建立socket监听远程端口（port）
- 本地转发时，使用者从本地端口连接到远程 host 走远程的dns解析，远程转发时，使用者从远程端口连接到本地， host 走本地主机的dns解析

## 其它常用参数
- -C： 压缩传输数据
- -f： 在后台运行，不登录到远程主机
- -n： 将stdio重定向到/dev/null（与 -f 配合使用）
- -N： 不执行远程命令（与 -f 配合使用）
- -g： 允许远程主机连接到建立的转发端口
- -T： 不分配TTY，只做代理

## autossh
可以通过```autossh```保持ssh会话
```
/usr/bin/autossh -M 0 -qN -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R 0:2222:localhost:22 host
```
