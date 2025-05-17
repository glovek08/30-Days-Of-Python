# Create a file named mydata2.txt
# Open file without 'with'
# Catch FileNotFoundError
# In else print contents
# In finally
# Open nonexistent file mydata3.txt

def print_file_content(path: str=""):
    if not path:
        return 0
    try:
        file = open(path, 'r')
    except FileNotFoundError:
        print(f"Couldn't open file at \"/{path}\"")
    else:
        print(file.read())
    finally:
        print("I'm inside finally!")

print_file_content("mydata22.txt")