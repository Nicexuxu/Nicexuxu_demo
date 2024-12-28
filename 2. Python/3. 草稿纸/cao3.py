import socket
import tkinter as tk
from tkinter import scrolledtext
import threading

# 连接到服务器
host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# 创建图形界面
def send_message():
    message = message_entry.get()
    if message:
        client.send(message.encode('utf-8'))
        message_entry.delete(0, tk.END)

# 接收消息并显示
def receive_message():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, message + '\n')
            chat_box.config(state=tk.DISABLED)
            chat_box.yview(tk.END)
        except:
            break

# 设置窗口
window = tk.Tk()
window.title("聊天软件")

# 聊天显示框
chat_box = scrolledtext.ScrolledText(window, width=50, height=20, state=tk.DISABLED)
chat_box.grid(row=0, column=0, padx=10, pady=10)

# 输入框
message_entry = tk.Entry(window, width=40)
message_entry.grid(row=1, column=0, padx=10, pady=10)

# 发送按钮
send_button = tk.Button(window, text="发送", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# 启动接收消息的线程
threading.Thread(target=receive_message, daemon=True).start()

window.mainloop()
