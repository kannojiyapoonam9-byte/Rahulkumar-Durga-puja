from django.contrib import admin
from .models import Post, Donation, Contact

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'address', 'date', 'is_approved')
    list_filter = ('is_approved', 'date')
    search_fields = ('name', 'address', 'phone')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    search_fields = ('name', 'email')

from .models import CommitteeMember, UserProfile
@admin.register(CommitteeMember)
class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'role')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

