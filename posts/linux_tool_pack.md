Date: 2018-05-17
Title: linux常规操作 - 打包、压缩
intro: 打包、压缩工具常用命令笔记
Tags: tar gzip 常规操作
Status: public
Toc: yes
Position: 979

## 打包工具 tar
tar 可以将多个文件或文件夹打包成一个文件，所以第一个参数是目标文件名  
常用选项

- c 创建
- x 与c对应 提取
- z 打包的同时压缩 提取的时候解压缩
- v verbose
- f 指定文件
常规操作
```bash
tar -czvf des.tar.gz a b c
tar -xzvf desc.tar.gz // .tar.gz 也可以简写成 .tgz 从文件名上表示出文件格式
```

## 压缩工具 xz
常规操作
```bash
xz filename // 压缩
xz -d filename.xz // 解压
```

## 压缩工具 gzip
常用选项

- v verbose
常规操作  
```bash
gzip filename // 压缩
gzip -d filename // 解压 同gunzip
gzip -r dirname // 递归压缩目录下的所有文件
```
