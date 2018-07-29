from django.db import models

# Create your models here.

class RegisteredEnvironment(models.Model):

    id = models.CharField(max_length=50, help_text="Ingrese codigo del ambiente")
    name = models.CharField(max_length=200, help_text="Ingrese nombre del ambiente")
    desc = models.TextField(max_length=1000, help_text='Ingrese descripcion del ambiente')

    def __str__(self):
        return self.id + ': ' + self.name

class RegisteredApplication(models.Model):

    id = models.CharField(max_length=50, help_text="Ingrese codigo de la aplicacion")
    name = models.CharField(max_length=200, help_text="Ingrese nombre de la aplicacion")
    desc = models.TextField(max_length=1000, help_text='Ingrese descripcion de la aplicacion y de sus parametros')

    def __str__(self):
        return self.id + ': ' + self.name

class ApplicationParameter(models.Model):

    id = models.CharField(max_length=50, help_text="Ingrese codigo del parametro")
    name = models.CharField(max_length=200, help_text="Ingrese nombre del parametro")
    desc = models.TextField(max_length=1000, help_text='Ingrese descripcion del parametro y formato permitido de sus valores')
    registered_application = models.ForeignKey('RegisteredApplication', on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return self.id + ': ' + self.name

class ParameterValue(models.Model):

    value = models.TextField(max_length=1000, help_text="Ingrese valor del parametro")
    application_parameter = models.ForeignKey('ApplicationParameter', on_delete=models.SET_NULL, null=True) 
    registered_environment = models.ForeignKey('RegisteredEnvironment', on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return self.application_parameter.name + ' (' + self.registered_environment.name + '): ' + self.value


