from mitmproxy import http
import json
from queue import Queue
import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 7899))

def send_msg(message):
    try:
        # 将列表转换为 JSON 字符串
        message_str = json.dumps(message)
        client_socket.sendall(message_str.encode())
        data = client_socket.recv(1024)
        print(f"回显数据: {data.decode()}")
    finally:
        client_socket.close()


def response(flow: http.HTTPFlow):
    # 检查请求的 URL 是否包含指定路径
    if "https://xyks.yuanfudao.com/leo-game-pk/android/math/pk/match" in flow.request.url:
        # print("抓到目标请求：")
        # print(f"请求 URL: {flow.request.url}")
        # print(f"请求方法: {flow.request.method}")
        
        # # 打印响应内容
        # print("响应内容:")
        # print(flow.response.text)  # 使用 flow.response.content 可以获取二进制数据
        json_data = json.loads(flow.response.text)
        questionlist = json_data["examVO"]["questions"]
        answers=[ans["answer"] for ans in questionlist]
        # print(answers)
        send_msg(answers)