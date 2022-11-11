from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('Русское название', max_length=200)
    title_en = models.CharField('Английское название', max_length=200, null=True)
    title_jp = models.CharField('Японское название', max_length=200, null=True)
    image = models.ImageField('Изображение', default='default.png')
    description = models.TextField('Описание', null=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Появиться', null=True)
    disappeared_at = models.DateTimeField('Исчезнет', null=True)
    level = models.IntegerField('Уровень', null=True)
    health = models.IntegerField('Здоровье', null=True)
    attack = models.IntegerField('Атака', null=True)
    defence = models.IntegerField('Защита', null=True)
    stamina = models.IntegerField('Выносливость', null=True)
