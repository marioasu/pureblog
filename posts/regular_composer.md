Date: 2018-07-30
Title: composer常规操作
intro: composer 基本使用
Tags: 常规操作
Status: private
Toc: yes
Position: 975

## 常用命令
require 首先检查配置中的repositories(对象数组，对象含type和url字段)属性，若未找到指定包，则从Packagist中查找
install 若没有composer.lock，则根据composer.json中的内容生成，有则直接使用composer.lock中的内容下载依赖文件
update 相当于没有composer.lock的install，会使用最新依赖
