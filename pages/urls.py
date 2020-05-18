from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required
from .views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
    path('create/', staff_member_required(PageCreate.as_view()), name = 'create'),
    path('update/<int:pk>', staff_member_required(PageUpdate.as_view()), name = 'update'),
    path('delete/<int:pk>', staff_member_required(PageDelete.as_view()), name = 'delete')
], 'pages') # para acceder a las vistas: pages:pages, pages:page, pages:create