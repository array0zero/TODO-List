import tkinter as tk
from linecache import cache
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        root.title("やることリスト")

        self.tasks = []

        # フレームを作成
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # やることを入力するテキストボックスをフレームに配置
        self.entry_task = tk.Entry(input_frame, width=40)
        self.entry_task.pack(side=tk.LEFT)

        # 入力したやることを追加処理するためのボタンをフレームに配置
        self.add_button = tk.Button(input_frame, text="追加", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # 　やることの一覧を表示する部分
        self.task_list = tk.Listbox(root, width=50, height=10)
        self.task_list.pack(padx=10)

        # 削除ボタン
        self.delete_button = tk.Button(root, text="削除", command=self.delete_task)
        self.delete_button.pack()

        # やることの完了状態を変更するためのボタン
        self.toggle_button = tk.Button(root, text="完了/未完了", command=self.toggle_task)
        self.toggle_button.pack()

    # タスク追加
    def add_task(self):
        task = self.entry_task.get()

        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_list()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("警告", "何も入力されていません！")

    # タスク削除
    def delete_task(self):
        try:
            select = self.task_list.curselection()[0]
            del self.tasks[select]
            self.update_list()
        except IndexError:
            messagebox.showwarning("警告", "タスクを選択してください！")

    # タスク完了状態切り替え
    def toggle_task(self):
        try:
            select = self.task_list.curselection()[0]
            self.tasks[select]["completed"] = not self.tasks[select]["completed"]
            self.update_list()
        except IndexError:
            messagebox.showwarning("警告", "タスクを選択してください！")

    # タスクの更新
    def update_list(self):
        self.task_list.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            text = task["task"]
            if task["completed"]:
                text = "[完了] " + text
                self.task_list.insert(tk.END, text)
                self.task_list.itemconfig(i, fg="gray", bg="lightgray")  # 完了したタスクを灰色で表示
            else:
                self.task_list.insert(tk.END, text)


if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
