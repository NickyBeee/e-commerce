from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("activelisting",views.activelisting,name="activelisting"),
    path("closedlisting",views.closedlisting,name="closedlisting"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("listing/categories",views.categories,name="categories"),
    path("category/<str:category>",views.category,name="category"),
    path("listing/<int:listing_id>",views.listing_detail,name="listing_detail")
]
