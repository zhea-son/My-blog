from django.contrib import admin
from .models import Post
from django import forms
from django.contrib import messages
# from ckeditor.widgets import CKEditorWidget

# Register your models here.

# admin.site.register(Post)

# class PostAdminForm(forms.ModelForm):
#     text = forms.CharField(widget=CKEditorWidget(),required=FALSE)

#     class Meta:
#         model = Post
#         fields = "__all__"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'published_date', 'author', 'is_active')
    list_filter = ('title', 'created_date', 'published_date')
    search_fields = ('title',)
    # form = PostAdminForm


    # def active(self, obj):
    #     return obj.is_active==True

    # active.boolean == True

    def make_active(ModelAdmin, request, queryset):
        queryset.update(is_active=True)
        messages.success(request, "Seleected REcord(s) marked as active successfully.")

    def make_inactive(ModelAdmin, request, queryset):
        queryset.update(is_active=False)
        messages.success(request, "Seleected REcord(s) marked as inactive successfully.")

    def has_delete_permission(self, request, obj=None):
        return False

    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive,"Make Inactive")