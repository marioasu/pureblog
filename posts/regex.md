Date: 2017-07-26
Title: 冷门正则表达式知识
intro: 你可能不知道的正则表达式知识点
Tags: 正则表达式
Status: public
Toc: yes
Position: 984

### 定界符 - Delimiters
成对出现的 ```[[a-zA-Z0-9\]``` 之外的其它字符都能作为正则表达式的定界符  
一般使用不会在匹配目标中出现的字符作为定界符，从而避免对这些字符的转义，以提高正则表达式的可读性  
e.g.  
想要匹配 ```'http://mrsu.me/'```  
使用'/'作定界符: ```'/http:\/\/mrsu.me\//'```  
换成'#': ```'#http://mrsu.me/#'```

### 简写字符集 - Shorthanded Character Classes
\w (word character) - 匹配```[a-zA-Z0-9_]``` (主要是想提醒还有下划线)  
\s (whitespace character) - 匹配```[ \t\r\n\f]``` (注意集合里有个空格)

### 模式修正符 - Mode Modifiers
i (case insensitive) - 大小写不敏感  
x (free-spacing mode) - 忽略正则表达式中的空格 这可以让你写出可读性更高的正则表达式 注意想要匹配空格的时候要使用\ 作转义(不然会被忽略掉)  
s (single line mode) - 单行匹配，将整个文本看做一行，这样```.```就能匹配包括换行符(\n)在内的所有字符了。与之对应的是 m (multi-line mode)

### 分组&捕获 - Grouping and Capturing
(?:exp) - 非捕获组(Non-Capturing Groups) 匹配exp的内容，但不捕获到组里 当()只用来限定或(|)的关系范围，而不是用来获取匹配值或反向引用时，exp的值就没有必要保存到分组里  
(?|exp) - 分支重设组(Branch Reset Groups) 与(?:exp)不同的是这个表达式会重新设置它包含的分支中未匹配的分支不捕获(不占用组号)  
e.g.  
```php
<?php
$regexp = '/((a)|(b)|(c))\d+(end)/';
$str = '123456a890end';
preg_match($regexp, $str, $matches);
print_r($matches);

结果: 索引0包含整个表达式匹配到的内容 索引1-5分别包含从左到右数第n个括号匹配到的内容
Array
(
    [0] => a890end
    [1] => a
    [2] => a
    [3] => 
    [4] => 
    [5] => end
)

现在改变 $regexp = '/(?:(a)|(b)|(c))\d+(end)/';
结果: 第一个括号匹配到的内容不再被捕获
Array
(
    [0] => a890end
    [1] => a
    [2] => 
    [3] => 
    [4] => end
)

再次改变 $regexp = '/(?|(a)|(b)|(c))\d+(end)/';
结果: (?|exp)包含的分支中未匹配到的分支未被捕获(不占用组号)
Array
(
    [0] => a890end
    [1] => a
    [2] => end
)
```

### 命名捕获组 - Named Capturing Groups
通常我们使用 ```\1 \2 \3``` 来反向引用分组，命名捕获组相当于给这些反向应用起了个别名  
使用 ```(?P<name>group)``` 来给匹配到的分组内容命名  
使用 ```\k<name>``` 来反向引用命名捕获组，当然同样可以使用原来的方式（对应匹配顺序的数字）来反向引用  
可以用来提取 ```PATH_INFO``` 中的信息，实现router  
e.g.
```php
<?php
$regex = '#/hello/(?P<user>\w+)ME\k<user>#';
$str = '/hello/mrsuMEmrsu';
preg_match($regex, $str, $matches);
var_dump($matches);

结果： 除了使用数字（1）之外，还可以使用组名key（user）来访问匹配到的分组
array(3) {
  [0] =>
  string(17) "/hello/mrsuMEmrsu"
  'user' =>
  string(4) "mrsu"
  [1] =>
  string(4) "mrsu"
}

```

### 参考资料
去这里了解更多关于正则表达式的知识：<a href="http://www.regular-expressions.info/" target="_blank">http://www.regular-expressions.info/</a>
