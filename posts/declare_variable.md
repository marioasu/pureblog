Date: 2017-05-08
Title: 变量声明语法
intro: java和c两种风格的数组声明语法，和同事聊天的收获
Tags: 语言 java c
Status: public
Toc: yes
Position: 989

今天下班和彬文一起走路回家，途中瞎侃。聊到程序语言设计，不知道我最近在哪里看到过说java和c的数组声明方式的差别：声明一个整型数组a，java的语法是 int[] a; c语言的语法是 int a[]; 当时并不真正明白孰优孰劣，直到和彬文解释时才豁然开朗：java把原始类型和复合类型的变量声明语法统一了（变量类型 + 空格 + 值）。当你看到int[] a时很容易就可以理解int[]是一个变量类型，它代表一个整型数组（事实上我在写接口文档的时候就是这样表示的），而对于c语言的语法当你看到int a[]的前半部分时并不知道接下来会声明一个整型还是一个整型数组，而且还带有二义性（究竟是想声明整型变量a[]还是想声明整型数组a），这就增加了额外的解读规则 -- 变量后面有个[]表示这是一个数组。

当然这是我当下的个人理解，貌似说得通。不过聊天真是一种活跃大脑，带动思考的好方式啊。
