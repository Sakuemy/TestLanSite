from django.db import models

class PointData(models.Model):
    PointData_Name = models.CharField('Название точки', max_length = 50)
    PointData_IP = models.GenericIPAddressField('IP')
    PointData_TestingIncluded = models.BooleanField('Тестирование включено')
    
    class Meta:
        verbose_name = 'Список тестируемых устройств'
        
    def __str__(self):
        return self.PointData_Name + '(' + self.PointData_IP + ')'
    
class CheckLog(models.Model):
    pointdata = models.ForeignKey(PointData, on_delete = models.CASCADE)
    PointData_Availability = models.BooleanField('Доступность')
    CheckLog_ResponseTime = models.IntegerField('Время ответа', default = 0)
    CheckLog_NumberOfJumpsToPoint = models.IntegerField('Количество прыжков до точки', default = 0)
    CheckLog_TestDate = models.DateTimeField('Дата теста')
    
class Alert(models.Model):
    Alert_Name = models.CharField('Имя админа', max_length = 50)
    Alert_TelegramAddress = models.URLField('Telegram адрес')
    Alert_Activity = models.BooleanField('Активность')
    
    class Meta:
        verbose_name = 'Даннае пользователей для оповещения'
        
    def __str__(self):
        return self.Alert_Name + '(Активность: ' + str(self.Alert_Activity) + ')'

class LogOfSendingNotifications(models.Model):
    alert = models.ForeignKey(Alert, on_delete = models.CASCADE)
    LogOfSendingNotifications_Date = models.DateTimeField('Дата оповещения')
    LogOfSendingNotifications_SubmissionStatus = models.TextField('Дата оповещения')