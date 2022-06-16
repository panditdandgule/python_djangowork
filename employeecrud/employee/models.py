from django.db import models

GENDER_CHOICES = [('M', 'MALE'),
                  ('F', 'FEMALE'),
                  ('O', 'OTHER')
                  ]


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField("Employee's First Name", max_length=50, null=True,
                                  blank=True)  # max length is mandatory for char field
    last_name = models.CharField("Employee's Last Name", max_length=50, null=True, blank=True)
    age = models.PositiveBigIntegerField()
    # gender=models.CharField(choices=GENDER_CHOICES,max_length=10)
    # date_of_birth=models.DateField()
    mobile_number = models.CharField("Employee's Mobile Number", max_length=10)
    email = models.EmailField()
    address = models.TextField()
    # profileimage=models.ImageField(upload_to="images/employee/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'employeeinfo'
