from random import choices
from django.db import models
from users.models import User
    
class FCL(models.Model):
    chk_date = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    carrier = models.CharField(max_length=100)
    twenty = models.CharField(max_length=100)
    fourty = models.CharField(max_length=100)
    freq = models.CharField(max_length=100)
    ttime = models.CharField(max_length=100)
    effective = models.CharField(max_length=100)
    scno = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='작성자')    

class Airfreight(models.Model):
    air_consol = models.CharField(max_length=100)
    air_chk_date = models.CharField(max_length=100)
    air_origin = models.CharField(max_length=100)
    air_dest = models.CharField(max_length=100)
    air_carrier = models.CharField(max_length=100)
    air_min = models.CharField(max_length=100)
    air_normal = models.CharField(max_length=100)
    air_45kg = models.CharField(max_length=100)
    air_100kg = models.CharField(max_length=100)
    air_300kg = models.CharField(max_length=100)
    air_500kg = models.CharField(max_length=100)
    air_1000kg = models.CharField(max_length=100)
    air_fsc = models.CharField(max_length=100)
    air_iss = models.CharField(max_length=100)
    air_tspoint = models.CharField(max_length=100)
    air_skdl = models.CharField(max_length=100)
    air_remark = models.CharField(max_length=100)
    air_effective = models.CharField(max_length=10)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='작성자')

class LCL(models.Model):
    

    LCL_chk_date = models.CharField(max_length=100)
    LCL_pic_code = models.CharField(max_length=100)
    LCL_origin = models.CharField(max_length=4)
    LCL_dest = models.CharField(max_length=4)
    LCL_ofc = models.CharField(max_length=100)
    ofcunit = (('CBM', 'CBM'),
                        ('KG', 'KG'),
                        ('BL', 'BL'),)
    LCL_ofcunit = models.CharField(max_length=5 , choices = ofcunit, default='CBM', blank=False) 
    LCL_consol = models.CharField(max_length=100)
    LCL_ttime = models.CharField(max_length=100)
    LCL_effective = models.CharField(max_length=100)
    LCL_remark = models.CharField(max_length=100)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='작성자')
    
class Local_Air(models.Model):
    ##Seoul Loc
    Air_unit = (('CBM', 'CBM'),
                        ('KG', 'KG'),
                        ('BL', 'BL'),)
    Loc_branch = models.CharField(max_length=10)
    Loc_port = models.CharField(max_length=4)
    Loc_Air_Hdc = models.CharField(max_length=10)
    Loc_Air_Hdcunit = models.CharField(max_length = 5 , choices = Air_unit, default = 'CBM', blank=False)
    Loc_Air_Clc = models.CharField(max_length=10)
    Loc_Air_Clcunit = models.CharField(max_length = 5 , choices = Air_unit, default = 'CBM', blank=False)
    Loc_Air_Doc = models.CharField(max_length=10)
    Loc_Air_Docunit = models.CharField(max_length = 5 , choices = Air_unit, default = 'CBM', blank=False)
    Loc_Air_Thc = models.CharField(max_length=10)
    Loc_Air_Thcunit = models.CharField(max_length = 5 , choices = Air_unit, default = 'CBM', blank=False)
    Loc_Air_Otc = models.CharField(max_length=100)
    Loc_Air_Remark = models.CharField(max_length=100)
    
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='작성자')    

class Local_Lcl(models.Model):
    
    Lcl_unit = (('CBM', 'CBM'),
                        ('KG', 'KG'),
                        ('BL', 'BL'),)
    Loc_branch = models.CharField(max_length=4)
    Loc_port = models.CharField(max_length=4)
    Loc_Lcl_Cfs = models.CharField(max_length=10)
    Loc_Lcl_Cfsunit =  models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Loc_Lcl_Doc = models.CharField(max_length=10)
    Loc_Lcl_Docunit = models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Loc_Lcl_Hdc = models.CharField(max_length=10)
    Loc_Lcl_Hdcunit = models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Loc_Lcl_Clc = models.CharField(max_length=10)
    Loc_Lcl_Clcunit = models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Loc_Lcl_Blf = models.CharField(max_length=10)
    Loc_Lcl_Blfunit = models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Loc_Lcl_Otc = models.CharField(max_length=100)
    Loc_Lcl_Remark = models.CharField(max_length=100)

    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='작성자')
    
class Local_Fcl(models.Model):
    
    Loc_branch = models.CharField(max_length=4)
    Loc_port = models.CharField(max_length=4)
    Loc_Fcl_Thc = models.CharField(max_length=10)
    Loc_Fcl_Doc = models.CharField(max_length=10)
    Loc_Fcl_Vgm = models.CharField(max_length=10)
    Loc_Fcl_Seal = models.CharField(max_length=10)
    Loc_Fcl_Clc = models.CharField(max_length=10)
    Loc_Fcl_Hdc = models.CharField(max_length=10)
    Loc_Fcl_Otc = models.CharField(max_length=100)
    Loc_Fcl_Remark = models.CharField(max_length=100)
    
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='작성자')


class Dest_Air(models.Model):
    ##Seoul Loc
    Air_unit = (('CBM', 'CBM'),
                        ('KG', 'KG'),
                        ('BL', 'BL'),)
    Dest_branch = models.CharField(max_length=10)
    Dest_port = models.CharField(max_length=4)
    Dest_Air_Hdc = models.CharField(max_length=10)
    Dest_Air_Hdcunit = models.CharField(max_length = 5 , choices = Air_unit, default = 'CBM', blank=False)
    Dest_Air_Clc = models.CharField(max_length=10)
    Dest_Air_Clcunit = models.CharField(max_length = 5 , choices = Air_unit, default = 'CBM', blank=False)
    Dest_Air_Doc = models.CharField(max_length=10)
    Dest_Air_Docunit = models.CharField(max_length = 5 , choices = Air_unit, default = 'CBM', blank=False)
    Dest_Air_Thc = models.CharField(max_length=10)
    Dest_Air_Thcunit = models.CharField(max_length = 5 , choices = Air_unit, default = 'CBM', blank=False)
    Dest_Air_Otc = models.CharField(max_length=100)
    Dest_Air_Remark = models.CharField(max_length=100)
    
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='작성자') 
    
class Dest_Lcl(models.Model):
    
    Lcl_unit = (('CBM', 'CBM'),
                        ('KG', 'KG'),
                        ('BL', 'BL'),)
    Dest_branch = models.CharField(max_length=4)
    Dest_port = models.CharField(max_length=4)
    Dest_Lcl_Baf = models.CharField(max_length=10)
    Dest_Lcl_Bafunit =  models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Dest_Lcl_Caf = models.CharField(max_length=10)
    Dest_Lcl_Cafunit =  models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Dest_Lcl_Drc = models.CharField(max_length=10)
    Dest_Lcl_Drcunit =  models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Dest_Lcl_Ccc = models.CharField(max_length=10)
    Dest_Lcl_Cccunit =  models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Dest_Lcl_Thc = models.CharField(max_length=10)
    Dest_Lcl_Thcunit =  models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Dest_Lcl_Doc = models.CharField(max_length=10)
    Dest_Lcl_Hdc = models.CharField(max_length=10)
    Dest_Lcl_Clc = models.CharField(max_length=10)
    Dest_Lcl_Whc = models.CharField(max_length=10)
    Dest_Lcl_Whcunit = models.CharField(max_length = 5 , choices = Lcl_unit, default = 'CBM', blank=False)
    Dest_Lcl_Otc = models.CharField(max_length=100)
    Dest_Lcl_Remark = models.CharField(max_length=100)

    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='작성자')
    
class Dest_Fcl(models.Model):
    
    Dest_branch = models.CharField(max_length=4)
    Dest_port = models.CharField(max_length=4)
    Dest_Fcl_Thc = models.CharField(max_length=10)
    Dest_Fcl_Doc = models.CharField(max_length=10)
    Dest_Fcl_Wfc = models.CharField(max_length=10)
    Dest_Fcl_Ccc = models.CharField(max_length=10)
    Dest_Fcl_Cic = models.CharField(max_length=10)
    Dest_Fcl_Hdc = models.CharField(max_length=10)
    Dest_Fcl_Otc = models.CharField(max_length=100)
    Dest_Fcl_Remark = models.CharField(max_length=100)
    
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='작성자')