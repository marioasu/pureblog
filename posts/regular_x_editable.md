Date: 2018-06-27
Title: x-editable常规操作
intro: x-editable 基本使用
Tags: 常规操作
Status: public
Toc: yes
Position: 978

## 基本介绍
x-editable可以提供行内编辑功能  
[官网](http://vitalets.github.io/x-editable/)  
支持三种引擎：bootstrap，jquery-ui，jquery  
引入相应的css和js文件便可使用

## 常规操作
x-editable有popup和inline两种编辑模式，默认是popup  
```js
// turn to inline mode
$.fn.editable.defaults.mode = 'inline';
```

请求方式默认是POST
```js
// turn to PUT
$.fn.editable.defaults.ajaxOptions = {type: "PUT"};
```

使用方法
```
$('username').editable({
    type: 'text', // text|textarea|select|date|checklist and more
    pk: 1,
    name: 'username',
    url: '/post',
    title: 'Enter someting', // popup框标题
    toggle: 'dbclick', // 默认为click
    validate: function(value) {
    	if(!value.match(/^\d{1,5}$/)) {
            '请输入1-5位数字';
        }
    },
    success: function(response, newValue) {
    	// userModel.set('username', newValue);
    }
});
```
其中url可以是function，这时验证和成功回调都在function中完成 参数为包含pk,name,value的json对象
```js
// If function - it will be called instead of ajax. Function should return deferred object to run fail/done callbacks.
url: function(params) {
    var d = new $.Deferred();
    if(params.value === 'abc') {
        return d.reject('error message'); //returning error via deferred object
    } else {
        //async saving data in js model
        someModel.asyncSaveMethod({
           ..., 
           success: function(){
              d.resolve();
           }
        }); 
        return d.promise();
    }
}
```
