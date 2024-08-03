import tkinter as tk
from datetime import datetime, timedelta


def update_time():
    now = datetime.now()
    time_label.config(text=now.strftime("%Y-%m-%d %H:%M:%S"))
    window.after(1000, update_time)  # 1秒後再次調用自己


def update_past_future_time():
    try:
        offset_hours = int(offset_entry.get())
        new_time = now + timedelta(hours=offset_hours)
        past_future_label.config(text=new_time.strftime("%Y-%m-%d %H:%M:%S"))
    except ValueError:
        past_future_label.config(text="無效的輸入")


# 創建主窗口
window = tk.Tk()
window.title("Show Time")

# 創建標籤顯示當前時間
time_label = tk.Label(window, font=("Arial", 24))
time_label.pack(pady=20)

# 創建標籤顯示過去或未來時間
past_future_label = tk.Label(window, font=("Arial", 24))
past_future_label.pack(pady=20)

# 創建輸入框和按鈕
offset_entry = tk.Entry(window)
offset_entry.pack()
update_button = tk.Button(window, text="更新", command=update_past_future_time)
update_button.pack(pady=10)

# 初始化時間
now = datetime.now()
update_time()  # 首次調用

window.mainloop()
