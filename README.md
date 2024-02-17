# huggingface_translation
 huggingface translation
运行：python main.py
调用：post访问127.0.0.1:3678/translation
请求数据：

{
    "from_lang":"en",
    "to_lang":"zh",
    "content":"You can use the 🤗 Transformers library with the translation_xx_to_yy pattern where xx is the source language code and yy is the target language code. The default model for the pipeline is t5-base which under the hood adds a task prefix indicating the task itself, e.g. “translate: English to French”."
}

返回数据：

{
    "code": 1,
    "msg": "success",
    "data": {
        "content": "您可以使用“ 变换器库” 的翻译_xx_to_yy 模式, 其中xx是源语言代码, yy是目标语言代码。 管道的默认模式是 t5- base, 在引擎盖下添加任务前缀, 表示任务本身, 例如“ 翻译: 英文到法文 ” 。"
    }
}

⚠️注意：
1、Docker化尚未成功，程序部署需安装transformers及相关依赖过程比较漫长且繁琐
2、该程序当前仅支持英语（en）对各语言的互相翻译
