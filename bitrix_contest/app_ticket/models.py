from django.db import models


class RequestData(models.Model):
    request_method = models.CharField(max_length=100)
    request_text = models.CharField(max_length=100)

    def __str__(self):
        return self.request_text
