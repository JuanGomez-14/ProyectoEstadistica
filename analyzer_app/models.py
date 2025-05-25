from django.db import models
from django.contrib.auth.models import User

class ExcelFile(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True,  # Hace que el campo sea opcional
        blank=True  # Permite que el campo esté vacío en formularios
    )
    file = models.FileField(upload_to='excel_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.file.name