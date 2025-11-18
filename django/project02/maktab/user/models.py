from django.db import models


# Create your models here.
class MaktabManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(deleted=False)

    def archive(self):
        return super().get_queryset()
    
    def deleted_records(self):
        queryset = super().get_queryset()
        return queryset.filter(deleted=True)
    
    def test(self):
        print("hiiiiiiiiii")

class MainModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deletable = models.BooleanField(default=True)
    editable = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, null=True)

    objects = MaktabManager()
    indexes = [models.Index(fields=["deleted"])]

    class Meta:
        abstract = True


class MaktabUser(MainModel):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    user_type = models.CharField(null=True)
    last_login = models.DateTimeField(null=True)
    date_register = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    gender = models.BooleanField(default=False, null=False)


    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.deleted=}"


class Course(MainModel):
    name = models.CharField(max_length=100, unique=True)
    duration = models.IntegerField(default=540)
    sylabus = models.TextField(null=True)


class Lecturer(MainModel):
    first_name = models.CharField(max_length=50)


class Bootcamp(MainModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
