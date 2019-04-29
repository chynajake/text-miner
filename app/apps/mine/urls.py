from django.urls import path

from apps.mine import views

app_name = 'mine'
urlpatterns = [
    path('text/create/', views.TextCreateView.as_view(), name='text-create'),
]

admin_patterns = [
    path('admin/', views.AdminInitialView.as_view(), name='admin-initial'),
    path('admin/raw_texts/', views.AdminRawTextListView.as_view(), name='admin-raw-texts'),
    path('admin/raw_texts/create/', views.AdminRawTextCreateView.as_view(), name='admin-raw-text-create'),
    path('admin/miners/', views.AdminMinerListView.as_view(), name='admin-miners'),
    path('admin/miners/', views.AdminModeratorListView.as_view(), name='admin-moderators'),
]
moderator_patterns = []
miner_patterns = []
urlpatterns += admin_patterns
urlpatterns += moderator_patterns
urlpatterns += miner_patterns