Date: 2017-07-06
Title: 玩玩树莓派壹 - 安装 Kali Linux
intro: 在树莓派上安装 Kaili Linux 及基本设置
Tags: 树莓派
Status: public
Toc: yes
Position: 985

安装
=======
Mac下格式化U盘（读卡器+Micro SD Card）
```
diskutil list - 找到U盘设备 我的是 /dev/disk4
diskutil eraseDisk FAT32 KALI /dev/disk4 - KALI是格式化后磁盘的名称
```

Linux下格式化U盘（读卡器+Micro SD Card）
```
sudo fdisk -l
sudo mkfs -t vfat /dev/sdXX
```

镜像烧录 - 在 Kali Linux 官网找到需要的<a href="https://www.offensive-security.com/kali-linux-arm-images/" target="_blank">系统img镜像</a>（我的是kali-2017.01-rpi2.img）并烧录到U盘
```
diskutil unmountDisk /dev/disk4 - Linux下用umount
sudo dd bs=2m if=kali-2017.01-rpi2.img of=/dev/disk4
```

扩容
=======
raspbian系统工具raspi-config可用来给Micro SD卡扩容，去<a href="http://archive.raspberrypi.org/debian/pool/main/r/raspi-config/" target="_blank">官网下载</a>deb包，注意别下最新版，新版只支持raspbian系统，我下的是raspi-config_20160506_all.deb
```
dpkg -i raspi-config_20161207_all.deb - 安装deb包，会出现依赖问题
apt --fix-broken install - 解决依赖
raspi-config -> Expand Filesystem
reboot - 重启后文件系统扩容生效
```

树莓派上的 Kali Linux 自动登录
=======
vi /etc/lightdm/lightdm.conf - 删除这两行注释并修改
```
autologin-user=root
autologin-user-timeout=0
```

vi /etc/pam.d/lightdm-autologin - 允许root用户自动登录
```
#auth      required pam_succeed_if.so user != root quiet_success - 注释掉这一行
```

添加中文字体
=======
```
apt-get install ttf-wqy-zenhei
```

修改时区（CST）
=======
```
ln -sf /usr/share/zoneinfo/Asia/Chongqing /etc/localtime
```
