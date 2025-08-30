def format(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print_formatted = format("anuj", "nalaWade")
print(print_formatted)