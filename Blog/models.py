from django.db import models
from datetime import datetime, timedelta


class Room(models.Model):
  name = models.CharField(max_length=200)
  floor = models.IntegerField()
  room_number = models.IntegerField()

  def str(self):
    return f"{self.name}, room: {self.room_number}, floor: {self.room_number}"




class Meeting(models.Model):
  title = models.CharField(max_length=120)
  date = models.DateField()
  start_time = models.TimeField(default= datetime.now)
  duration = models.IntegerField(default=1)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)
  def str(self):
    return f"title:  {self.title} date: {self.date} "