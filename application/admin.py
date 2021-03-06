from django.contrib import admin
from .models import Assignment, Solution, UserProfile,Course
# Register your models here.


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'body', 'student')
    list_filter = ('assignment', 'submission_date', 'student')

class SolutionInline(admin.TabularInline):
    model = Solution

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'updated', 'deadline')
    list_filter = ('semester', 'deadline', 'updated')
    inlines = [SolutionInline]

class UserProfileAdmin(admin.ModelAdmin):
	pass

#Register the admin class with the associated model
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Course)




#Admin Usename = Ankita
#Admin Email = ankitapanchal0662@gmail.com
#Admin Password = anki0662