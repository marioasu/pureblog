Date: 2017-06-21
Title: 玩玩树莓派零 - 点亮及基本设置
intro: 从安装树莓派系统到基本设置备忘
Tags: 树莓派
Status: public
Toc: yes
Position: 986

设备
=======
- 树莓派
- Micro SD Card
- 带HDMI接口的显示器及连接线
- USB键盘
- USB鼠标

安装
=======
镜像烧录
```
umount /dev/sdX1
dd bs=4M if=2017-04-10-raspbian-jessie.img of=/dev/sdX
```

基本设置
=======
sudo raspi-config 进入设置界面

### Localisation Options
- Change Locale -> en_US.UTF-8 UTF-8
- Change Timezone -> Asia -> Chongqing
- Change Keybord Layout -> Generic 101-key PC -> English (US) English (US, alternative international) -> Ok -> Ok -> Yes

### Interfacing Options
- SSH -> Yes

其他配置
=======
设置固定ip
-------
修改 /etc/dhcpcd.conf 添加
```
# config by mrsu
static ip_address=192.168.1.120/24
static routers=192.168.1.1
static domain_name_servers=114.114.114.114 8.8.8.8
```

安装Docker
-------
```
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi
```
