from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Person(models.Model):
    villes = [
        ("Abengourou", "Abengourou"),
        ("Abidjan", "Abidjan"),
        ("Aboisso", "Aboisso"),
        ("Adzopé", "Adzopé"),
        ("Agboville", "Agboville"),
        ("Akoupé", "Akoupé"),
        ("Anyama", "Anyama"),
        ("Bingerville", "Bingerville"),
        ("Bondoukou", "Bondoukou"),
        ("Bouaflé", "Bouaflé"),
        ("Bouaké", "Bouaké"),
        ("Boundiali", "Boundiali"),
        ("Dabou", "Dabou"),
        ("Daloa", "Daloa"),
        ("Daoukro", "Daoukro"),
        ("Dimbokro", "Dimbokro"),
        ("Divo", "Divo"),
        ("Ferkessédougou", "Ferkessédougou"),
        ("Gagnoa", "Gagnoa"),
        ("Grand-Bassam", "Grand-Bassam"),
        ("Guiglo", "Guiglo"),
        ("Issia", "Issia"),
        ("Katiola", "Katiola"),
        ("Korhogo", "Korhogo"),
        ("Lakota", "Lakota"),
        ("Man", "Man"),
        ("Odienné", "Odienné"),
        ("San-Pédro", "San-Pédro"),
        ("Sassandra", "Sassandra"),
        ("Séguéla", "Séguéla"),
        ("Soubré", "Soubré"),
        ("Tiassalé", "Tiassalé"),
        ("Toumodi", "Toumodi"),
        ("Yamoussoukro", "Yamoussoukro"),
        ("Zuénoula", "Zuénoula")
    ]
    communes = [
        ('abobo', 'Abobo'),
        ('adjame', 'Adjamé'),
        ('anyama', 'Anyama'),
        ('attecoube', 'Attécoubé'),
        ('bingerville', 'Bingerville'),
        ('cocody', 'Cocody'),
        ('koumassi', 'Koumassi'),
        ('marcory', 'Marcory'),
        ('plateau', 'Plateau'),
        ('port-bouet', 'Port-Bouët'),
        ('treichville', 'Treichville'),
        ('yopougon', 'Yopougon'),
    ]


    name = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    numero = models.CharField(max_length=14)
    date = models.DateField(null=True, default=None)
    location = models.CharField(max_length=100, blank=True, choices=villes)
    commune = models.CharField(max_length=100, blank=True, choices=communes)
    status = models.CharField(max_length=100)
    genre = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name} {self.prenoms} {self.email} {self.numero} {self.date} {self.location} {self.commune} {self.status} {self.genre}"
    
class spirit(models.Model):
    CHOIX = [
        ("oui","oui"),
        ("non","non")
    ]
    DEPARTEMENT = [
        ("ESTER","ESTHER"),
        ("EMMANUEL","EMMANUEL"),
        ("JOSUE","JOSUE"),
        ("OSE","OSE"),
    ]
    COMMIT = [
        ("ORDRE ET ACCEUIL", "ORDRE ET ACCEUIL"),
        ("COMMITE SOCIAL", "COMMITE SOCIAL")
    ]
    person = models.ForeignKey(Person,null=True, blank=True, on_delete=models.CASCADE)
    baptism_water = models.CharField(max_length=3, default=None, choices=CHOIX)
    date = models.DateField(null=True, blank=True)
    baptism_spirit = models.CharField(max_length=3, default=None, choices=CHOIX)
    community = models.CharField(max_length=16,null=True, blank=True, default=None, choices=COMMIT)
    jeunesse = models.CharField(max_length=8,null=True, blank=True, default=None, choices=DEPARTEMENT)
    
class scolaire(models.Model):
    LEVEL = [
        ("JE CONTINUE LES COURS","JE CONTINUE LES COURS"),
        ("CP1","CP1"),
        ("CP2","CP2"),
        ("CE1","CE1"),
        ("CE2","CE2"),
        ("CM1","CM1"),
        ("CM2","CM2"),
        ("SIXIEME","SIXIEME"),
        ("CINQUIEME","CINQUIEME"),
        ("QUATRIEME","QUATRIEME"),
        ("TROISIEME","TROISIEME"),
        ("SECOND","SECOND"),
        ("PREMIERE","PREMIERE"),
        ("TERMINAL","TERMINAL"),
        ("LICENCE 1","LICENCE 1"),
        ("LICENCE 2","LICENCE 2"),
        ("LICENCE 3","LICENCE 3"),
        ("MASTER 1","MASTER 1"),
        ("MASTER 2","MASTER 2"),
        ("DOCTORAT","DOCTORAT")
    ]
    
    DIPLOME = [
        ("CEPE","CEPE"),
        ("BEPEC","BEPEC"),
        ("BACCALAUREAT","BACCALAUREAT"),
        ("BTS","BTS"),
        ("LICENCE 3","LICENCE 3"),
        ("MASTER","MASTER"),
        ("DOCTORAT","DOCTORAT"),
        ("DUT","DUT"),
    ]
    TYPES = [
        ("A","A"),
        ("B","B"),
        ("C","C"),
        ("D","D"),
        ("E","E"),
        ("F","F"),
        ("G","G"),
    ]
    person = models.ForeignKey(spirit,null=True,default=None, on_delete=models.CASCADE)
    niveau = models.CharField(max_length=21,null=True, blank=True, choices=LEVEL)
    diplomes = models.CharField(max_length=12,null=True, blank=False, choices=DIPLOME)
    series = models.CharField(max_length=12,null=True, blank=True, choices=TYPES)
    filieres = models.CharField(max_length=36,null=True, blank=True)
    
class professionnal(models.Model):
    CHOIX = [
        ("oui","oui"),
        ("non","non")
    ]
    secteurs_activite = [
        ('agriculture', 'Agriculture'),
        ('telecommunications', 'Télécommunications'),
        ('petrole_gaz', 'Pétrole et gaz'),
        ('banque_finance', 'Banque et finance'),
        ('energie', 'Énergie'),
        ('tourisme', 'Tourisme'),
        ('commerce', 'Commerce'),
        ('construction_immobilier', 'Construction et immobilier'),
        ('manufacturier', 'Manufacturier'),
        ('services', 'Services'),
        ('transport_logistique', 'Transport et logistique'),
        ('technologie', 'Technologie de l\'information'),
        ('education', 'Éducation'),
        ('sante', 'Santé'),
        ('media', 'Média et communication'),
        ('mode', 'Mode et textile'),
        ('art_culture', 'Art et culture'),
        ('sport', 'Sport et loisirs'),
        ('restauration', 'Restauration'),
        ('automobile', 'Automobile'),
        ('environnement', 'Environnement'),
    ]

    person = models.ForeignKey(scolaire,null=True, on_delete=models.CASCADE)
    domaine = models.CharField(max_length=80, null=True, blank=True, choices=secteurs_activite)
    working = models.CharField(max_length=3,null=True, blank=True, choices=CHOIX)
    metier= models.CharField(max_length=80,null=True, blank=True)
    description = models.TextField(blank=True, default=None)
    cv = models.FileField(upload_to='PDF/CV/', null=True)
    image_de_profil = models.ImageField(upload_to='Pictures/profil', null=True)
    
# class PersonIdentifier(models.Model):
    
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     form2 = models.ForeignKey(spirit, on_delete=models.CASCADE, null=True, blank=True)
#     form3 = models.ForeignKey(scolaire, on_delete=models.CASCADE, null=True, blank=True)
#     form4 = models.ForeignKey(professionnal, on_delete=models.CASCADE, null=True, blank=True)