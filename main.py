import turtle
import turtle as t
import random

# package imported for extraction of colors from a picture
import colorgram

t.speed("fastest")
t.colormode(255)

# below method is used to on accepting rgb color for tutrtle

# def random_Color():
#   R=random.randint(0,255)
#   G=random.randint(0,255)
#   B=random.randint(0,200)
#   # Below we created a tupple to return values of random RGB color
#   RGB=(R,G,B)
#   return RGB
# t.pensize(1)

# First Way to create Spirograph
# while True:
#  #    through heading method we can know the position of our tortule
#  print(t.heading())
#  R,G,B=random_Color()
#  t.circle(100)
#  t.right(5)
#  t.color(R,G,B)
#  if t.heading()==0:
#     break
#
#
#
#
#
#
# t.color('red', 'yellow')
# t.begin_fill()
# while True:
#     t.forward(200)
#     t.left(170)
#     if abs(t.pos()) < 1:
#         break
# t.end_fill()
# t.done()


# Drawing The paintings
extracted_color = colorgram.extract('image.jpg', 30)
# it returns a list and inside that a tupple with rgb colors
# print(extracted_color)
# t.exitonclick()
# color1=extracted_color[0]
# print(color1)
#
# (r,g,b)=color1.rgb
# print((r,g,b))
# colors_list=[]
#
# # 1st way to take rgb values from list and make tupple of it
# # for i in range(0,len(extracted_color)):
# #     color=extracted_color[i]
# #     (r,g,b)=color.rgb
# #     colors_list.append((r,g,b))
# #     # below line was for testing
# #     # print(f"test {colors_list}")
# # print(colors_list)
# # 2nd way to take rgb values from list and make tupple of it
# for i in extracted_color:
#    r=i.rgb.r
#    g=i.rgb.b
#    b=i.rgb.b
#    hell=(r,g,b)
#    colors_list.append(hell)
#
# print(colors_list)
# # colors extracted from above picture drawing a random line to check the colors
# # for i in range(1,10):
# #     t.forward(20)
# #     random_color=random.choice(colors_list)
# #     t.color(random_color)
# #     t.pensize(20)
t.speed("fastest")
t.penup()
t.goto(200,200)
#  below are the colors extracted from picture so we created list and append the tupples inside it
colors_list=[(204, 122, 122), (196, 159, 159), (241, 226, 226), (226, 230, 230), (227, 241, 241), (148, 186, 186), (148, 67, 67), (231, 183, 183), (237, 158, 158), (220, 141, 141), (147, 156, 156), (189, 86, 86), (183, 115, 115), (145, 97, 97), (167, 69, 69), (182, 214, 214), (170, 182, 182), (82, 96, 96), (99, 110, 110), (99, 128, 128), (158, 214, 214), (117, 149, 149), (130, 56, 56), (88, 15, 15), (118, 26, 26), (97, 20, 20), (90, 152, 152), (78, 43, 43), (60, 68, 68)]

t.right(180)
for i in range(0,10):
    for x in range(0,10):
      t.color(random.choice(colors_list))
      t.penup()
      t.dot(20)
      t.forward(50)
      t.pendown()
    t.right(180)
    for i in range(0,10):
     t.penup()
     t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)



t.exitonclick()


# for i in range(len(extracted_color)):
#     colors = extracted_color[i]
    # extracted_color_list=colors.rgb+extracted_color_list
    # print(colors.rgb)
    # (r, g, b) = colors.rgb
#     # print(r, g, b)
# print(extracted_color_list)