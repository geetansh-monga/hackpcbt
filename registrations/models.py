from django.db import models

class team(models.Model):
  team_id = models.CharField(max_length=6)
  team_name = models.CharField(max_length=20)
  def __str__(self):
    return self.team_id

class user(models.Model):
    year = [
  (1, "1st"),
  (2, "2nd"),
  (3, "3rd"),
  (4, "4th"),
  ]
    title = [
    ('male', 'Mr.'),
    ('female', 'Mrs.')
    ]

    username = models.CharField(max_length=10,null=False)
    first_name = models.CharField(max_length=15,null=False)
    last_name = models.CharField(max_length=15)
    mob = models.CharField(max_length=10,unique=True,null=False)
    title = models.CharField(max_length=6,choices=title,default='other')
    mail = models.EmailField(unique=True,null=False)
    dob = models.DateField(null=False)
    college = models.CharField(max_length=30,null=True)
    course = models.CharField(max_length = 25,null=True)
    year = models.PositiveIntegerField(choices=year)
    city = models.CharField(max_length=30,null=False)
    about = models.TextField(null=False)
    skills = models.TextField(null=False)
    githubUrl = models.URLField()
    linkedinUrl = models.URLField()
    profile_pic = models.ImageField(storage='600kb',blank=True,default='.static/resources/hack_logo-hd.png')
    team_id = models.ForeignKey(team, on_delete = models.CASCADE)

    def __str__(self):
      return self.first_name
