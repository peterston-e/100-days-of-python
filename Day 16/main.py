# import turtle
#
# from another_module import var
# print(var)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse3")
#
#
# timmy.forward(10)
# timmy.right(59)
# timmy.forward(10)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",
                 ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",
                 ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

