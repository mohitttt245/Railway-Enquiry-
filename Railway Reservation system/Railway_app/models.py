from django.db import models
# Create your models here.
    
class Add_Train(models.Model):
    train_name = models.CharField(max_length=30, null=True)
    train_no = models.IntegerField(null=True)
    from_city = models.CharField(max_length=30, null=True)
    to_city = models.CharField(max_length=30, null=True)
    departure_time = models.DateTimeField(("Departure"), auto_now=False, auto_now_add=False,null=True)
    arrival_time = models.DateTimeField(("Arrival"), auto_now=False, auto_now_add=False,null=True)
    distance = models.IntegerField(null=True)
    img = models.FileField(null=True)

    def __str__(self):
        return self.train_name + "  " + str(self.train_no)
    
class Passenger(models.Model):
    train_no= models.ForeignKey(Add_Train,on_delete=models.CASCADE,null=True)
    train_name=models.CharField(max_length=80, null=True)
    full_name = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    email_id = models.EmailField(unique=True)
    card_number= models.IntegerField(null=True)
    card_holder_name= models.CharField(max_length=80,null=True)
    fare = models.IntegerField(null=True)
    from_city = models.CharField(max_length=30, null=True)
    to_city = models.CharField(max_length=30, null=True)
    date = models.DateField(null=True)
    PAYMENT_CHOICES = [
        ('done', 'Done'),
        ('not_done', 'Not Done'),
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='not_done')

    
class Ticket(models.Model):
    PNR = models.CharField(max_length=9, null=True)
    train_no = models.IntegerField(null=True)
    ticket_number = models.CharField(max_length=20, unique=True)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    train = models.ForeignKey(Add_Train, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    fare = models.DecimalField(max_digits=8, decimal_places=2)
    issued_at = models.DateTimeField(auto_now_add=True)
    seat = models.IntegerField(null=True)

    def __str__(self):
        return self.ticket_number


class TrainSchedule(models.Model):
    train = models.ForeignKey(Add_Train, on_delete=models.CASCADE)
    station = models.CharField(max_length=30,null=True)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    def __str__(self):
        return f"{self.train} - {self.station}"

    class Meta:
        unique_together = ('train', 'station')
        ordering = ['train', 'departure_time']

class Payment(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)