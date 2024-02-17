from wsgiref.simple_server import make_server
import json
import urllib

def RunServer(environ, start_response):

    #添加回复内容的HTTP头部信息，支持多个
    headers = {'Content-Type': 'application/json', 'Custom-head1': 'Custom-info1'}

    # environ 包含当前环境信息与请求信息，为字符串类型的键值对
    current_url = environ['PATH_INFO']
    print(current_url)
    # current_content_type = environ['CONTENT_TYPE']
    # current_content_length = environ['CONTENT_LENGTH']
    # current_request_method = environ['REQUEST_METHOD']
    # current_remote_address = environ['REMOTE_ADDR']
    # current_encode_type = environ['PYTHONIOENCODING']        #获取当前文字编码格式，默认为UTF-8

    #获取 body JSON内容转换为python对象
    current_req_body = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
    current_req_json = json.loads(current_req_body)

    #打印请求信息
    #print("environ:", environ)
    # print("REQUEST remote ip:", current_remote_address)
    # print("REQUEST method:", current_request_method)
    # print("REQUEST URL:", current_url)
    # print("REQUEST Content-Type:", current_content_type)
    # print("REQUEST body:", current_req_json)

    from_lang = current_req_json['from_lang']
    from_lang = urllib.parse.unquote(from_lang)

    to_lang = current_req_json['to_lang']
    to_lang = urllib.parse.unquote(to_lang)

    content = current_req_json['content']
    content = urllib.parse.unquote(content)

    #根据不同URL回复不同内容
    if current_url == "/translation":
        # 处理content
        result = do_translation(from_lang,to_lang,content)
        
    # 拼装回复报文
    successStr = '''
        {
            "code":1,"msg":"success",
            "data":{
                "content":"%s"
            }
        }
        ''' % (result)
    start_response("200 OK", list(headers.items()))
    return [successStr.encode("utf-8"), ]

def do_translation(from_lang,to_lang,content):
    # 调用transformers进行翻译
    from transformers import pipeline
    model_checkpoint = "Helsinki-NLP/opus-mt-" + from_lang + "-" + to_lang
    translator = pipeline('translation', model=model_checkpoint)
    result = translator(content)
    return result[0]['translation_text']

if __name__ == '__main__':

    #10000为HTTP服务监听端口，自行修改
    httpd = make_server('', 3678, RunServer)
    host, port = httpd.socket.getsockname()
    print('Serving running', host, 'port', port)
    httpd.serve_forever()