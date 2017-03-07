from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from workatolist.apiworkatolist.urls import router

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/v1.0/', include(router.urls)),
]
