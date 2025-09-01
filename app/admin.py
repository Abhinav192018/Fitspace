from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from datetime import timedelta
from .models import InteriorWork, GalleryImage, Blog, Featured_Blog, banner_Image, Contact,Services


# ✅ Show Image Preview Helper
def image_preview(obj):
    if obj.image:
        return format_html('<img src="{}" style="height: 80px; width: auto; border-radius: 6px;" />', obj.image.url)
    return "No Image"


@admin.register(banner_Image)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ("preview", "description")

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;"/>', obj.image.url)
        return "No Image"

    preview.short_description = "Image"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("id", "preview")

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;"/>', obj.image.url)
        return "No Image"

    preview.short_description = "Image"


@admin.register(InteriorWork)
class InteriorWorkAdmin(admin.ModelAdmin):
    list_display = (
        "main_image_preview", "interior_type", "client_name", "location", "completion_date", "created_at", 
    )
    list_filter = ("interior_type", "location", "completion_date", "created_at")
    search_fields = ("title", "client_name", "location")

    def main_image_preview(self, obj):
        if obj.image1:
            return format_html('<img src="{}" style="height:60px;"/>', obj.image1.url)
        return "No Image"

    main_image_preview.short_description = "Main Image"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
       "image_preview", "category", "author_name", "published_date", "updated_at", 
    )
    list_filter = ("category", "published_date", "updated_at")
    search_fields = ("title", "author_name")

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;"/>', obj.image.url)
        return "No Image"

    image_preview.short_description = "Blog Image"


@admin.register(Featured_Blog)
class FeaturedBlogAdmin(admin.ModelAdmin):
    list_display = (
        "image_preview", "category", "author_name", "published_date", "updated_at", 
    )
    list_filter = ("category", "published_date", "updated_at")
    search_fields = ("title", "author_name")

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;"/>', obj.image.url)
        return "No Image"

    image_preview.short_description = "Featured Image"


# ✅ Custom Date Filter for Contact
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


# ✅ Correct Contact Admin
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subject', 'created_at')
    list_filter = (
        ContactDateFilter,  # custom quick filter
        ('created_at', admin.DateFieldListFilter),  # calendar/date filter
    )
    search_fields = ('name', 'phone', 'subject')



@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("image_preview", "title", "short_description")
    search_fields = ("title", "description")

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = "Service Image"

    def short_description(self, obj):
        return (obj.description[:75] + "...") if len(obj.description) > 75 else obj.description
    short_description.short_description = "Description"