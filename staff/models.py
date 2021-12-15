from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Staff(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    job_title = models.CharField(max_length=200)
    onboard_date = models.DateTimeField(auto_now_add=False)
    salary = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', )

    def __str__(self):
        return f'id {self.id}  Chief_id  {self.parent_id}  Name:  {self.name}'

    class MPTTMeta:
        """
        adds some tweaks to django-mptt
        """
        order_insertion_by = ['name'] #in this case, just order_insertion_by This indicates the natural ordering of the data in the tree.


