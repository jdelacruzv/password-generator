import random
import string


def generate_password(pass_length):
	characters = string.ascii_letters + string.digits + string.punctuation
	password = random.sample(characters, pass_length)
	return password


def main():
	while True:
		pass_length = input("Ingrese longitud de la contraseña (>=8 y <=94 ): ")		
		try:
			pass_length = int(pass_length)
			if pass_length >= 8 and pass_length <= 94:
				generated_password = "".join(generate_password(pass_length))
				print("Contraseña generada:", generated_password)
				break
			else:
				print(f"Longitud {pass_length} fuera del rango, inténtalo de nuevo")
		except:
			print("Entrada inválida")


main()