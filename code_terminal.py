# subprocess permet d'avoir accès à toutes les commandes bash de terminal
import subprocess

# Ancienne version : Popen
# Nouvelle version : run()

while True:
    commande = input("Commande : ")
    if commande == "exit":
        print("Arrêt du terminal")
        break
    
    result = subprocess.run(commande, shell="True", capture_output=True, universal_newlines=True)
    
    print(result.stdout)
    print(result.stderr)