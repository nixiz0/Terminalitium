# subprocess permet d'avoir accès à toutes les commandes bash de terminal
import subprocess
import os

# Ancienne version : Popen
# Nouvelle version : run()

#os.getcwd() permet d'avoir le chemin d'accès au dossier où l'on se trouve
#os.chdir(..) permet de changer de directory (de dossier)

while True:
    commande = input(os.getcwd() + " --8> ")
    if commande == "exit":
        print("Arrêt du terminal")
        break

    commande_split = commande.split(" ")
    if len(commande_split) == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1])
        except FileNotFoundError:
            print("ERREUR : chemin inexistant ")
    else:
        result = subprocess.run(commande, shell="True", capture_output=True, universal_newlines=True)
        
        print(result.stdout)
        print(result.stderr)