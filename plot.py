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

'''oc = Oct2Py()
script = "plot(rand(1,10))"
with open("myScript.m","w+") as f:
    f.write(script)
oc.myScript()'''