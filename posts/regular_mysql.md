Date: 2018-07-04
Title: mysql常规操作
intro: mysql 基本使用
Tags: 常规操作
Status: public
Toc: yes
Position: 977

## 连接
```
mysql -h{host} -P{port} -u{username} -p{password} // 为了安全 password 在 -p 换行后输入
mysql -u{username} -S{sock_file} -p{password} // 通过socket文件本地连接
```

## 创建用户和授权
```
CREATE USER {username}@{host} IDENTIFIED BY {password}
GRANT PRIVILEGES ON {database}.{table} TO {username}@{host} [WITH GRANT OPTION]
DENY/REVOKE PRIVILIGES ON {database}.{table} FROM {username}@{host}
SHOW GRANTS FOR {username}@{host}
```
_grant是赋予deny是拒绝revoke是取消_  
_priviliges包括select|insert|update|delete等,逗号分割,all表示全部权限_  
_database和table用*占位,host用%占位并可只占部分网段_
_with grant option让该用户拥有授权的权限_

## 设置密码
- 方法1. 使用mysqladmin
```
mysqladmin -u{username} [-p{old_pwd}] password {new_pwd}
```
- 方法2. 使用命令 - 推荐
```
set password for {username}@{host} = password({password})
```
- 方法3. 直接编辑mysql.user表
```
update mysql.user set password/authentication_string(after 5.7) = password({password}) where user={user} and host={host};
flush privileges;
```

## 简写符号
ego (\G) 纵向展示数据  
edit (\e) 使用编辑器编辑命令  
system (\!) {shell command} 执行shell指令  
\c 清除本次输入字符

## 常规命令
STATUS;
SHOW ENGINES;
SHOW VARIABLES LIKE 'have%';

## 支持函数
sin pi version inet_aton inet_ntoa abs ceil floor rand round  
length //字节数 char_length //字符数 concat(str1, str2, ...) left(str, len) right(str, len) substring(str, pos[, len]) //pos从1开始 lower(str) upper(str)  
now curtime curdate
count min max avg sum

## 支持变量
CURRENT_DATE

## 默认事务级别
transaction_isolation | REPEATABLE-READ

## EXPLAIN工具
列解释
-------
- type -- 访问类型 表示MySQL在表中找到所需行的方式 ALL(Full Table Scan) - index(Full Index Scan) - range(索引范围扫描) - ref(非唯一索引扫描) - eq_ref(唯一索引扫描) - const, system - NULL
- Extra -- Using where - InnoDB存储层找到记录后返回给MySQL Server层过滤  Using index 直接从索引中取数据