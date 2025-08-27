from django.contrib import admin
from .models import InteriorWork,GalleryImage,Blog,Featured_Blog,banner_Image,Contact
# Register your models here.


admin.site.site_header = "Fitspace Admin"
admin.site.site_title = "Fitspace Admin Portal"
admin.site.index_title = "Welcome to Fitspace Admin Portal"

admin.site.register(InteriorWork)
admin.site.register(GalleryImage)
admin.site.register(Blog)
admin.site.register(Featured_Blog)
admin.site.register(banner_Image)



from django.contrib import admin
from django.utils import timezone
from datetime import timedelta
from .models import Contact


class ContactDateFilter(admin.SimpleListFilter):
    title = 'Created Date'   # Sidebar title
    parameter_name = 'created_at'

    def lookups(self, request, model_admin):
        return [
            ('today', 'Today'),
            ('yesterday', 'Yesterday'),
            ('last_7_days', 'Last 7 Days'),
            ('this_month', 'This Month'),
            ('last_month', 'Last Month'),
            ('this_year', 'This Year'),
            ('last_year', 'Last Year'),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        now = timezone.now().date()

        if value == 'today':
            return queryset.filter(created_at__date=now)
        if value == 'yesterday':
            return queryset.filter(created_at__date=now - timedelta(days=1))
        if value == 'last_7_days':
            return queryset.filter(created_at__date__gte=now - timedelta(days=7))
        if value == 'this_month':
            return queryset.filter(
                created_at__year=now.year,
                created_at__month=now.month
            )
        if value == 'last_month':
            first_day_this_month = now.replace(day=1)
            last_month_end = first_day_this_month - timedelta(days=1)
            return queryset.filter(
                created_at__year=last_month_end.year,
                created_at__month=last_month_end.month
            )
        if value == 'this_year':
            return queryset.filter(created_at__year=now.year)
        if value == 'last_year':
            return queryset.filter(created_at__year=now.year - 1)

        return queryset


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subject', 'created_at')
    list_filter = (ContactDateFilter,)  # 👈 custom filter here


