
import os

def local_dict(directory):
    data_dict = {}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("_chinese.yml"):
                file_path = os.path.join(root, file)
                # Process the file data here
                # Add the processed data to the dictionary
                # For example:
                with open(file_path, 'r',encoding='UTF-8') as f:
                    file_data = f.read()
                    if len(file_data.split("l_simp_chinese:"))==1:
                        continue
                    # Process the file_data as needed
                    # For example, you can split each line by ':' and add it to the dictionary
                    processed_data = file_data.split("l_simp_chinese:")[1]
                    #data_dict[file_path] = processed_data
                    for line in processed_data.split('\n'):
                        if line.strip():  # Check if the line is not empty
                            if '#' in line: 
                                continue
                            key, value = line.split(':', 1)
                            data_dict[key.strip()] = value.strip().lstrip('0').replace('$', '%')
                            # Replace all occurrences of '$' with '%'

                    # Process the file_data as needed
                    # For example, you can parse the YAML data using a library like PyYAML
                    # and add it to the dictionary
                    # data_dict[file_path] = processed_data
                

    return data_dict
#data_dict=process_files("E://lqz//git//Ethics-Civics-Infinity-new//localisation")
#with open('test.txt','w',encoding='UTF-8')as f:
#    f.write(str(data_dict))