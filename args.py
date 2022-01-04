
import argparse


parser = argparse.ArgumentParser(description='Program to create video from playlist or disc from Deezer')
parser.add_argument('-a', '--album', type=str, help='Parametro para agregar album')
parser.add_argument('-e', '--efect', type=str, default='player', required=False, help='Argumento proporcinar el efecto de la portada de los discos')
parser.add_argument('-f', '--font',  type=str, default='one', required=False, help='Fuenta para la letra en el video'  )
parser.add_argument('-p', '--playlist', type=str, help='Parametro para agregar playlist')
parser.add_argument('-t', '--test', action='store_true', help="Permite validar que canciones si se van a descargar")


args = parser.parse_args()





