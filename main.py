import tkinter as tk
from linecache import cache
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        root.title("やることリスト")

        self.tasks = []

        # やることを入力するテキストボックス
        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.pack(pady=10)

        # 入力したやることを追加処理するためのボタン
        self.add_button = tk.Button(root, text="追加", command=self.add_task)
        self.add_button.pack()

        # 　やることの一覧を表示する部分
        self.task_list = tk.Listbox(root, width=50, height=10)
        self.task_list.pack()

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
        for task in self.tasks:
            text = task["task"]
            if task["completed"]:
                text = "[完了]" + text
            self.task_list.insert(tk.END, task)


if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
