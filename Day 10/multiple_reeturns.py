# #  functions with outputs

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"


# print(format_name("petER", "farETRA"))

# #  functions with outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you didnt enter your name correctly"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("petER", "farETRA"))
