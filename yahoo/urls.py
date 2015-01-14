from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^home', 'bmw.views.home'),
	url(r'^login', 'bmw.views.login'),
	url(r'^man_home', 'bmw.views.man_home'),
	url(r'^woman_home', 'bmw.views.woman_home'),
	url(r'^logout', 'bmw.views.logout_view'),
	url(r'^create', 'bmw.views.create_user'),
	#url(r'^next', 'bmw.views.next'),

    url(r'^admin/', include(admin.site.urls)),
)
