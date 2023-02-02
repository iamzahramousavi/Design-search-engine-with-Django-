from django.db import models


class DataScraped(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.URLField(max_length=1000, null=True, blank=True)
    titleOrg = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    pubDate = models.CharField(max_length=200, null=True, blank=True)
    bodyOrg = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    createAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.titleOrg


class Tokens(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    posting = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.name


class Idf(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.OneToOneField(Tokens, on_delete=models.CASCADE, blank=True, null=True, related_name='tok')
    idf = models.FloatField(default=1)

    def __str__(self):
        return self.token.name


class TfIdfList(models.Model):
    id = models.AutoField(primary_key=True)
    doc = models.OneToOneField(DataScraped, on_delete=models.CASCADE, blank=True, null=True, related_name='dc')
    tfIdfFirstList = models.JSONField(max_length=5000, null=True, blank=True)
    tfIdfSecondList = models.JSONField(max_length=5000, null=True, blank=True)
    lengthFirst = models.FloatField(default=1, null=True, blank=True)
    lengthSecond = models.FloatField(default=1, null=True, blank=True)

    def __str__(self):
        return self.doc.title

#
# class ClassCrf(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50, null=True, blank=True)
#     CrfFirstList = models.JSONField(max_length=5000, null=True, blank=True)
#     CrfSecondList = models.JSONField(max_length=5000, null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Category(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50, null=True, blank=True)
#     docList = models.JSONField(max_length=5000, null=True, blank=True)
#
#     def __str__(self):
#         return self.name
