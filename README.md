# sg

This project allows user to define json structure for creating sqlite3 database as defined in the json file.
Make sure that the json structure is same as the given structure.
Current state = Alpha development
Have following project structure

your project
    |
    |json_folder
        |
        |json_files
    main.py 


Use the code givnen in schema.py to run
sg.main import main
main('json_file_source', 'path_to_store_db_file')

Example
main('src', 'dist')

You can use json from example_json folder
