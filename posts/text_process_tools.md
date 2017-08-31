Date: 2017-05-22
Title: Linux常用文本处理工具
intro: 总结一下经常用到的linux文本处理工具(命令)
Tags: linux gawk grep
Status: public
Toc: yes
Position: 988

文本处理通常需要合用很多工具，简单汇总一下，仅列出常用的选项

### grep
-E :    --extended-regexp 扩展的正则表达式  
-o :    --only-matching 只输出匹配部分  
-i :    --ignore-case 不分大小写  
-v :    --invert-match 选择不匹配的行  
-r :    --recursive 这个主要在目录下的文件中搜索匹配的内容，可以配合-n使用  
-n :    --line-number 同时输出行号  
--color:    为匹配内容添加颜色，通常在~/.bashrc中配置 alias grep='grep --color'  

### gawk
gawk的一般使用模式是 gawk [options] '[/pattern/ | expression] {action}'  
-F :    --field-separator 字段分隔符，可以指定多个（[f1f2]） 默认是任意数量的空格或tab  
变量 FS 对应参数-F的值  
变量 OFS 输出字段分隔符  
变量 ORS 输出记录分隔符  
变量 NF 表示当前记录中字段的个数 - 所以 $NF 可以引用最后一个字段（使用NF可以引用其数值）、$(NF-1) 引用倒数第二个...  
变量 NR 表示当前记录个数  
变量 FILENAME 表示当前输入文件的名字  
$0 可以引用整条记录  
BEGIN 和 END 模式 - BEGIN {action} 或 END {action} 处理记录之前或之后要做的操作  
在字段中匹配模式 - $field ~ /pattern/ 或 $field !~ /pattern/ (不匹配) 还可以使用==/!=/>=等比较运算符  
可以使用布尔操作符（&& || !）连接多个规则  

### sed 流编辑器
sed [OPTION]... {script-only-if-no-other-script} [input-file]...  
-n :    只输出匹配的行  
-i :    直接在原文件上编辑  
表达式  
p 打印  
d 删除  
s 替换 紧跟s的字符就是查找串和替换串的分隔符  

### cut
-d :    --delimiter 分隔符  
-f :    --fields 输出字段

### sort
-r :    --reverse 反向排序  
-n :    --numeric-sort 按数值排序  

### uniq 去除相邻重复行，通常先sort排序再uniq去重
-c :    --count 统计重复行数  
-i :    --ignore-case 不区分大小写的比较  
-u :    --unique 只打印没有重复的行  

通过管道组合这些工具就可以做一些文本查找替换，日志分析之类的事情了  
例如查找某nginx访问日志中ip请求量的top10可以用：  
cat nginx_access.log | gawk '{print $1}' | sort | uniq -c | sort -rn | head -n 10

<br>
今天北京难得下了场不小的雨，下班时天空的粉红印在了建筑的玻璃墙上
<p><img style="max-width: 500px;" src="/static/img/blog_post/20170522.jpg" /></p>
