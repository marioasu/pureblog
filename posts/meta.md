Date: 2016-02-16
Title: meta标签常用属性
intro: 工作中用到了控制手机号码显示为拨号的超链接的meta元素 <meta name="format-detection" content="telephone=no" /> 顺便查了下meta标签的常规使用，做个小结
Tags: html meta
Status: public
Toc: yes
Position: 992

###两类meta标签
meta标签分为两大类 1.http标题信息(http-equiv) 类似http头文件(php中 优先级低于header函数)，向浏览器传回有用信息。 2.页面描述信息(name) 多用于描述网页，便于搜索引擎查找、分类。 两类meta标签都对应content属性，content属性类容用;(英文分号)分隔。

##http-equiv
- Content-Type 设定显示字符集
```html
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
```
同php中的：
```php
header('Content-Type:text/html;charset=UTF-8');
```
h5中较常使用
```html
<meta charset="UTF-8" />
```

- Refresh 刷新/跳转页面
```html
<meta http-equiv="Refresh" content="60" />
<meta http-equiv="Refresh" content="3;URL=http://mrsu.me" />
```

- Pragma cache模式
```html
<meta http-equiv="Pragma" content="no-cache" /> // 不缓存网页
```


##name
- keywords 关键字
```html
<meta name="keywords" content="mrsu,博客,IT" />
```

- description 简介
```html
<meta name="description" content="mrsu is me" />
```

- format-detection 格式侦测
```html
<meta name="format-detection" content="telephone=no,email=no,adress=no" />
```
