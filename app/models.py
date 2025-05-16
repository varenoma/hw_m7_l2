from django.db import models
from django.utils.text import slugify

# Create your models here.


class ClassQatagon(models.Model):
    toliq_ism = models.CharField(max_length=150, unique=True)
    tavsif = models.TextField()
    tugilgan_sana = models.DateField()
    vafort_etgan_sana = models.DateField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.toliq_ism)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.toliq_ism

    class Meta:
        db_table = 'qatagonlar'
        ordering = ['toliq_ism']
        verbose_name = "Qatag'on"
        verbose_name_plural = "Qatag'onlar"
