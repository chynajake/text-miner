from django.urls import path

from apps.mine import views

app_name = 'mine'
urlpatterns = [
    path('text/create/', views.TextCreateView.as_view(), name='text-create'),
]

admin_patterns = [
    path('admin/', views.AdminInitialView.as_view(), name='admin-initial'),
    path('admin/texts/', views.AdminRawTextListView.as_view(), name='admin-raw-texts'),
    path('admin/texts/create/', views.AdminRawTextCreateView.as_view(), name='admin-raw-text-create'),
    path('admin/texts/<int:pk>/', views.AdminRawTextDetailView.as_view(), name='admin-raw-text-detail'),
    path('admin/texts/<int:pk>/moderate/', views.AdminModerateTextView.as_view(), name='admin-raw-text-moderate'),
    path('admin/texts/moderated/', views.AdminModeratedTextListView.as_view(), name='admin-moderated-text'),
    path('admin/texts/moderated/<int:pk>/', views.AdminModeratedTextDetailView.as_view(), name='admin-moderated-text-detail'),
    path('admin/miners/', views.AdminMinerListView.as_view(), name='admin-miners'),
    path('admin/moderators/', views.AdminModeratorListView.as_view(), name='admin-moderators'),
]
moderator_patterns = [
]
miner_patterns = []
urlpatterns += admin_patterns
urlpatterns += moderator_patterns
urlpatterns += miner_patterns