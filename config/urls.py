"""

"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns # translate
from django.utils.translation import gettext_lazy as _ # для перевода отдельных приложений

from payment import webhooks # из за перевода переноситм сюда ( из payment)


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path(_('cart/'), include('cart.urls', namespace='cart')),
    path(_('orders/'), include('orders.urls', namespace='orders')),
    path(_('payment/'), include('payment.urls', namespace='payment')),
    path(_('coupons/'), include('coupons.urls', namespace='coupons')),
    path('rosetta/', include('rosetta.urls')),
    path('', include('shop.urls', namespace='shop')),

)

# из за перевода переноситм сюда ( из payment)
urlpatterns += [path('payment/webhook/', webhooks.stripe_webhook,
name='stripe-webhook'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
