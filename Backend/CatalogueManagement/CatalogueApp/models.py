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
