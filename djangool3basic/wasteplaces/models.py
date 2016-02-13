#from django.db import models

# Create your models here.

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class loc_colonnes_enterrees_nm(models.Model):
    matricule = models.CharField(primary_key=True, max_length=10)
    type_deche = models.CharField(max_length=20)
    quartier = models.CharField(max_length=30)
    num_voie = models.FloatField()
    adresse = models.CharField(max_length=50)
    cle_voie = models.CharField(max_length=20)
    capacite_c = models.FloatField()
    capacite_f = models.FloatField()
    prehension = models.CharField(max_length=15)
    couleur = models.CharField(max_length=30)
    finition_p = models.CharField(max_length=20)
    trappe_com = models.FloatField()
    typ_avaloi = models.CharField(max_length=15)
    isolation = models.FloatField()
    numero_pol = models.FloatField()
    nom_pole_n = models.CharField(max_length=30)
    code_com = models.FloatField()
    commune = models.CharField(max_length=30)
    long_wgs84 = models.FloatField()
    lat_wgs84 = models.FloatField()
    geom = models.PointField(srid=2154)

    class Meta:
        db_table = 'loc_colonnes_enterrees_nm'


# Auto-generated `LayerMapping` dictionary for loc_colonnes_enterrees_nm model
loc_colonnes_enterrees_nm_mapping = {
    'matricule' : 'matricule',
    'type_deche' : 'type_deche',
    'quartier' : 'quartier',
    'num_voie' : 'num_voie',
    'adresse' : 'adresse',
    'cle_voie' : 'cle_voie',
    'capacite_c' : 'capacite_c',
    'capacite_f' : 'capacite_f',
    'prehension' : 'prehension',
    'couleur' : 'couleur',
    'finition_p' : 'finition_p',
    'trappe_com' : 'trappe_com',
    'typ_avaloi' : 'typ_avaloi',
    'isolation' : 'isolation',
    'numero_pol' : 'numero_pol',
    'nom_pole_n' : 'nom_pole_n',
    'code_com' : 'code_com',
    'commune' : 'commune',
    'long_wgs84' : 'long_wgs84',
    'lat_wgs84' : 'lat_wgs84',
    'geom' : 'POINT',
}
