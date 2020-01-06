from django.contrib import admin
from Test.models import TestMarks
from .models import User

# Register your models here.

class TestMarksInLine(admin.TabularInline):
    model = TestMarks

@admin.register(User)
class Users(admin.ModelAdmin):
    inlines = [TestMarksInLine,]