balie-teller

een django project om een teller te tonen per balie

db tabels
Balie
- balie status
- meerdere balies, elke rij is een balie
- balie groepen met unieke tellen
- elke balie heeft zijn eigen tel
- te balie selecteert de nummer van tel en schrijft in zijn eigen kolom
Tel
- elke rij is een nieuwe tel
- de referentie voor elke balie
- elke balie moet van hier de nummer krijgen
- na een nummer nemen, Tel verhoogt
- balie's in dezelfde groep moet unieke tellen hebben

views
Publiek
- overview van alles met laatste gewijzigd balie
Balie
- hudige balie status en tel
- knoppen: status, volgende nummer, nieuwe tel
Tel
- door admin interface
