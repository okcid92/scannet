import tkinter as tk
import socket
import subprocess
import platform
import threading
from tkinter import messagebox, filedialog

class SimpleScannerReseau:
    def __init__(self, root):
        self.root = root
        self.root.title("Scanet_Dicko")
        self.root.geometry("600x500")

        self.creer_interface()

    def creer_interface(self):
        # Titre
        tk.Label(self.root, text="Scanner de Réseau (Dicko Alou)", 
                 font=("Arial", 14)).pack(pady=10)

        # Plage IP
        tk.Label(self.root, text="Plage IP à scanner:").pack()
        self.ip_entry = tk.Entry(self.root, width=40)
        self.ip_entry.pack(pady=5)
        self.ip_entry.insert(0, self.get_ip_local())

        # Boutons
        tk.Button(self.root, text="Scanner", 
                  command=self.lancer_scan).pack(pady=5)
        tk.Button(self.root, text="Sauvegarder", 
                  command=self.sauvegarder_resultats).pack(pady=5)

        # Zone de résultats
        self.resultats = tk.Text(self.root, height=20, width=70)
        self.resultats.pack(pady=10)

    def get_ip_local(self):
        """Récupère l'adresse IP locale par défaut"""
        try:
            # Crée un socket temporaire pour récupérer l'IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            # Convertit en plage /24
            return '.'.join(ip.split('.')[:-1]) + '.0/24'
        except:
            return '192.168.1.0/24'

    def ping_ip(self, ip):
        """Teste la connectivité d'une IP"""
        try:
            # Détecte le système d'exploitation
            if platform.system().lower() == "windows":
                cmd = ['ping', '-n', '2', '-w', '2000', str(ip)]
            else:
                cmd = ['ping', '-c', '2', '-W', '2', str(ip)]

            # Exécute la commande ping
            resultat = subprocess.run(cmd, capture_output=True, text=True, timeout=3)
            return resultat.returncode == 0
        except:
            return False

    def lancer_scan(self):
        # Effacer les résultats précédents
        self.resultats.delete(1.0, tk.END)
        
        # Récupérer la plage IP
        plage_ip = self.ip_entry.get()
        
        try:
            # Extraire les parties de l'adresse IP pour générer les adresses
            ip_base = '.'.join(plage_ip.split('.')[:-1]) + '.'
            debut = 1
            fin = 254
            
            # Message de démarrage
            self.resultats.insert(tk.END, f"Scan de {plage_ip} en cours...\n")
            self.root.update()

            # Liste pour stocker les résultats
            resultats_scan = []

            # Scanner chaque IP
            for i in range(debut, fin + 1):
                ip = f"{ip_base}{i}"
                if self.ping_ip(ip):
                    resultat = f"Appareil trouvé : {ip}"
                    self.resultats.insert(tk.END, resultat + "\n")
                    self.root.update()
                    resultats_scan.append(ip)

            # Message de fin
            self.resultats.insert(tk.END, f"\nScan terminé. {len(resultats_scan)} appareils trouvés.")
            
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def sauvegarder_resultats(self):
        """Sauvegarde les résultats dans un fichier"""
        try:
            # Ouvrir une boîte de dialogue pour choisir l'emplacement
            fichier = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Fichiers texte", "*.txt")]
            )
            
            if fichier:
                with open(fichier, 'w') as f:
                    f.write(self.resultats.get(1.0, tk.END))
                messagebox.showinfo("Succès", "Résultats sauvegardés !")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

def main():
    root = tk.Tk()
    app = SimpleScannerReseau(root)
    root.mainloop()

if __name__ == "__main__":
    main()
