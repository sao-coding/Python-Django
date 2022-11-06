from django.db import models

# Create your models here.


class Tv_list(models.Model):
    # tvno = models.IntegerField()
    tvname = models.CharField(max_length=20)
    tvcode = models.CharField(max_length=20)

    def __str__(self):
        return self.tvname


class Engtv_list(models.Model):
    # tvno = models.IntegerField()
    tvname = models.CharField(max_length=20)
    tvcode = models.CharField(max_length=20)

    def __str__(self):
        return self.tvname


class Car_list(models.Model):
    maker = (
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
        ('Mazda', 'Mazda')
    )
    # Ford = (
    #     ('Fiesta', 'Fiesta'),
    #     ('Focus', 'Focus'),
    #     ('Mustang', 'Mustang'),
    # )
    # Honda = (
    #     ('Fit', 'Fit'),
    #     ('City', 'City'),
    #     ('NSX', 'NSX')
    # )
    # Mazda = (
    #     ('Mazda3', 'Mazda3'),
    #     ('Mazda5', 'Mazda5'),
    #     ('Mazda6', 'Mazda6')
    # )
    model = [
        ('Ford', (
            ('Fiesta', 'Fiesta'),
            ('Focus', 'Focus'),
            ('Mustang', 'Mustang')
        )
        ),
        ('Honda', (
            ('Fit', 'Fit'),
            ('City', 'City'),
            ('NSX', 'NSX')
        )),
        ('Mazda',
         (
             ('Mazda3', 'Mazda3'),
             ('Mazda5', 'Mazda5'),
             ('Mazda6', 'Mazda6')
         )
         ),
    ]

    car_maker = models.CharField(max_length=20, choices=maker)
    car_model = models.CharField(max_length=20, choices=model)
    car_price = models.IntegerField()
    car_qty = models.IntegerField(default=0)

    def __str__(self):
        return self.car_model
