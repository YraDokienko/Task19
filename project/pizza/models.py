from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Ingredient(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']


class Pizza(models.Model):
    name = models.CharField('Название', max_length=40)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='Размер')
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2, default=0)
    ingredient = models.ManyToManyField(Ingredient, verbose_name='Ингридиенты')
    description = models.CharField('Описание', max_length=300)
    available = models.BooleanField('Наличие', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пиццу'
        verbose_name_plural = 'Пиццы'
        ordering = ['name']
