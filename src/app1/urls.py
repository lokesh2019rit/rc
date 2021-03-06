from django.urls import path, re_path, include
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import (
    User_Delete,
    login,
    TransactionListView,
    BillListView,
    ProductListView,
    ProductDeleteView,
    Buy,
    Sell,
    Expiry,
    Product_Update,
    Profit,
    ProductSearch,
    Billing,
    unauth_pdf,
    Generate_PDF,
)

urlpatterns = [
    # path("", login, name="login"),
    path("login/", login, name="login"),
    path("auth/user_delete/", csrf_exempt(User_Delete.as_view()), name="user_delete"),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    url(r"^api/bill/$", BillListView.as_view()),
    url(r"^api/productlist/$", ProductListView.as_view()),
    url(r"^api/productlist/(?P<pk>\d+)/$", ProductDeleteView.as_view()),
    url("api/buy/", csrf_exempt(Buy.as_view())),
    url("api/sell/", csrf_exempt(Sell.as_view())),
    url("api/profit/", csrf_exempt(Profit.as_view())),
    url(r"api/update/(?P<pid>\d+)/$", csrf_exempt(Product_Update.as_view())),
    # Might be useless
    url(r"api/transactions/$", TransactionListView.as_view()),
    url(r"api/explist/", Expiry.as_view()),
    url("api/order/", Billing.as_view()),
    path("api/pdf/<int:bill_id>", Generate_PDF.as_view()),
    path("api/wejwafjbf204729487/<int:bill_id>", unauth_pdf),
    # url("api/search/", csrf_exempt(SearchResultsView.as_view())),
    url("api/prodsearch/", ProductSearch.as_view()),
    re_path(r"^(?:.*)/?$", login, name="login"),
]
