# filterTest

---

根本不是这样的！！
---
更正
---





---
原答案
---

google了一下关键字django filter，除了django官方文档下的QuerySet方法外，还查到了一个第三方库django_filters

按照官方的样例试着运行了一下，大概明白了怎样使用

* 安装
* 定义models
* 根据查找需要，定义Filter，查询的字段名放进元数据下的fields列表中
* views中使用Filter，做好url映射
* 模板渲染

---
悄咪咪的分割线
---


这样做的话虽然没有在views中显式地import models，但是还是在model_filter.py中引入了model