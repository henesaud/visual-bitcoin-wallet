from django.contrib import admin
from .models import Wallet


class WalletAdmin(admin.ModelAdmin):
	list_display = 	('name', 'description','type', 'master_public_key')

admin.site.register(Wallet, WalletAdmin)
