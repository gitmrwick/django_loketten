from django.db import models

class Balie(models.Model):
    '''de model voor een balie loket
    elke balie heeft een groep
    binnen deze groep moet de tel uniek zijn
    elke balie refereert naar een tel_master voor de volgende nummer
    '''
    GESLOTEN = 'X'
    OPEN = 'O'
    BEZET = 'B'
    stati = [('X', 'Gesloten'), ('O', 'Open'), ('B', 'Bezet')]

    balie_nummer = models.IntegerField() 
    balie_naam = models.CharField(max_length=180, blank=True)
    balie_groep = models.CharField(max_length=4, default='AAAA')
    balie_tel = models.CharField(max_length=20, default='1')
    tel_master = models.ForeignKey('Tel', on_delete=models.DO_NOTHING)
    balie_status = models.CharField(
            max_length=2,
            choices=stati,
            default=GESLOTEN,
            )

    def is_gesloten(self):
        return self.balie_status == GESLOTEN

    def is_open(self):
        return self.balie_status == OPEN

    def is_bezet(self):
        return self.balie_status == BEZET

    def __str__(self):
        return f"Balie {self.balie_naam} - {self.balie_tel}"

class Tel(models.Model):
    '''een tel is gewoon een referentie
    een Balie groep refereert naar een tel om zijn eigen tel te verhoogen
    het is de werk van de Balie om de tel te verhoogen na zijn eigen tel is verhoogt
    '''
    tel_naam = models.CharField(max_length=180)
    tel_positie = models.IntegerField() 
    tel_prefix = models.CharField(max_length=10, blank=True)
    tel_suffix = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"Tel {self.tel_naam} - {self.tel_positie}"
