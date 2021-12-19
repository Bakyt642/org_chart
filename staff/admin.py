from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Staff


class StaffAdmin(DraggableMPTTAdmin) :
    pass


admin.site.register(Staff, StaffAdmin)

