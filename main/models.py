from django.db import models

# Create your models here.
class Arithmetic(models.Model):
    number1 = models.FloatField('Перше число')
    number2 = models.FloatField('Друге число')
    operation = models.TextField('Оператор')

    def __str__(self):
        return str(self.numerator) + str(self.operation) + str(self.denominator)

    class Meta:
        verbose_name = "Арифметичні операції"
        verbose_name_plural = "Арифметична операція"

class Conversion(models.Model):
    kilometers = models.FloatField('Кілометри')

    def __str__(self):
        return str(self.kilometers) + " km"

    class Meta:
        verbose_name = "Кілометрів"
        verbose_name_plural = "Кілометри"