from django.shortcuts import render
from django.views import View
from .services.tinkoff import build_collection
from .services.binance import build_collection_crypto
from django.conf import settings


class StocksView(View):
    """Страница ценных бумаг"""
    template = 'money/stocks.html'

    def get(self, request, *args, **kwargs):
        stats_br, stocks_br, operations_usd_br, operations_usd_profit_br = build_collection('2001148671')
        stats_iis, stocks_iis, operations_usd_iis, operations_usd_profit_iis = build_collection('2004836843')
        # Операции по обмену доллара
        operations_usd = operations_usd_br + operations_usd_iis
        operations_usd.sort(key=lambda k: k["date"])
        for el in operations_usd:
            el['date'] = el['date'].strftime("%d.%m.%Y")
        operations_usd_profit = round(operations_usd_profit_br + operations_usd_profit_iis, 2)
        return render(request, self.template, context={
            'stats_br': stats_br,
            'stocks_br': stocks_br,
            'stats_iis': stats_iis,
            'stocks_iis': stocks_iis,
            'operations_usd_iis': operations_usd_iis,
            'operations_usd': operations_usd,
            'operations_usd_profit': operations_usd_profit,
            'tax_plus': int(settings.TINKOFF_TAX_PLUS)
        })


class CryptoView(View):
    """Страница криптовалют"""
    template = 'money/crypto.html'

    def get(self, request, *args, **kwargs):
        wallet, balance_wallet, deposits, balance_deposits = build_collection_crypto()
        return render(request, self.template, context={
            'wallet':wallet,
            'balance_wallet': balance_wallet,
            'deposits': deposits,
            'balance_deposits': balance_deposits
        })
