from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homePage, name='home'),
    url(r'^message/$', views.MessagePage.as_view(), name='message'),
    url(r'^represent/', views.meetTheReps, name='represent'),
    url(r'^calendar/$', views.calEvents, name='calendar'),
    url(r'^announce/$', views.announcements, name='announce'),
    url(r'^announce/(?P<id>[0-9]+)/$', views.announcement, name='eachAnnouncement'),
    url(r'^contacts/',views.ContactNumbers.as_view(),name='contacts'),
    url(r'^nitk_life/', views.NitkLifePage.as_view(), name='nitk_life'),
    url(r'^blog/$', views.blogPage, name='blogs'),
    url(r'^blog/(?P<num>[0-9]+)/$', views.blogPage, name='eachBlog'),
    url(r'^news/$', views.newsPage, name='news'),
    url(r'^news/(?P<num>[0-9]+)/$', views.newsPage, name='eachNews'),
    url(r'^faq/',views.FAQ.as_view(),name='faq'),
    url(r'^senate/',views.SenatePage.as_view(),name='senate'),
    url(r'^minutes/',views.minutes,name='minutes'),
    url(r'^mou/',views.mous,name='mous'),
    url(r'^grants/',views.grants,name='grants'),
    url(r'^reports/',views.reports,name='reports'),
    url(r'^resources/',views.resources,name='resources'),
    url(r'^letters/',views.letters,name='letters'),

]
