# Importa la librería yt-dlp para descargar el audio de un video de YouTube en formato mp3
import os
import yt_dlp

CARPETA_MUSICA = "musica" # Carpeta donde se guardarán los archivos mp3

#Si no existe la carpeta, la creamos
if not os.path.exists(CARPETA_MUSICA):
    os.makedirs(CARPETA_MUSICA)

def descargar_mp3(url):
    opciones = {
        'format': 'bestaudio/best', # Descarga el mejor audio disponible
        'outtmpl': f'{CARPETA_MUSICA}/%(title)s.%(ext)s', # Guarda el archivo con el título del video
        #'optmpl': 'musica/%(title)s.%(ext)s',
        'postprocessors': [ # Convertimos el audio descargado a mp3
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
            {'key': 'EmbedThumbnail'}, # Agrega la miniatura del video como carátula del mp3
            {'key': 'FFmpegMetadata'} # Escribimos los metadata del video en el mp3
        ]
    }

    # Creamos una instancia de YoutubeDL con las opciones
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

# Solicitamos la URL del video al usuario, y llamamos la funcion descargar_mp3
if __name__ == "__main__":
    url = input("🔗 Ingresa la URL del video: ")
    descargar_mp3(url)
    print("🎵 Descarga completada.")
