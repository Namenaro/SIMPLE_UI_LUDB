from ax_plotter import plot_lead

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class UI:
    def __init__(self, signals, leads_names, diagnosis):
        self.diagnosis = diagnosis
        self.signals = signals
        self.leads_names = leads_names

        self.root = tk.Tk()
        self.root.state('zoomed')  # Запускаем окно в полноэкранном режиме
        self.root.title("Просмотрщик ЭКГ")

        # Создаем верхний и нижний фреймы
        self.top_frame = ttk.Frame(self.root)
        self.bottom_frame = ttk.Frame(self.root)

        # Распределяем фреймы в пропорции 0.7 к 0.3
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=False)


        # Создаем графики на верхнем фрейме
        self.create_plots(self.top_frame)

        # Создаем нижний фрейм с левой и правой частями
        self.create_bottom_panel(self.bottom_frame)
        # Привязываем обработчик события изменения размера окна
        self.root.bind("<Configure>", self.update_frames)
        self.update_frames()
        # Запускаем главный цикл
        self.root.mainloop()

    def update_frames(self, event=None):
        self.top_frame.config(height=self.root.winfo_height() * 0.8)
        self.bottom_frame.config(height=self.root.winfo_height() * 0.2)

    def get_MAX_MIN_Y(self):
        mins = []
        maxs = []
        for signal in self.signals:
            mins.append(np.min(signal))
            maxs.append(np.max(signal))
        overall_min = min(mins)
        overall_max = max(maxs)
        return overall_max, overall_min

    def create_plots(self, parent):

        n = len(self.leads_names)

        # Вычисляем высоту каждого рисунка как долю от высоты верхнего фрейма
        plot_height = 2.0 / n  # Высота каждого графика (в дюймах)
        Y_max, Y_min = self.get_MAX_MIN_Y()
        for i in range(n):
            signal = self.signals[i]
            name = self.leads_names[i]
            fig = plt.Figure(figsize=(6, plot_height))  # Ширина 6, высота plot_height
            ax = fig.add_subplot(111)  # Один подграфик на рисунке

            plot_lead(ax=ax, signal_mV=signal, line_width = 1, sample_rate=500, Y_max=Y_max, Y_min=Y_min)#Y_max=None, Y_min=None) или #Y_max=Y_max, Y_min=Y_min)

            # Встраиваем рисунок в tkinter
            canvas = FigureCanvasTkAgg(fig, master=parent)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10)

    def create_bottom_panel(self, parent):
        """Создает нижний фрейм с кнопками и текстовыми полями."""
        # Левый фрейм для кнопок
        left_frame = ttk.Frame(parent)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        # Правая часть для текстовых полей
        right_frame = ttk.Frame(parent)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Создаем кнопки в левом фрейме
        button1 = ttk.Button(left_frame, text="Кнопка 1")
        button1.pack(side=tk.TOP, fill=tk.Y, expand=True, padx=10, pady=10)

        button2 = ttk.Button(left_frame, text="Кнопка 2")
        button2.pack(side=tk.TOP, fill=tk.Y, expand=True, padx=10, pady=10)

        # Создаем текстовые поля в правом фрейме

        entry1 =  tk.Text(right_frame, wrap=tk.WORD)
        entry1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        entry1.insert(tk.END, "Диагноз врача: " + str(self.diagnosis))


        entry2 = ttk.Entry(right_frame)
        entry2.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

# Пример использования
if __name__ == "__main__":
    pass