#!/usr/bin/env python3
"""
read_marc.py
Lecture d'un fichier MARC binaire et affichage du titre de chaque notice.
Exemple basé sur la doc PyMARC (MARCReader + record.title).
"""
import sys
from pymarc import MARCReader

def main(path):
    # Ouvrir en binaire pour MARC (.mrc/.dat)
    with open(path, 'rb') as fh:
        reader = MARCReader(fh)
        for i, record in enumerate(reader, start=1):
            # La doc montre print(record.title) ; ici on gère None proprement
            title = getattr(record, "title", None)
            print(f"{i}: {title}" if title else f"{i}: <pas de 245$a trouvé>")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python read_marc.py path/to/file.mrc")
        sys.exit(1)
    main(sys.argv[1])
