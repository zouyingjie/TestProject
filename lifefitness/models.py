from django.db import models

# Create your models here.


class LifeFitnessBaseModel(models.Model):
    class Meta:
        app_label = "lifefitness"
        db_table = "lifefitness_base_body"

    request_body = models.TextField(verbose_name=u"请求内容", default="")