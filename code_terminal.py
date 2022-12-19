# subprocess permet d'avoir accès à toutes les commandes bash de terminal
import subprocess

# Ancienne version : Popen
# Nouvelle version : run()
subprocess.run("dir", shell="True")
