# t5trans
 a repository using "utrobinmv/t5_translate_en_ru_zh_small_1024" to translate

 一个使用"utrobinmv/t5_translate_en_ru_zh_small_1024"进行翻译的库
 
## 如何安装
```
pip install git+https://github.com/escapistmost/t5trans.git
```
or
```
git clone https://github.com/escapistmost/t5trans.git
cd t5trans
pip install .
```

## 使用示例

``` python
import t5trans
print(t5trans.trans_en2ch('hello world'))
print(t5trans.trans_ru2ch('Здравствуйте, мир'))
print(t5trans.trans_ch2ru('你好，世界'))
print(t5trans.trans_ch2en('你好，世界'))
print(t5trans.trans_en2ru('hello world'))
print(t5trans.trans_ru2en('Здравствуйте, мир'))
```
Russian (ru_RU), Chinese (zh_CN), English (en_US)

## 注意事项
这个库会自动下载模型到你运行这个代码的models文件夹中（没有这个文件夹它也会自动创建一个），但是大家可能会遇到没有魔法（翻不了墙，下半天结果网络错误），位置存储不够等问题，我将提供对应的解决方法：

#### 网络波动问题
下面是这个模型的链接，你需要自己去把这个文件下载下来并解压到对应的地址，然后使用函数的时候增加一个参数（下面是个例子）：
https://pan.baidu.com/s/1TMbs6OGJC4daS7tqqFlLAw?pwd=ggnm

```
print(t5trans.trans_en2ch('hello world'), cache_dir='./my_model/')
```
上面对应的文件夹相对格式是这样的：
main.py  ——你运行文件时的相对路径
my_model ——文件夹
    models--utrobinmv--t5_translate_en_ru_zh_small_1024 ——模型文件