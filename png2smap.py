from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

heightmap_out = []
typemap_out = []
shadermap_out = []
heightmapfile = askopenfilename(title="Select heightmap...", filetypes=[("PNG Files", "*.png")])
typemapfile = askopenfilename(title="Select typemap...", filetypes=[("PNG Files", "*.png")])
shadermapfile = askopenfilename(title="Select shadermap...", filetypes=[("PNG Files", "*.png")])
hmap = Image.open(heightmapfile)
tmap = Image.open(typemapfile)
smap = Image.open(shadermapfile)
for x in range(hmap.size[0]):
    for y in range(hmap.size[1]):
        height = str(hmap.getpixel((x, y)))
        heightmap_out.append(height)
for x in range(tmap.size[0]):
    for y in range(tmap.size[1]):
        pixel_color = tmap.getpixel((x, y))
        pixel_type = "0"
        if pixel_color == (0, 255, 0):
            pixel_type = "0"
        elif pixel_color == (0, 0, 255):
            pixel_type = "1"
        elif pixel_color == (0, 127, 0):
            pixel_type = "2"
        typemap_out.append(pixel_type)
for x in range(smap.size[0]):
    for y in range(smap.size[1]):
        shading = str(hmap.getpixel((x, y)))
        shadermap_out.append(shading)
smapfile = asksaveasfilename(title="Save as...", filetypes=[("SMAP Files", "*.smap")])
with open(smapfile, 'w') as f:
    f.truncate(0)
    f.write(str(hmap.size[0]) + '\n')
    f.write(str(hmap.size[1]) + '\n')
    for heightvalue in heightmap_out:
        f.write(heightvalue + '\n')
    f.write(str(tmap.size[0]) + '\n')
    f.write(str(tmap.size[1]) + '\n')
    for typevalue in typemap_out:
        f.write(typevalue + '\n')
    f.write(str(smap.size[0]) + '\n')
    f.write(str(smap.size[1]) + '\n')
    for shadingvalue in shadermap_out:
        f.write(shadingvalue + '\n')
