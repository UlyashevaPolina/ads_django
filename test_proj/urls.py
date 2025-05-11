from django.contrib import admin
from django.urls import path
from ads.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('name/<str:name>',index),
    path('cat/<str:cat>',index),
    path('auth', auth),
    path('logout', u_logout),
    path('register', register),
    path('add_ads', add_ads),
    path('edit_ads/<int:id>', edit_ads),
    path('del_ads/<int:id>', del_ads),
    path('exchange/', exchange),
    path('create_exchange/<int:senderAdId>/<int:receiverAdId>', create_exchange),
    path('accept-offer/<int:id>',acceptOffer),
    path('decline-offer/<int:id>',declineOffer),

]
