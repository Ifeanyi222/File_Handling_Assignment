# Write to file
file = open("my_file.txt", "w")
file.write("Welcome to file handling line 1 \n")
file.write("This is line 2 with numbers: 12345\n")
file.write("The third line contains a mix of strings and numbers like 3.14.\n")
file.close()


# Read and display the content of the file
f = open("my_file.txt", "r")
content=f.read()
print(content)
f.close()


#File Appending
ff=open("my_file.txt", "a")
ff.write("My name is Linus\n")
ff.write("you are a student of PLP\n")
ff.write("Located in Africa\n")
ff.close()



#Error Handling
try:
    # Append to the file
    with open("my_file.txt", "a") as file:
        file.write("This is line 4 appended to the file.\n")
        file.write("Fifth line includes a date: 2024-03-26\n")
        file.write("Last line has some special characters like @, $, and !\n")
except FileNotFoundError:
    print("File not found. Please check the file path.")
except PermissionError:
    print("Permission denied. You do not have permission to access the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Read and display the updated contents of the file
    try:
        with open("my_file.txt", "r") as file:
            updated_content = file.read()
            print(updated_content)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
