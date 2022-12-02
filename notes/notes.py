# Functions with Outputs
def format_name(f_name, l_name):
# Doc strings

    """Take the first and last name and format it"""
    if f_name == "" or l_name == "":
        return "You didnt provide valid inputs."
    formated_name = f_name.title()
    formated_last_name = l_name.title()
    return f"{formated_name} {formated_last_name}"
print(format_name(input("What is your first name? "), input("What is your last name? ")))
