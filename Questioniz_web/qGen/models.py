from django.db import models

# Create your models here.
class EndUser(models.Model):
    username = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    # is_active = models.BooleanField(null=True)

    def __str__(self):
        return self.username

class Paragraph(models.Model):
    paragraph= models.CharField(max_length=2500)
    no_of_questions= models.IntegerField()

    def __str__(self):
        return self.paragraph

class ParaHistory(models.Model):
    para_no= models.IntegerField()
    username= models.ForeignKey("Enduser", on_delete= models.CASCADE)
    paragraph= models.ForeignKey("Paragraph", on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.para_no} - {self.paragraph}"

