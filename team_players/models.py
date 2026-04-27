from django.db import models

class Player_Details(models.Model):
    player_id=models.IntegerField(primary_key=True)
    player_name=models.CharField(blank=False,unique=True,db_index=True)
    player_role=models.CharField(blank=False)
    player_perfrating=models.IntegerField(choices=[(1,'⭐'),(2,'⭐⭐'),(3,'⭐⭐⭐'),(4,'⭐⭐⭐⭐'),(5,'⭐⭐⭐⭐⭐')])
    player_jersey=models.IntegerField(blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    ##magic method
    def __str__(self):
        return self.player_name