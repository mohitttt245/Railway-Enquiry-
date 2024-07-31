# from django.contrib import admin
# from .models import Register, Add_Train, Passenger

# @admin.register(Register)
# class RegisterAdmin(admin.ModelAdmin):
#     list_display = ['user', 'mobile', 'address', 'dob', 'gender']

# @admin.register(Add_Train)
# class AddTrainAdmin(admin.ModelAdmin):
#     list_display = ['train_name', 'train_no', 'from_city', 'to_city', 'departure_time', 'arrival_time', 'distance']


# @admin.register(Passenger)
# class PassengerAdmin(admin.ModelAdmin):
#     list_display = ['first_name','last_name', 'age', 'gender', 'route', 'status', 'date', 'fare']

from typing import Any
from django import urls
from django.contrib import admin
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models

from .models import Add_Train, Passenger, Ticket,  Payment, TrainSchedule

@admin.register(models.Add_Train)
class Add_trainAdmin(admin.ModelAdmin):
    actions= ["Starting"]
    field=[""]
    list_display = ['train_name', 'train_no', 'from_city', 'to_city', 'departure_time', 'arrival_time', 'distance']
    list_per_page= 75
    list_filter= ["train_no"]
    search_fields= ["train_no","train_name"]
    
    @admin.action(description="Starting")
    def registration(self, request, queryset):
        updated_count = queryset.update(registration=0)
        self.message_user(
            request, f"{updated_count} Train start."
        )


@admin.register(models.Passenger)
class PassengerAdmin(admin.ModelAdmin):
    actions= ["Starting"]
    field=[""]
    list_display = ['full_name','train_name','gender', 'age', 'email_id', 'fare', 'from_city', 'to_city','train_no', 'date', 'payment_status','card_holder_name','card_number']
    list_per_page= 75
    list_filter= ["train_no",]
    search_fields= ["train_no","train_name"]
    
    @admin.action(description="Starting")
    def registration(self, request, queryset):
        updated_count = queryset.update(registration=0)
        self.message_user(
            request, f"{updated_count} Train start."
        )


# admin.site.register(Ticket)

@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display= ["passenger","payment_method","amount","status"]
    list_per_page= 100
    search_fields= ["passenger"]
    ordering= ["passenger"]

    @admin.display(ordering="User")
    def order_count(self, customer):
        url =(
            reverse("admin:store_order_changelist")
            + "?"
            + urlencode({
                "customer__id":customer.id
            })
        )
        return format_html('<a href="{}">{}</a>',url ,Passenger.User)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(order_count=Count("passenger"))


# admin.site.register(TrainSchedule)