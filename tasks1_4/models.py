from django.db import models

# Create your models here.

class MachineDir(models.Model):
    machine_id = models.BigIntegerField(primary_key=True)
    machine_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_dir'


class IndustrialConsts(models.Model):
    ic_id = models.IntegerField(primary_key=True)
    min_mass = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    max_mass = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    min_count = models.IntegerField(blank=True, null=True)
    max_count = models.IntegerField(blank=True, null=True)
    industrial_type = models.ForeignKey('IndustrialTypes', models.DO_NOTHING, db_column='industrial_type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industrial_consts'


class IndustrialTypes(models.Model):
    it_id = models.IntegerField(primary_key=True)
    it_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'industrial_types'