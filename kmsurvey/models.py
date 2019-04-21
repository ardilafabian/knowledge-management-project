from django.db import models

class Approach(models.Model):
    name = models.CharField(max_length=30)
    score = models.FloatField()

    def __str__(self):
        return '[Approach: %s, Score: %f]' % (self.name, self.score)

class Tool(models.Model):
    name = models.CharField(max_length=30)
    score = models.FloatField()
    approach = models.ForeignKey(Approach, on_delete=models.CASCADE)

    def __str__(self):
        return '[Tool: %s, Score: %f, Approach: %s]' % (self.name, self.score, self.approach)

class Scale_Choice(models.Model):
    TOTALLY_AGREE = 5
    AGREE = 4
    NEITHER_AGREE_NOR_DISAGREE = 3
    DISAGREE = 2
    TOTALLY_DISAGREE = 1

    SCALE_CHOICES = (
        (TOTALLY_AGREE, 'Totally Agree'),
        (AGREE, 'Agree'),
        (NEITHER_AGREE_NOR_DISAGREE, 'Neither agree nor disagree'),
        (DISAGREE, 'Disagree'),
        (TOTALLY_DISAGREE, 'Totally disagree'),
    )

    scale_choice = models.PositiveIntegerField(
        choices = SCALE_CHOICES,
        default = TOTALLY_AGREE,
    )

    def __str__(self):
        return '[SCALE - Value: %d]' % (scale_choice)

class Dicotomic_Choice(models.Model):
    YES = 5
    NO = 1

    DICOTOMIC_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No'),
    )

    dicotomic_choice = models.PositiveIntegerField(
        choices = DICOTOMIC_CHOICES,
        default = YES,
    )

    def __str__(self):
        return '[DICOTOMIC - Value: %d]' % (dicotomic_choice)

class Scale_Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice = models.ForeignKey(Scale_Choice, on_delete=models.CASCADE)

class Dicotomic_Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice = models.ForeignKey(Dicotomic_Choice, on_delete=models.CASCADE)
