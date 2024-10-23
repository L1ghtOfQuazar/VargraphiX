from oct2py import Oct2Py
import subprocess
import sys
import os
import os
def plot2d(x, y):
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    f = open("plot2d.m", "w+")
    f.write(f'plot({y}, {x})\n')
    f.write(f'pause')
    f.close()
    os.popen("octave plot2d.m")

def plot3d(x, y, z):
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    z = [float(i) for i in z]
    f = open("plot3d.m", "w+")
    f.write(f'plot3({x}, {y}, {z})\n')
    f.write(f'grid on\n')
    f.write(f'pause')
    f.close()
    os.popen("octave plot3d.m")

def plot_bar(labels, values):
    values = [float(i) for i in values]
    f = open("plot_bar.m", "w+")
    f.write(f'bar({values})\n')
    f.write(f'set(gca, "xtick", 1:{len(labels)}, "xticklabel", {labels})\n')
    f.write(f'pause')
    f.close()
    os.popen("octave plot_bar.m")

def plot_pie(labels, values):
    values = [float(i) for i in values]
    f = open("plot_pie.m", "w+")
    f.write(f'pie({values})\n')
    f.write(f'legend({labels})\n')
    f.write(f'pause')
    f.close()
    os.popen("octave plot_pie.m")

'''oc = Oct2Py()
script = "plot(rand(1,10))"
with open("myScript.m","w+") as f:
    f.write(script)
oc.myScript()'''
