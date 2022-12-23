import factory
from factory.django import DjangoModelFactory

from main.models import Namirnica, Napomena, Obrok, Osoba, Datum

## Defining a factory
class NamirnicaFactory(DjangoModelFactory):
    class Meta:
        model = Namirnica

    namirnica_povrce = factory.Faker("povrce")
    namirnica_voce = factory.Faker("voce")
    namirnica_meso = factory.Faker("meso")
    namirnica_ostalo = factory.Faker("ostalo")


class NapomenaFactory(DjangoModelFactory):
    class Meta:
        model = Napomena

    napomena_alergije = factory.Faker("alergije")
    napomena_lijekovi = factory.Faker("lijekovi")
    napomena_bolesti = factory.Faker("bolesti")

class OsobaFactory(DjangoModelFactory):
    class Meta:
        model = Osoba

    osoba_ime = factory.Faker("ime")
    osoba_prezime = factory.Faker("prezime")
    osoba_oib = factory.Faker("oib")

class ObrokFactory(DjangoModelFactory):
    class Meta:
        model = Obrok

    obrok_zajutrak = factory.Faker("zajutrak")
    obrok_dorucak = factory.Faker("dorucak")
    obrok_rucak = factory.Faker("rucak")
    obrok_uzina = factorNamirnicaFactoryy.Faker("uzina")
    obrok_vecera = factory.Faker("vecera")
    obrok_komentar = factory.Faker("komentar")

class DatumFactory(DjangoModelFactory):
    class Meta:
        model = Datum

    datum_dan = factory.Faker("dan u tjednu")
    datum_datum = factory.Faker("datum")
    datum_obroka = factory.Faker("datum obroka")