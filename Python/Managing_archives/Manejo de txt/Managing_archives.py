def read_and_sort_file(input_file, output_filename):
    try:
        with open(input_file, 'r',  encoding='utf-8') as f:
            lines = f.read().splitlines() 
        lines.sort()


        with open(output_filename, 'w' , encoding='utf-8') as file:
            file.write('\n'.join(lines))
        
        print(f"File '{input_file}' sorted and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: No tienes permisos para acceder a '{input_file}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")


read_and_sort_file('my_file.txt', 'ordered.txt')




