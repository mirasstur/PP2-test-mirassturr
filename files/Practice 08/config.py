print("RUNNING FILE")
import os
print("FILE PATH:", __file__)
def load_config(filename='database.ini', section='postgresql'):
    from configparser import ConfigParser
    import os

    parser = ConfigParser()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)

    parser.read(file_path)
    print("FILES READ:", parser.read(file_path))
    print("SECTIONS:", parser.sections())

    if parser.has_section(section):
        params = parser.items(section)
        return {k: v for k, v in params}
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    
    