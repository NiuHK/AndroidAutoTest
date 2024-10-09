import threading
import subprocess
import socket


from libs.execution import Execution
from time import sleep
import numpy as np
import json
process = Execution()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 7899))
    server_socket.listen(1)
    print("服务器已启动，等待连接...")

    conn, addr = server_socket.accept()
    print(f"连接地址: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"收到数据: {data.decode()}")
        conn.sendall(data)  # 回显收到的数据
        op(json.loads(data.decode()))
        

    conn.close()
    
# 定义函数来运行 mitmdump
def run_b_script():
    subprocess.run(["mitmdump", "-s", "b.py","--quiet"])



def op(list):
    input("any key to continue")
    for i in list:
        if i == "<":
            process.swipe((687, 1447) , (555, 1525), 40)
            process.swipe( (555, 1525) ,(687, 1725) , 40)
        elif i == ">":
            process.swipe((555, 1447) , (687, 1525), 40)
            process.swipe( (687, 1525) ,(555, 1725) , 40)
        else:
            print('error',i)
        sleep(0.5)
        



# 启动 b.py 的线程
thread = threading.Thread(target=run_b_script)
thread.daemon = True
thread.start()
start_server()
thread.join()


# pip install Werkzeug==2.2.2