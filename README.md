# ras-mkv
## Remove and Add Subtitles to MKV files
Este pequeño script en Python 3 automatiza dos pasos importantes para mejorar la experiencia de visualización de tus series en formato MKV. En primer lugar, elimina automáticamente todos los subtítulos incrustados en los archivos MKV dentro del directorio. Luego, agrega subtítulos en español con la codificación adecuada de modo que los caracteres con tildes y letras latinas se vean correctamente.

Para utilizar el script de manera eficiente, se recomienda seguir un formato de nomenclatura específico para los archivos MKV y SRT. Puedes nombrar tus archivos de esta manera: "Nombre de la Serie (Año de Lanzamiento) S0XE0X". Por ejemplo, "The Sandman (2022) S01E01.mkv" para el video y "The Sandman (2022) S01E01.srt" para el subtítulo correspondiente.

Para ejecutar el script, sigue estos pasos:

1. Coloca el script en la misma carpeta donde se encuentran tus archivos MKV y SRT.
2. Abre una terminal en ese directorio (puedes navegar a la ubicación del directorio y hacer clic con el botón derecho para abrir una terminal).
3. En la terminal, ejecuta el siguiente comando para invocar el script usando Python 3:
python3 ras-mkv.py
