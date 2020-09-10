from django.db import models

# Create your models here.
class category(models.Model):
    id = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="category"

    def __str__(self):
        return self.categoryname

class creator(models.Model):
    id = models.AutoField(primary_key=True)
    creativename = models.CharField(max_length=200)
    üye_date = models.DateTimeField(auto_now_add=True)
    üye_foto=models.ImageField(upload_to="üyeler/", height_field=None, width_field=None, max_length=100)
    class Meta:
        db_table="creator"
    def __str__(self):
        return self.creativename

class product(models.Model):
    id = models.AutoField(primary_key=True)
    productname= models.CharField(max_length=200)
    category= models.ForeignKey(category, on_delete=models.CASCADE)
    creator= models.ForeignKey(creator, on_delete=models.CASCADE)
    publish_date = models.DateTimeField( auto_now_add=True)
    price=models.DecimalField( max_digits=5, decimal_places=2)
    oldprice=models.DecimalField( max_digits=5, decimal_places=2,blank=True,null=True)
    class Meta:
        db_table="product"
    def __str__(self):
        return self.productname

class altcategory(models.Model):
    id = models.AutoField(primary_key=True)
    altcategoryname = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    category= models.ForeignKey(category, on_delete=models.CASCADE)
    class Meta:
        db_table="altcategory"

    def __str__(self):
        return self.altcategoryname
