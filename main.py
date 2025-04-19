import os
import numpy as np
from PIL import Image
from matplotlib.colors import LinearSegmentedColormap
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time

# Eigene Colormap definieren
custom_colors = ["#2C3E50", "#2980B9", "#27AE60", "#E74C3C", "#8E44AD"]  # Dunkle, kontrastreiche Farben
custom_colormap = LinearSegmentedColormap.from_list("custom_colormap", custom_colors)

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, files):
        self.files = [os.path.abspath(file) for file in files]

    def on_modified(self, event):
        if os.path.abspath(event.src_path) in self.files:
            print(f"Änderung erkannt: {event.src_path}")
            generate_wordcloud(self.files)


def generate_wordcloud(files):
    text = ''
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            text += f.read()

    # Maske laden (Kreuz-Bild)
    mask = np.array(Image.open("kreuz.png"))

    wordcloud = WordCloud(
        width=1920,
        height=1080,
        background_color="#FFE4D6",
        colormap=custom_colormap,
        max_font_size=200,
        min_font_size=10,
        max_words=100,
        mask=mask,  # Maske anwenden
        contour_color="black",  # Optional: Konturfarbe
        contour_width=0,  # Optional: Konturbreite
        font_path=None
    ).generate(text)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    wordcloud.to_file("wordcloud.png")
    print("Wortwolke wurde aktualisiert und gespeichert.")


if __name__ == '__main__':
    files_to_watch = ["input1.txt", "input2.txt"]
    event_handler = FileChangeHandler(files=files_to_watch)
    observer = Observer()
    for file in files_to_watch:
        observer.schedule(event_handler, path=os.path.dirname(os.path.abspath(file)), recursive=False)

    observer.start()
    print("Überwachung gestartet. Änderungen an den Dateien werden erkannt.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()