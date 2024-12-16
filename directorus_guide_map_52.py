import tkinter as tk
from tkintermapview import TkinterMapView

# Создание главного окна
root = tk.Tk()
root.title("Pie-Rise // Справочник-путеводитель")

# Создание виджета карты
map_view = TkinterMapView(root, width=800, height=600, corner_radius=0)
map_view.pack(fill="both", expand=True)

# Установка начального местоположения и уровня масштабирования
map_view.set_position(48.3357600, 38.0532500) # Санкт-Петербург
map_view.set_zoom(17)

# Добавление маркера
map_view.set_marker(48.3357600, 38.0532500, "Горловка")

# Запуск главного цикла приложения
root.mainloop()