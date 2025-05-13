from django.contrib import admin
from .models import Employee,Ratings,Restaurant,Sales
from django.db.models import Avg


admin.site.register(Sales)
admin.site.register(Restaurant)
admin.site.register(Ratings)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile','salary','show_avg_sal','show_daily_sal']
    list_filter = ('name','mobile','email')
    search_fields = ('mobile','name','email')
    
    
    def show_avg_sal(self,obj):
        result = Employee.objects.aggregate(
            avg_sal = Avg('salary'),
        )
        avg_sal = result['avg_sal']
        return round(avg_sal,2)
    
    show_avg_sal.short_description = 'Avg Salary'

    def show_daily_sal(self,obj):
        try:
            daily_sal = float(obj.salary)/30
            return f"{daily_sal:.2f}"
        except ValueError:
            return "Invalid salary"

    show_daily_sal.short_description = "Daily salary"    