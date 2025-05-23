from django.contrib import admin
from .models import Tenant, Domain


# Custom admin to hide Tenant and Domain for non-superusers
class SuperuserOnlyAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser  # Only superusers can see these models

# Custom admin for tenant-specific models
class TenantModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            # Filter by user's tenant (adjust based on your tenant setup)
            return qs.filter(tenant=request.user.tenant)
        return qs

    def has_add_permission(self, request):
        return request.user.is_superuser or hasattr(request.user, 'tenant')

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return obj.tenant == request.user.tenant
        return True

    def has_delete_permission(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return obj.tenant == request.user.tenant
        return True

# Register the models with custom admin classes
admin.site.register(Tenant, SuperuserOnlyAdmin)
admin.site.register(Domain, SuperuserOnlyAdmin)