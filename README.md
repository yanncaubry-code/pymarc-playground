# pymarc-playground

Dépôt minimal pour apprendre **PyMARC** et manipuler des fichiers MARC binaire (MARC-8 ou UTF-8).

## Utiliser en ligne (Codespaces)
1. Code > **Create codespace on main**
2. Dans le terminal du Codespace :
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python read_marc.py test_marc.dat
