#!/usr/bin/env python3
"""
write_example.py
Créer un enregistrement minimal et l'écrire en MARC binaire.
"""
from pymarc import Record, Field, Subfield, Indicators

record = Record()
record.add_field(
    Field(
        tag='245',
        indicators=Indicators('0', '1'),
        subfields=[
            Subfield(code='a', value='Titre de test : '),
            Subfield(code='b', value='sous-titre /'),
            Subfield(code='c', value='Auteur.')
        ]
    )
)

with open('example_out.mrc', 'wb') as out:
    out.write(record.as_marc())

print("Écrit : example_out.mrc")
