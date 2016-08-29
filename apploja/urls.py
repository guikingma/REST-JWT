from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token
from apploja import views

urlpatterns = [
    url(r'^pedidos/$', views.OrderList.as_view()),
    url(r'^pedidos/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
    url(r'^pedidos/(?P<pk>[0-9]+)/desc/$', views.OrderDesc.as_view()),
    url(r'^produtos/$', views.ProductList.as_view()),
    url(r'^produtos/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^produtos/(?P<pk>[0-9]+)/desc/$', views.ProductDesc.as_view()),

    # Jwt Token
    url(r'^api-token-auth/', obtain_jwt_token),
]

# add sufix (ex .json)
urlpatterns = format_suffix_patterns(urlpatterns)
