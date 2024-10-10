import threading
import subprocess
import socket
from libs.execution import Execution
from time import sleep
import json

process = Execution()
info_ = False

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 7899))
    server_socket.listen(1)
    print("服务器已启动，等待连接...")

    while True:
        conn, addr = server_socket.accept()
        print(f"连接地址: {addr}")
        handle_client(conn)
        conn.close()

def handle_client(conn):
    print("等待数据")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"收到数据: {data.decode()}")
        conn.sendall(data)  # 回显收到的数据
        op(json.loads(data.decode()))

def run_b_script():
    subprocess.run(["mitmdump", "-s", "b.py", "--quiet"])

def op(list):
    print("等待进入答题界面")
    process.click_point(*process.wait_templete("assests/xiaoyuan/4.png",0.8,print_info=True))
    print('进入答题界面')
    # input('按回车键继续')
    for i in list:
        speed = 10
        if i == "<":
            process.swipe((687, 1447), (555, 1525), speed)
            process.swipe((555, 1525), (687, 1725), speed)
        elif i == ">":
            process.swipe((555, 1447), (687, 1525), speed)
            process.swipe((687, 1525), (555, 1725), speed)
        else:
            print('error', i)
        sleep(0.2)
    sleep(1.5)
    process.send_key_event(4)
    sleep(1.5)
    process.click_point(*process.find_templete("assests/xiaoyuan/3.png",0.8,print_info=info_))
    sleep(1.5)

# 启动 b.py 的线程
thread = threading.Thread(target=run_b_script)
thread.daemon = True
thread.start()
start_server()
thread.join()