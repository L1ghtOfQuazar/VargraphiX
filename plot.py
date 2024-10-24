import time
import sys
import os
import os
def plot2d(x, y, x1, y1, col):
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    f = open("plot2d.m", "w+", encoding='utf-8')
    f.write(f'plot({y}, {x}, {col})\n')
    f.write("xlabel('"+ y1 + "')\n")
    f.write("ylabel('"+ x1 + "')\n")
    f.write(f'pause')
    f.close()
    os.popen("Taskkill /IM octave.exe /F")
    os.popen("Taskkill /IM octave-gui.exe /F")
    time.sleep(1)
    os.popen("octave plot2d.m")

def plot3d(x, y, z, x1, y1, z1, col):
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    z = [float(i) for i in z]
    f = open("plot3d.m", "w+", encoding='utf-8')
    f.write(f'plot3({x}, {y}, {z}, {col})\n')
    f.write("xlabel('" + x1 + "')\n")
    f.write("ylabel('" + y1 + "')\n")
    f.write("zlabel('" + z1 + "')\n")
    f.write(f'grid on\n')
    f.write(f'pause')
    f.close()
    os.popen("Taskkill /IM octave.exe /F")
    os.popen("Taskkill /IM octave-gui.exe /F")
    time.sleep(1)
    os.popen("octave plot3d.m")

def plot_bar(labels, values, col):
    f = open("plot_bar.m", "w+", encoding='utf-8')
    f.write(f'bar({values}, {col})\n')
    f.write("xlabel('Номера элементов')\n")
    f.write("ylabel('" + labels + "')\n")
    f.write(f'pause')
    f.close()
    os.popen("Taskkill /IM octave.exe /F")
    os.popen("Taskkill /IM octave-gui.exe /F")
    time.sleep(1)
    os.popen("octave plot_bar.m")

def plot_pie(labels, values, n):
    #values = [float(i) for i in values]
    f = open("plot_pie.m", "w+", encoding='utf-8')
    f.write(f'pie({values},{labels})\n')
    f.write(f'legend({labels})\n')
    f.write("title('" + str(n) + "')\n")
    f.write(f'pause')
    f.close()
    os.popen("Taskkill /IM octave.exe /F")
    os.popen("Taskkill /IM octave-gui.exe /F")
    time.sleep(1)
    os.popen("octave plot_pie.m")
