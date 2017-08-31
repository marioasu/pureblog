Date: 2015-07-03
Title: LeanCloud权限认证 js前端对接
intro: LeanCloud开启服务端认证后的js前端对接，官方没有实现鉴权函数，自己写了一个，对js的回调函数又有了新的认识。
Tags: LeanCloud SaaS
Status: public
Toc: yes
Position: 998

#### 一.创建实时通信实例时开启服务端认证

```
	rt = AV.realtime({
		...
        auth: AuthFun // 打开这行代码的注释即可
    });
```

#### 二.配置鉴权服务器地址

```
	var authUrl = 'http://yourdomain/path/xxx';
```

具体的服务端签名方式参见官方说明文档，通过自己的服务器(云代码方式没研究过)完成签名后返回json到客户端示例：

`
    {"signature":"cbf90a9528496763d0f95e808c2f4f910e947117","nonce":"vBkiW5Uc","timestamp":1435052994}
`

#### 三.最最关键的一步，实现认证函数--AuthFun

这里(自以为)巧妙地利用的官方包里的ajax工具，让代码显得很简短
稍微解释一下这个认证函数：
AuthFun在官方包AV.realtime.js里面调用，调用时第一个参数会根据鉴权的类型(建立session、加入房间...)不同而不同，它是交给服务器用于鉴权的信息，服务端需要根据参数信息来决定如何签名；第二个参数是一个回调函数，需要我们在鉴权函数里调用并传入鉴权信息（json格式）作为参数，我利用官方提供的ajax工具，在ajax请求自己的服务器得到签名信息后，以签名信息作参数，调用这个回调函数。
```
	function AuthFun(param, callback) {
        var data = {};
        data = param;

        AV.realtime._tool.ajax({
            url: authUrl,
            method: 'post',
            form: true,
            data: data
        }, callback);
    }
```