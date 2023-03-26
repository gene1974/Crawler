# instructions

### crawl_gptzero instruction

pip intsall selenium 

根据下面这个链接，安装对应版本的chromedriver

https://cloud.tencent.com/developer/article/1624100

输入文本在41行，需要大于250个字符

```python
text = '...'
```

输出结果在49行

```python
print(result_head_element.text)
```

如果需要多次调用接口，可以把41-52行放在循环里，不用重复创建页面。

网不好的时候可能会超时。

如果需要看程序执行UI，把9-14行的`chrome_options.add_argument`注释掉。

运行：

```bash
python crawl_gptzero.py
```
