from django.db import models


class Wallet(models.Model):
    WALLET_TYPES = (
        ("P2PKH", "Legacy"),
        ("P2SH", "Compatibility"),
        ("Bech32 ", "Segwit"),
    )

    id_wallet = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(
        choices=WALLET_TYPES, max_length=60, verbose_name="Keystore type"
    )
    master_public_key = models.CharField(
        max_length=62, verbose_name="Master Public Key"
    )

    def _str_(self):
        return self.name
