import tkinter as tk
import math
import colorsys

root = tk.Tk()
root.title("Show")

canvas_width = 1000
canvas_height = 1000
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

center_x = canvas_width // 2
center_y = canvas_height // 2

angle = 0
radius = 400
step = 0
spiral_count = 6
history = []


def draw():
    global angle, radius, step

    canvas.delete("all")
    for h in history[-600:]:
        x, y, color, size = h
        canvas.create_oval(x, y, x + size, y + size, fill=color, outline=color)

    for i in range(spiral_count):
        offset = (2 * math.pi / spiral_count) * i
        r = radius * (1 + 0.1 * math.sin(step * 0.05 + i))
        a = angle + offset

        x = center_x + math.cos(a) * r
        y = center_y + math.sin(a) * r

        hue = ((step + i * 40) % 360) / 360
        r_, g_, b_ = colorsys.hsv_to_rgb(hue, 1, 1)
        color = f'#{int(r_ * 255):02x}{int(g_ * 255):02x}{int(b_ * 255):02x}'

        size = 4 + 3 * math.sin(step * 0.1 + i)
        history.append((x, y, color, size))

    angle += 0.12
    radius *= 0.995 + 0.002 * math.sin(step * 0.02)
    step += 1

    root.after(10, draw)


draw()
root.mainloop()
