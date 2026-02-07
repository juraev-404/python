import tkinter as tk
import math

class FractalTree:
    def __init__(self, root):
        self.root = root
        self.root.title("Фрактальное дерево")
        
        # Создаем фрейм для холста
        canvas_frame = tk.Frame(self.root)
        canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Создаем холст
        self.canvas = tk.Canvas(canvas_frame, width=800, height=600, bg='black')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Создаем фрейм для элементов управления 
        control_frame = tk.Frame(self.root)
        control_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Создаем слайдер для угла
        tk.Label(control_frame, text="Угол ветвления:").pack(side=tk.LEFT)
        self.angle_var = tk.DoubleVar(value=30)
        angle_slider = tk.Scale(control_frame, from_=0, to=360,
                               orient=tk.HORIZONTAL, variable=self.angle_var,
                               command=self.update_tree, length=300)
        angle_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Создаем слайдер для коэффициента длины
        tk.Label(control_frame, text="Коэффициент длины:").pack(side=tk.LEFT)
        self.length_factor_var = tk.DoubleVar(value=0.7)
        length_slider = tk.Scale(control_frame, from_=0.1, to=0.9, 
                                orient=tk.HORIZONTAL, variable=self.length_factor_var,
                                resolution=0.05, command=self.update_tree, length=300)
        length_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Начальные параметры
        self.start_x = 400
        self.start_y = 500
        self.start_length = 120
        self.max_depth = 10
        
        # Рисуем начальное дерево
        self.update_tree()
    
    def draw_tree(self, x, y, angle, length, depth):
        if depth == 0:
            return
            
        # Вычисляем конечную точку ветви
        end_x = x - length * math.sin(math.radians(angle))
        end_y = y - length * math.cos(math.radians(angle))
        
        # Рисуем ветвь
        self.canvas.create_line(x, y, end_x, end_y, width=depth/2, fill='white')
        
        # Рекурсивно рисуем следующие ветви
        self.draw_tree(end_x, end_y, angle - self.angle_var.get(), 
                      length * self.length_factor_var.get(), depth - 1)
        self.draw_tree(end_x, end_y, angle + self.angle_var.get(), 
                      length * self.length_factor_var.get(), depth - 1)
    
    def update_tree(self, event=None):
        # Очищаем холст
        self.canvas.delete("all")
        
        # Рисуем дерево
        self.draw_tree(self.start_x, self.start_y, 0, self.start_length, self.max_depth)
        
        # Добавляем информацию о параметрах
        info_text = f"Угол: {self.angle_var.get():.1f}°, Коэффициент: {self.length_factor_var.get():.2f}"
        self.canvas.create_text(400, 550, text=info_text, font=("Arial", 12))

if __name__ == "__main__":
    root = tk.Tk()
    app = FractalTree(root)
    root.mainloop()