from django.contrib import admin

from .models import Balie, Tel

class BalieInline(admin.StackedInline):
    model = Balie
    extra = 0

@admin.register(Balie)
class BalieAdmin(admin.ModelAdmin):
    pass

@admin.register(Tel)
class TelAdmin(admin.ModelAdmin):
    inlines = [BalieInline,]
