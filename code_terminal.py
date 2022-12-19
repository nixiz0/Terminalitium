# subprocess permet d'avoir accès à toutes les commandes bash de terminal
import subprocess

# Ancienne version : Popen
# Nouvelle version : run()
result = subprocess.run("dir", shell="True", capture_output=True, universal_newlines=True)

print(result.stdout)