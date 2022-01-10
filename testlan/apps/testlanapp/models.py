from django.db import models

class PointData(models.Model):
    PointData_Name = models.FileField('Название точки', max_length = 50)
    PointData_IP = models.FileField('IP', max_length = 15)
    PointData_Availability = models.BooleanField('Доступность')
    PointData_TestingIncluded = models.BooleanField('Тестирование включено')
    PointData_DateAdded = models.DateTimeField('Дата добавления')
    
class CheckLog(models.Model):
    pointdata = models.ForeignKey(PointData, on_delete = models.CASCADE)
    CheckLog_ResponseTime = models.IntegerField('Время ответа', default = 0)
    CheckLog_NumberOfJumpsToPoint = models.IntegerField('Количество прыжков до точки', default = 0)
    CheckLog_TestDate = models.DateTimeField('Дата теста')
    
class Alert(models.Model):
    Alert_Name = models.FileField('Имя админа', max_length = 50)
    Alert_TelegramAddress = models.FileField('Telegram адрес', max_length = 200)
    Alert_Activity = models.BooleanField('Активность')
    Alert_DateAdded = models.DateTimeField('Дата добавления')
    Alert_EditingDate = models.DateTimeField('Дата редактирования')

class LogOfSendingNotifications(models.Model):
    alert = models.ForeignKey(Alert, on_delete = models.CASCADE)
    LogOfSendingNotifications_Date = models.DateTimeField('Дата оповещения')
    LogOfSendingNotifications_SubmissionStatus = models.TextField('Дата оповещения')