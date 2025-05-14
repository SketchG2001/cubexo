from django.contrib import admin
from .models import Employee,Ratings,Restaurant,Sales
from django.db.models import Avg


admin.site.register(Sales)
# admin.site.register(Restaurant)
admin.site.register(Ratings)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name','address','res_type']

    list_per_page=30


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile','salary','show_avg_sal','show_daily_sal']
    list_filter = ('name','mobile','email')
    search_fields = ('mobile','name','email')
    list_per_page=30
    
    def get_queryset(self, request):
        # Cache the average salary to avoid recomputing for every row
        self.avg_salary = Employee.objects.aggregate(avg_sal=Avg('salary'))['avg_sal']
        return super().get_queryset(request)

    def show_avg_sal(self, obj):
        # Use cached value set in get_queryset
        if self.avg_salary is None:
            return "N/A"
        return round(self.avg_salary, 2)
    show_avg_sal.short_description = 'Avg Salary'

    def show_daily_sal(self, obj):
        try:
            daily_sal = float(obj.salary) / 30
            return f"{daily_sal:.2f}"
        except (TypeError, ValueError):
            return "Invalid salary"
    show_daily_sal.short_description = "Daily Salary"