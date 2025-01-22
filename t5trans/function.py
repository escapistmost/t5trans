from transformers import T5ForConditionalGeneration, T5Tokenizer
import os
import torch



def get_model(cache_dir=None,device=torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    if cache_dir is None:
        cache_dir = "./models"
    os.makedirs(cache_dir, exist_ok=True)  # 确保目录存在
    model_name = 'utrobinmv/t5_translate_en_ru_zh_small_1024'
    model = T5ForConditionalGeneration.from_pretrained(model_name, cache_dir=cache_dir)
    model.to(device)
    tokenizer = T5Tokenizer.from_pretrained(model_name, cache_dir=cache_dir)
    return model, tokenizer


def trans_ch2en(chinese='你好,世界', cache_dir=None,device=torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    """

    :param chinese: 输入中文，string
    :param cache_dir: 模型保存/读取地址，string
    :param device: 判定使用gpu还是cpu运行模型，一般不用管，但有的人torch判定能用gpu但运行会出问题的话可以改成cpu，就是慢一点，string
    :return: 翻译出来的英语，string
    """
    model, tokenizer = get_model(cache_dir,device)
    prefix = 'translate to en: '
    src_text = prefix + chinese
    input_ids = tokenizer(src_text, return_tensors="pt")
    generated_tokens = model.generate(**input_ids.to(device))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return result[0]


def trans_en2ch(english='hello world', cache_dir=None,device=torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    """

    :param english: 输入英语，string
    :param cache_dir: 模型保存/读取地址，string
    :param device: 判定使用gpu还是cpu运行模型，一般不用管，但有的人torch判定能用gpu但运行会出问题的话可以改成cpu，就是慢一点，string
    :return: 翻译出来的中文，string
    """
    model, tokenizer = get_model(cache_dir,device)
    prefix = 'translate to zh: '
    src_text = prefix + english
    input_ids = tokenizer(src_text, return_tensors="pt")
    generated_tokens = model.generate(**input_ids.to(device))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return result[0]


def trans_ru2ch(russian='Здравствуйте, мир!', cache_dir=None,device=torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    """

    :param russian: 输入俄语，string
    :param cache_dir: 模型保存/读取地址，string
    :param device: 判定使用gpu还是cpu运行模型，一般不用管，但有的人torch判定能用gpu但运行会出问题的话可以改成cpu，就是慢一点，string
    :return: 翻译出来的中文，string
    """
    model, tokenizer = get_model(cache_dir,device)
    prefix = 'translate to zh: '
    src_text = prefix + russian
    input_ids = tokenizer(src_text, return_tensors="pt")
    generated_tokens = model.generate(**input_ids.to(device))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return result[0]


def trans_ch2ru(chinese='你好,世界', cache_dir=None,device=torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    """

    :param chinese: 输入中文，string
    :param cache_dir: 模型保存/读取地址，string
    :param device: 判定使用gpu还是cpu运行模型，一般不用管，但有的人torch判定能用gpu但运行会出问题的话可以改成cpu，就是慢一点，string
    :return: 翻译出的俄语，string
    """
    model, tokenizer = get_model(cache_dir,device)
    prefix = 'translate to ru: '
    src_text = prefix + chinese
    input_ids = tokenizer(src_text, return_tensors="pt")
    generated_tokens = model.generate(**input_ids.to(device))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return result[0]


def trans_en2ru(english='hello world', cache_dir=None,device=torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    """

    :param english: 输入英语，string
    :param cache_dir: 模型保存/读取地址，string
    :param device: 判定使用gpu还是cpu运行模型，一般不用管，但有的人torch判定能用gpu但运行会出问题的话可以改成cpu，就是慢一点，string
    :return: 翻译出的俄语，string
    """
    model, tokenizer = get_model(cache_dir,device)
    prefix = 'translate to ru: '
    src_text = prefix + english
    input_ids = tokenizer(src_text, return_tensors="pt")
    generated_tokens = model.generate(**input_ids.to(device))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return result[0]


def trans_ru2en(russian='Здравствуйте, мир!', cache_dir=None,device=torch.device("cuda" if torch.cuda.is_available() else "cpu")):
    """
    将俄语翻译成英语
    :param russian: 输入俄语，string
    :param cache_dir: 模型保存/读取地址，string
    :param device: 判定使用gpu还是cpu运行模型，一般不用管，但有的人torch判定能用gpu但运行会出问题的话可以改成cpu，就是慢一点，string
    :return: 翻译出来的英语，string
    """
    model, tokenizer = get_model(cache_dir,device)
    prefix = 'translate to en: '
    src_text = prefix + russian
    input_ids = tokenizer(src_text, return_tensors="pt")
    generated_tokens = model.generate(**input_ids.to(device))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return result[0]

