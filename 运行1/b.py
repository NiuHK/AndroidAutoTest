from mitmproxy import http
import json
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
    except Exception as e:
        print(f"发送消息时出错: {e}")
    finally:
        client_socket.close()

def response(flow: http.HTTPFlow):
    # 检查请求的 URL 是否包含指定路径
    if "https://xyks.yuanfudao.com/leo-game-pk/android/math/pk/match" in flow.request.url:
        json_data = json.loads(flow.response.text)
        questionlist = json_data["examVO"]["questions"]
        answers = [ans["answer"] for ans in questionlist]
        send_msg(answers)