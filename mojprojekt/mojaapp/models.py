from django.db import models

class Ustawienia(models.Model):
    kolor = models.CharField(max_length=7, default='#FFFFFF')  # Domyślny kolor to biały
    tytul = models.CharField(max_length=100, default='Moja Strona')  # Domyślny tytuł strony

    def __str__(self):
        return f"Ustawienia {self.pk}"

