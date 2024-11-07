def format_name(f_name = "Barry", l_name = "Salmon"):
  
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"
  

f_name = input("What is your first name?")
l_name = input("What is your last name")
print(format_name( f_name, l_name))
