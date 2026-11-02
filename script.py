import re

while True:
	mdp = input("Entrez un mot de passe : ")

	if re.fullmatch(r".{6,11}", mdp) is None:
		print("Le mot de passe doit contenir au moins 6 caractères et moins de 12.")
		continue

	if re.fullmatch(r".*\d.*", mdp) is None:
		print("Le mot de passe doit contenir au moins une chiffre.")
		continue

	if re.fullmatch(r".*[A-Z].*", mdp) is None:
		print("Le mot de passe doit contenir au moins une lettre majuscule.")
		continue

	if re.fullmatch(r".*[a-z].*", mdp) is None:
		print("Le mot de passe doit contenir au moins une lettre minuscule.")
		continue

	if re.fullmatch(r".*[#%{}@!].*", mdp) is None:
		print("Le mot de passe doit contenir au moins un des caractères suivants : # % { } @")
		continue

	print("\nMot de passe valide.")
	break

