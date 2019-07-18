from django.conf.urls import include, url

urlpatterns = [
	url(r'^$', 'usermanagement.views.main_page'),

    #url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^login/$', 'usermanagement.views.login_page', name='login'),
    url(r'^logout/$', 'usermanagement.views.logout_page', name='logout'),
    
    #deactivate registration form for staff: do not delete
	#url(r'^register/$', 'usermanagement.views.register_page', name='register'),
	url(r'^edit/(?P<search_id>\d+)$', 'usermanagement.views.staff_update', name='staff_update'),
  	#url(r'^(?P<search_id>[0-9]+)/$', 'usermanagement.views.staff_profile', name='staff_profile'),
    #url(r'^(?P<search_id>.*)/$', 'usermanagement.views.staff_profile', name='staff_profile'),

    #(r'^login$', 'django.contrib.auth.views.login', {'redirect_if_logged_in': '/'})
    
	#url(r'^profile/$', 'usermanagement.views.profile_page', name='staff_profile'),
    url(r'^profile/$', 'usermanagement.views.staff_profile', name='staff_profile'),
]