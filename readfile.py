def modify_file_contents(contents):
    # Example modification: convert all text to uppercase
    return contents.upper()

def read_and_write_file():
    input_filename = input("Enter the filename to read: ")
    
    try:
        with open(input_filename, 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
        return
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
        return

    modified_contents = modify_file_contents(contents)
    
    output_filename = "modified_" + input_filename
    try:
        with open(output_filename, 'w') as file:
            file.write(modified_contents)
    except IOError:
        print(f"Error: The file '{output_filename}' could not be written.")
        return
    
    print(f"Modified contents written to '{output_filename}' successfully!")

# Execute the program
read_and_write_file()

