Date: 2018-09-25
Title: ldap服务搭建
intro: ldap相关服务
Tags: ldap
Status: public
Toc: yes
Position: 974

> 公司内部通常会有各种需要认证的服务，账号密码的创建和管理成本随服务和员工的增多会变得很高。实现使用统一的账号登录不同系统，ldap服务是一个很好的账号统一管理方案。

## 安装

ubuntu下的安装
```bash
apt-get install slapd
apt-get install ldap-utils
```

## 配置
首先为管理员账号生成密码
```bash
slappasswd
```
然后拷贝配置文件
```bash
sudo cp /usr/share/slapd/DB_CONFIG /var/lib/ldap/
sudo cp /usr/share/slapd.conf /etc/ldap/
```
修改 /etc/ldap/slapd.conf
```bash
database  bdb
suffix "dc=17play,dc=tech"
rootdn "cn=admin,dc=17play,dc=tech"
rootpw {SSHA}t/KFe......
access to [what]
    by [who] [control]
```

## 管理
可以安装ldap-account-manager来管理ldap数据
```
sudo apt-get install ldap-account-manager
```
安装之后配置nginx服务到 /usr/share/ldap-account-manager

## 工具指令
ldapsearch
-------
-x 简单验证  
-b searchbase 根节点

##参考资料
https://mp.weixin.qq.com/s/JyH5mqwWFt0N1nGYZqBCBQ  
https://mp.weixin.qq.com/s/VdZ_vGXEhRhQiyH_kTMRFw  
