

import matplotlib.pyplot as plt
import numpy as np
import math


def plot_lead(signal_mV, ax, Y_max=None, Y_min=None, line_width = 1, sample_rate=500):
    if Y_max is None:
        Y_max = max(signal_mV) + 0.1

    if Y_min is None:
        Y_min = min(signal_mV) -0.1
    # Создаем маленькую сетку
    cell_time = 0.04 # Один миллметр по оси времени соотв. 0.04 секунды
    cell_voltage = 0.1 # один миллиметр по оси напряжения соответ. 0.1 милливольта

    x = np.arange(0, len(signal_mV), dtype=np.float32) / sample_rate
    _x_min = float(x[0])
    _x_max = float(x[-1] + 1 / sample_rate)

    x_min = math.ceil(_x_min / cell_time) * cell_time
    ax.set_xticks(np.arange(x_min, _x_max , cell_time), minor=True)

    y_min = math.ceil(Y_min / cell_voltage) * cell_voltage
    ax.set_yticks(np.arange(y_min, Y_max, cell_voltage), minor=True)


    #Создаем большую сетку
    cell_time_major = 0.2
    cell_voltage_major = 0.5

    x_min = math.ceil(_x_min / cell_time_major) * cell_time_major
    y_min = math.ceil(Y_min / cell_voltage_major) * cell_voltage_major

    ax.set_xticks(np.arange(x_min, _x_max , cell_time_major))
    ax.set_yticks(np.arange(y_min, Y_max, cell_voltage_major))

    # Включаем сетки
    ax.grid(True, which='minor', linestyle=':', linewidth=0.5, color='gray')
    ax.grid(True, which='major', linestyle='-', linewidth=0.8, color='gray')

    # ограничиваем рисунок
    ax.set_xlim(_x_min, _x_max)
    ax.set_ylim(Y_min, Y_max)

    # Названия к осям
    #ax.set_xlabel("Секунды")
    ax.set_ylabel("мВ")

    # Убираем подписи осей для чистоты
    ax.set_xticklabels([])
    #ax.set_yticklabels([])

    # Устанавливаем  масштаб по осям
    aspect = cell_time / cell_voltage
    ax.set_aspect(aspect)


    ax.plot(x, signal_mV,
            linestyle='-',  # Сплошная линия
            linewidth=line_width,  # Толщина линии
            alpha=0.9,  # Полупрозрачная линия
            #marker='o',  # Маркеры в виде кружков
            #markersize=line_width +0.1,  # Размер маркеров (диаметр кружков)
            #markerfacecolor='black',  # Цвет заливки маркеров
            #markeredgecolor='black',  # Цвет границы маркеров
            #markeredgewidth=0  # Толщина границы маркеров (0 — без границы))
            )


def plot_delineation(ax, delineation, Y_max, color='red', sample_rate=500):
    for x in delineation:
        ax.axvline(x=x/sample_rate, ymax=Y_max, ymin=0, color=color, linewidth=0.5)