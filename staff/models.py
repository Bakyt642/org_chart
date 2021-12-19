from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Staff(MPTTModel) :
    name = models.CharField(max_length=50, unique=False)
    job_title = models.CharField(max_length=50)
    onboard_date = models.DateTimeField(auto_now_add=True)
    salary = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', )

    def __str__(self) :
        return f'id {self.id}  Chief_id  {self.parent_id}  Name:  {self.name}'

    def get_absolute_url(self) :
        return reverse('staff_detail', kwargs={'pk' : self.pk, })

    class MPTTMeta :
        """
        adds some tweaks to django-mptt
        """
        order_insertion_by = [
            'id']  # in this case, just order_insertion_by This indicates the natural ordering of the data in the tree.
