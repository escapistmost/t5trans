import t5trans

print("hello world 翻译为中文",t5trans.trans_en2ch('hello world'))
print("Здравствуйте, мир 翻译为中文",t5trans.trans_ru2ch('Здравствуйте, мир'))
print("你好，世界 翻译为俄文",t5trans.trans_ch2ru('你好，世界'))
print("你好，世界 翻译为英文",t5trans.trans_ch2en('你好，世界'))
print("hello world 翻译为俄文",t5trans.trans_en2ru('hello world'))
print("Здравствуйте, мир 翻译为英文",t5trans.trans_ru2en('Здравствуйте, мир'))

