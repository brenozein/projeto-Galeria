from django.db import models

class Viagens(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Campo para a imagem da viagem
    image =models.ImageField(upload_to='viagens/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Viagem"
        verbose_name_plural = "Viagens"
        ordering = ['-created_at'] #Ordena as viagens pela data (mais novas primeiro)
