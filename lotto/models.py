from django.db import models

class LottoTicket(models.Model):
    user =  models.CharField(max_length=50)
    numbers = models.CharField(max_length=20)
    round = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class LottoDraw(models.Model):
    round = models.IntegerField(unique=True)
    winning_numbers = models.CharField(max_length=20)
    draw_date = models.DateTimeField(auto_now_add=True)
