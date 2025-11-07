class AudioSystem:
    def configurar_audio(self):
        print("Configurando el audio...")
    def ajustar_volumen(self, volumen):
        print(f"Ajustando el volumen a {volumen}% ...")
    
class VideoSystem:
    def configurar_video(self):
        print("Configurando el video...")
    def ajustar_resolucion(self, resolucion):
        print(f"Ajustando la resolución a {resolucion} píxeles...")

class StreamingService:
    def conectar(self):
        print("Conectándose al servicio de streaming...")
    def iniciar(self, pelicula):
        print(f"Iniciando la película {pelicula}...")
    
class HomeTheaterFacade:
    def __init__(self):
        self.audio = AudioSystem()
        self.video = VideoSystem()
        self.streaming = StreamingService()

    def ver_pelicula(self, pelicula):
        print("Iniciando sistema de películas...\n")
        self.audio.configurar_audio()
        self.audio.ajustar_volumen(40)
        self.video.configurar_video()
        self.video.ajustar_resolucion(1080)
        self.streaming.conectar()
        self.streaming.iniciar(pelicula)
        print("\nTodo hecho, disfrute su película.")

if __name__ == "__main__":
    home_theater = HomeTheaterFacade()
    home_theater.ver_pelicula("Avengers End Game")