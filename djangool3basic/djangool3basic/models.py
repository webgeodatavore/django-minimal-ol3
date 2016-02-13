# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class loc_colonnes_enterrees_nm(models.Model):
    matricule = models.CharField(max_length=0)
    type_deche = models.CharField(max_length=0)
    quartier = models.CharField(max_length=0)
    num_voie = models.FloatField()
    adresse = models.CharField(max_length=0)
    cle_voie = models.CharField(max_length=0)
    capacite_c = models.FloatField()
    capacite_f = models.FloatField()
    prehension = models.CharField(max_length=0)
    couleur = models.CharField(max_length=0)
    finition_p = models.CharField(max_length=0)
    trappe_com = models.FloatField()
    typ_avaloi = models.CharField(max_length=0)
    isolation_field = models.FloatField()
    numero_pol = models.FloatField()
    nom_pole_n = models.CharField(max_length=0)
    code_com = models.FloatField()
    commune = models.CharField(max_length=0)
    long_wgs84 = models.FloatField()
    lat_wgs84 = models.FloatField()
    geom = models.PointField(srid=2154)

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
    'isolation_field' : 'isolation_',
    'numero_pol' : 'numero_pol',
    'nom_pole_n' : 'nom_pole_n',
    'code_com' : 'code_com',
    'commune' : 'commune',
    'long_wgs84' : 'long_wgs84',
    'lat_wgs84' : 'lat_wgs84',
    'geom' : 'POINT',
}
