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
print(t5trans.trans_en2ch('hello world'))
print(t5trans.trans_ru2ch('Здравствуйте, мир'))
print(t5trans.trans_ch2ru('你好，世界'))
print(t5trans.trans_ch2en('你好，世界'))
print(t5trans.trans_en2ru('hello world'))
print(t5trans.trans_ru2en('Здравствуйте, мир'))
```
