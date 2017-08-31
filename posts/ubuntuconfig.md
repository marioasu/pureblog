Date: 2017-08-03
Title: 重新配置Ubuntu16.04笔记
intro: 昨天自己的vps被黑了，用Ubuntu16.06的镜像rebuild了一下，重新配置并部署了博客和shadowsocks服务，顺便记一下笔记
Tags: Linux
Status: public
Toc: yes
Position: 983

### 前言
我用的是<a href="https://www.linode.com/" target="_blank">Linode</a>的VPS，Tokyo 2, JP 机房，速度我很满意。昨天服务器被停用了，按照工单上的原因说明，从我的ip对其它服务器发起了攻击（暴力尝试ssh登录），比较靠谱的解决方法就是rebuild。我用了Ubuntu16.06的镜像rebuild之后回复了工单，不久服务器网络限制解除。这样一来，之前服务器上的服务全得重新搭建，于是就有了这篇笔记。

### 创建用户
创建admin用户，密码和rebuild时填写的root密码都用```pwgen```生成，加入sudo组
```
useradd -g sudo -d /home/admin -m -s /bin/bash admin
passwd admin
```

### 修改主机名
将主机名改为linode，方便自己在终端中识别。在```/etc/hosts```文件中把主机名指向本地回环地址，不然在执行sudo的时候会提示```sudo: unable to resolve host linode```（我也不知道为啥）
```
echo 'linode' /etc/hostname
hostname -F /etc/hostname
/etc/hosts
127.0.0.1       linode
```

### 修改本地时间
```
ln -sf /usr/share/zoneinfo/Asia/Chongqing /etc/localtime
```

### 安装docker服务
docker安装教程见 <a href="https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/" target="_blank">https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/</a>    
然后安装docker-composer
```
sudo apt-get install docker-composer
```
将admin用户加入docker组，省去每次执行docker都要敲sudo的麻烦
```
sudo usermod -aG docker admin
```

### 配置git
如果没有配置，在下次执行commit的时候也会得到配置提示
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```
然后生成一对ssh秘钥，将公钥添加到github上
```
ssh-keygen -t rsa -C "from mrsu's linode"
```

### 修改sshd端口
有了前车之鉴，不能使用sshd的默认端口了（其实也有```fail2ban```的解决方案，未尝试）。况且从```/var/log/auth.log```发现了大量类似```Aug  3 02:07:14 localhost sshd[12680]: Failed password for root from 221.194.47.233 port 51624 ssh2```的记录，于是决定不再使用22端口  
顺便限制只能ipv4登录  
修改```/etc/ssh/sshd_config```
```
Port 2333
AddressFamily inet
```

### 软件配置
软件配置单开了一篇，随时更新：[我的Linux软件配置文件](/post/configfile)
