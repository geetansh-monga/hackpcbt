from django.db import models

class team(models.Model):
  team_id = models.CharField(unique=True,max_length=6)
  team_name = models.CharField(max_length=20)
 
  def __str__(self):
    return self.team_id

class user(models.Model):
    year = [
  ("first", "1st"),
  ("second", "2nd"),
  ("third", "3rd"),
  ("fourth", "4th"),
  ]
  
    title = [
    ('male', 'Mr.'),
    ('female', 'Mrs.')
    ]

    username = models.CharField(max_length=40,blank=True,)
    first_name = models.CharField(max_length=20,null=False)
    last_name = models.CharField(max_length=20,null=True)
    mob = models.CharField(max_length=10,unique=True,blank=False)
    title = models.CharField(max_length=6,choices=title,blank=False)
    mail = models.EmailField(unique=True,blank=False)
    dob = models.TextField(blank=False)
    college = models.CharField(max_length=30)
    course = models.CharField(max_length = 25,blank=False)
    year = models.CharField(max_length=10,choices=year,blank=False)
    city = models.CharField(max_length=30,blank=False)
    about = models.TextField(blank=False)
    skills = models.TextField(blank=False)
    githubUrl = models.URLField()
    linkedinUrl = models.URLField()
    team_id = models.ForeignKey(team, on_delete = models.CASCADE)
    teamname = models.CharField(max_length=30,blank=True)

    def __str__(self):
      return self.first_name
