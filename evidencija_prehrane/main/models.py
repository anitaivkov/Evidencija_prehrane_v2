from django.db import models

class Namirnica(models.Model):
    """Obrok se sastoji od Namirnice. Namirnica je u vezi s Obrokom M:M"""

    namirnica_povrce = models.CharField(max_length = 30, default=None)
    namirnica_voce = models.CharField(max_length = 30, default=None)
    namirnica_meso = models.CharField(max_length = 30, default=None)
    namirnica_ostalo = models.TextField

    def __str__(self):
        return str(self.namirnica_povrce)

class Napomena(models.Model):
    """Osoba ima Napomenu koja može utjecati na prehranu. Napomena je u vezi s Osobom 1:1"""

    napomena_alergije = models.TextField
    napomena_lijekovi = models.CharField(max_length = 50, default=None)
    napomena_bolesti = models.TextField

    def __str__(self):
        return str(self.napomena_bolesti)

class Osoba(models.Model):
    """U evidenciji prehrane je potrebno navesti osobu. Osoba je u vezi s Napomenom 1:1
    i s Obrokom 1:M"""

    osoba_ime = models.CharField(max_length = 30, default=None)
    osoba_prezime = models.CharField(max_length = 30, default=None)
    osoba_oib = models.PositiveIntegerField

    osoba_napomena = models.OneToOneField(
        Napomena, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.osoba_ime)

class Obrok(models.Model):
    """u klasi Obrok su navedeni nazivi obroka i u vezi je s Osobom M:1, Datumom 1:M
    i Namirnicom M:M"""

    obrok_zajutrak = models.CharField(max_length = 50, default=None)
    obrok_dorucak = models.CharField(max_length = 50, default=None)
    obrok_rucak = models.CharField(max_length = 50, default=None)
    obrok_uzina = models.CharField(max_length = 50, default=None)
    obrok_vecera = models.CharField(max_length = 50, default=None)
    obrok_komentar = models.TextField

    def __str__(self):
        return str(self.obrok_rucak)

    obrok_namirnice = models.ManyToManyField(Namirnica, default=None)
    obrok_od_osobe = models.ForeignKey(Osoba, on_delete=models.CASCADE, default=None)

class Datum(models.Model):
    """Svaki obrok ima Datum. U Datumu se navodi dan u tjednu i datum.
    Postoji odabir između dana u tjednu. U vezi je s Obrokom M:1"""
    PONEDJELJAK = 'PON'
    UTORAK = 'UTO'
    SRIJEDA = 'SRI'
    CETVRTAK = 'CET'
    PETAK = 'PET'
    SUBOTA ='SUB'
    NEDJELJA = 'NED'
    datum_dan_choices = [
        (PONEDJELJAK, 'Ponedjeljak'),
        (UTORAK, 'Utorak'),
        (SRIJEDA, 'Srijeda'),
        (CETVRTAK, 'Četvrtak'),
        (PETAK, 'Petak'),
        (SUBOTA, 'Subota'),
        (NEDJELJA, 'Nedjelja')]

    datum_dan = models.CharField(
        max_length = 10,
        choices = datum_dan_choices)

    datum_datum = models.DateField

    def __str__(self):
        return str(self.datum_datum)

    datum_obroka = models.ForeignKey(Obrok, on_delete=models.CASCADE, default=None)