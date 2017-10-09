# from django.conf.urls import url
# from snippets import views
# from rest_framework.urlpatterns import format_suffix_patterns
#
# from snippets.views import HeroViewSet
# from rest_framework import renderers

from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from snippets import views as core_views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers



router = routers.SimpleRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'signin',views.UserViewSet)

urlpatterns = [
    url(r'^search/(?P<name>[-\w]+)/$', views.SearchList.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^rest-auth/', include('rest_auth.urls')),
url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))

]
urlpatterns = urlpatterns+router.urls







# heroes_list = HeroViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# heroes_detail = HeroViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# urlpatterns = format_suffix_patterns([
#     url(r'^heroes/$', heroes_list, name='heroes-list'),
#     url(r'^heroes/(?P<pk>[0-9]+)/$', heroes_detail, name='heroes-detail'),
# ])

# urlpatterns = [
#     url(r'^heroes/$', views.Hero_list.as_view()),
#     url(r'^heroes/(?P<pk>[0-9]+)/$', views.Hero_detail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)