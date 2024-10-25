import os

# Define the folder path
meets_folder = 'meets'
output_file = 'index.html'

# Ensure the folder exists
if not os.path.exists(meets_folder):
    print(f"The folder '{meets_folder}' does not exist.")
else:
    # List to store the file paths
    html_files = []

    # Walk through the folder
    for root, dirs, files in os.walk(meets_folder):
        for file in files:
            # Check if the file ends with .html
            if file.endswith('.html'):
                # Create the full path to the file
                file_path = os.path.join(root, file)
                # Append to the list
                html_files.append(file_path)
    
    # Create or open the index.html file for writing
    with open(output_file, 'w') as f:
        # Write the basic HTML structure
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>HTML Files Index</title>\n')
        f.write('<link rel="stylesheet" href="css/reset.css">\n')
        f.write('<link rel="stylesheet" href="css/style.css">\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<h1>List of HTML Files</h1>\n')
        f.write('<ul>\n')

        # Write each file path as a link
        for link in html_files:
            relative_path = os.path.relpath(link, start=os.path.dirname(output_file))
            display_name = relative_path.lstrip('meets/').rstrip('.html')
            f.write(f'<li><a href="{relative_path}">{display_name}</a></li>\n')
        
        # Close the list and the HTML tags
        f.write('</ul>\n')
        f.write('</body>\n')
        f.write('</html>\n')

    print(f"Index file created successfully at {output_file}")