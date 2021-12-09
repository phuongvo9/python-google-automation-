def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    return hex_color

print(color_translator("blue")) #Should be #0000fff
print(color_translator("yellow")) # should be unknown
print(color_translator("red")) #should be #ff0000
print(color_translator("black")) #shouldbe #00ff00
print(color_translator("green")) #should be #00ff00
print(color_translator("")) #should be unknown