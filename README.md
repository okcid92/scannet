# Scanet_Dicko

Application graphique Python (Tkinter) pour scanner rapidement un sous-réseau local en envoyant des requêtes `ping` et afficher les hôtes accessibles.

## Fonctionnalités

- Détection automatique de l’IP locale (proposition par défaut en `/24`)
- Scan d’un réseau IPv4 local (de `.1` à `.254`)
- Affichage en temps réel des appareils détectés
- Sauvegarde des résultats dans un fichier `.txt`
- Compatibilité Linux / Windows (commande `ping` adaptée au système)

## Structure du projet

- `Scanet_Dicko.py` : application principale (interface + logique de scan)
- `manuel_DIcko_Alou.pdf` : documentation fournie dans le dépôt

## Prérequis

- Python 3.x
- Tkinter (généralement inclus avec Python)
- Commande système `ping` disponible dans le PATH

## Lancer l’application

Depuis la racine du dépôt :

```bash
python Scanet_Dicko.py
```

## Utilisation

1. Vérifier ou modifier la plage IP proposée.
2. Cliquer sur **Scanner** pour démarrer la détection.
3. Consulter les IP trouvées dans la zone de résultats.
4. Cliquer sur **Sauvegarder** pour exporter les résultats.

## Limites actuelles

- Le scan est basé sur `ping` uniquement (pas de scan de ports/services).
- La logique actuelle parcourt un sous-réseau de type `/24`.
- Le scan s’exécute dans le thread principal, ce qui peut figer l’interface pendant l’exécution.
