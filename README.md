# read_and_modify_file
Python script that reads the contents of a user-specified file, modifies the content and writes the result to a new file


🖋️ FILE READ AND WRITE WITH HANDLING ERROR
This Python script reads the contents of a user-specified file, modifies the content (e.g., converts it to uppercase), and writes the result to a new file. It also includes error handling for missing or unreadable files.


📦 FEATURES
1. Asks the user for the name of a file to read

2. Handles errors (e.g., file not found or access denied)

3. Converts the file's text to uppercase

4. Saves the modified content to a new file prefixed with modified_




🧰 REQUIREMENTS
1. Python 3.x

2. A text file to test with




🚀 HOW TO RUN
1. Save the script in a file called, for example, file_modifier.py.

2. Open your terminal or command prompt.

3. Navigate to the folder where your script is saved.

4. Run the script:
    python file_modifier.py

5. When prompted, enter the name of a text file that exists in the same directory (e.g., sample.txt).




❗ ERROR HANDLING

If the file doesn’t exist:
javascript:
Error: The file 'missing.txt' does not exist.

If the file can't be read or written:
pgsql:
Error: Could not read from 'example.txt' or write to the new file.




🔧 CUSTOMIZATION IDEAS
-You can modify the script to:

-Reverse each line instead of uppercasing

-Strip whitespace or punctuation

-Replace words or add line numbers

-Log operations to a separate log file





📂 OUTPUT FILE
-The output file is saved in the same directory as the input.

-It is named modified_<original_filename>.



