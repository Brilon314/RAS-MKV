import os
import subprocess
import re

# Obtiene la cantidad de capítulos contando los archivos MKV en el directorio
caps = sum(1 for file in os.listdir() if file.endswith(".mkv"))
if caps == 0:
    print("No se encontraron archivos MKV en el directorio.")
    exit()


nombre = None
temporada = None

# Expresión regular para encontrar patrones como "S01E01" en el nombre del archivo
pattern = re.compile(r'S\d{2}E\d{2}', re.IGNORECASE)

for file in os.listdir():
    if file.endswith(".mkv"):
        base_name = os.path.splitext(file)[0]
        match = pattern.search(base_name)
        if match:
            found_pattern = match.group()
            nombre = base_name.split(found_pattern)[0] + found_pattern[:4]
            temporada = found_pattern[1:3]
            break

if nombre is None or temporada is None:
    print("No se encontraron archivos MKV en el directorio.")
    exit()



def remove_subtitles(caps, nombre):
    for i in range(1, caps + 1):
        if i < 10:
            input_movie = f"{nombre}0{i}.mkv"
            input_subtitle = f"{nombre}0{i}.srt"
            output_filename = f"{nombre}0{i}m.mkv"
        else:
            input_movie = f"{nombre}{i}.mkv"
            input_subtitle = f"{nombre}{i}.srt"
            output_filename = f"{nombre}{i}m.mkv"
        
        # Merge without subtitles
        merge_command = f"mkvmerge -o \"{output_filename}\" -S \"{input_movie}\""
        
        if os.system(merge_command) == 0:
            print(f"Subtitulo eliminado de {input_movie} a {output_filename}")
        else:
            print(f"Fallo al eliminar el subtitulo de {input_movie}")

def add_subtitle(caps, nombre):
    for i in range(1, caps + 1):
        if i < 10:
            input_movie = f"{nombre}0{i}m.mkv"
            input_subtitle = f"{nombre}0{i}.srt"
            output_filename = f"{nombre}0{i}.mkv"
        else:
            input_movie = f"{nombre}{i}m.mkv"
            input_subtitle = f"{nombre}{i}.srt"
            output_filename = f"{nombre}{i}.mkv"
        
        # Merge with subtitles
        merge_command = f"mkvmerge -o \"{output_filename}\" --default-track 3 --sub-charset 0:ISO-8859-15 --language 3:spa \"{input_subtitle}\" \"{input_movie}\""
        
        process = subprocess.Popen(merge_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 1:
            print(f"Subtitulo agregado a {input_movie} con {input_subtitle} a {output_filename}")
        else:

            print(process.returncode)
            print(f"Fallo al agregar a {input_movie} el subtitulo {input_subtitle}")
            # print("Salida estándar:", stdout)
            print("Error estándar:", stderr)
        
        # Remove input files
        os.remove(input_movie)
        os.remove(input_subtitle)


print("Cantidad de capis: "+str(caps))
print("Nombre base: "+nombre)

# Llamada a la función con los valores deseados
remove_subtitles(caps, nombre)
# Llamada a la función con los valores deseados
add_subtitle(caps, nombre)
