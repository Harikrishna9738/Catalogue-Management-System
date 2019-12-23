from django.db import models


# Create your models here.
class Category(models.Model):
    """category models,this has a tree structure using foriegn key.
    the name is unique"""
    name = models.CharField(max_length=250, unique=True, help_text="category name,name must be unique")
    parent_category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, help_text="this was created at starting")
    last_modified = models.DateTimeField(auto_now_add=True, help_text="this was created whn modified last")

    def __str__(self):
        return self.name

    def get_breadcrumbs(self):
        get_breadcrumbs = []
        category = self
        parent_category = category.parent_category
        while parent_category is not None:
            get_breadcrumbs.append(category.name)
            parent_category = parent_category.parent_category
        get_breadcrumbs.append(category.name)
        return get_breadcrumbs


class Brand(models.Model):
    """brand models,this has a tree structure using foriegn key.
    the name is unique"""
    name = models.CharField(max_length=250, unique=True, help_text="brand name,name must be unique")
    date_created = models.DateTimeField(auto_now_add=True, help_text="this was when brand created")
    last_modified = models.DateTimeField(auto_now_add=True, help_text="this was created when modified last")

    def __str__(self):
        return self.name


class Product(models.Model):
    """holds the brand and category is unique.a product can have multiple specifications"""
    name = models.CharField(max_length=250, unique=True, help_text="product name,name must be unique")
    brand = models.ForeignKey(Brand, help_text="the brand belongs to product", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, help_text="the category belongs to product", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, help_text="this was when brand created")
    last_modified = models.DateTimeField(auto_now_add=True, help_text="this was created when modified last")

    def __str__(self):
        return self.name


class Specifications(models.Model):
    """specifications models,about the product specifications"""
    key = models.CharField(max_length=250, unique=True, help_text="the key of specification")
    vale = models.CharField(max_length=250, unique=True, help_text="the value of specification")
    unit = models.CharField(max_length=250, null=True, unique=True, help_text="the unit of specification")
    date_created = models.DateTimeField(auto_now_add=True, help_text="this was when brand created")
    last_modified = models.DateTimeField(auto_now_add=True, help_text="this was created when modified last")

    def __str__(self):
        return self.key + ' ,' + self.value + (' ' + self.unit if + self.unit else ' ')
