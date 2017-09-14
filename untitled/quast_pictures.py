__author__ = 'dima'
from wand.image import Image
from wand.color import Color
import sys

path_to_quast_folder = sys.argv[1]
prefix = ""
if(len(sys.argv) == 3) :
    prefix = sys.argv[2] + "_"

with Image(filename=path_to_quast_folder + "basic_stats/Nx_plot.pdf", resolution=300) as img:
  with Image(width=img.width, height=img.height, background=Color("white")) as bg:
    bg.composite(img,0,0)
    bg.save(filename=prefix+"Nx_plot.png")

with Image(filename=path_to_quast_folder + "basic_stats/cumulative_plot.pdf", resolution=300) as img:
  with Image(width=img.width, height=img.height, background=Color("white")) as bg:
    bg.composite(img,0,0)
    bg.save(filename=prefix+"cumulative_plot.png")