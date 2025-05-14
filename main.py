def read_and_modify_file():
    try:
        input_filename = input("Enter the name of the file to read: ")

        # Try to open and read the original file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File has been read, modified, and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read from '{input_filename}' or write to the new file.")

# Run the function
read_and_modify_file()
