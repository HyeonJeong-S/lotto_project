from django.contrib import admin
from .models import LottoTicket, LottoDraw

@admin.register(LottoTicket)
class LottoTicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'numbers', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user', 'numbers')

@admin.register(LottoDraw)
class LottoDrawAdmin(admin.ModelAdmin):
    list_display = ('round', 'winning_numbers', 'draw_date')
    list_filter = ('draw_date',)
    search_fields = ('winning_numbers',)
