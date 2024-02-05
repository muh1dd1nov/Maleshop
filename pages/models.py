from django.db import models

class MainCarusel(models.Model):
    image = models.ImageField(upload_to='home-carusel')
    titlesmall = models.CharField(max_length = 50)
    info = models.CharField(max_length = 255)
    titlebig = models.CharField(max_length = 50)
    is_active = models.BooleanField(default = False)
     
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.titlebig    
    
    class Meta:
        verbose_name = 'carusel'
        verbose_name_plural = 'carusels'
