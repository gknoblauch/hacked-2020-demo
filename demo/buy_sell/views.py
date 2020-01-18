from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from buy_sell.models import Ad, Profile
from buy_sell.forms import AdForm


# Create your views here.
def index(request):

    ads = Ad.objects.order_by("-posted")

    return render(request, "index.html", context=dict(recent_ads=ads))

@login_required
def create_listing(request):
    
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            new_ad = Ad(
                title=form.cleaned_data.get("title"),
                body=form.cleaned_data.get("body"),
                author=request.user.user_profile
            )

            new_ad.save()
            return redirect("buy_sell_index")

    return render(request, "create_ad.html", context=dict(form=AdForm))

def view_listing(request, ad_id):
    
    ad = get_object_or_404(Ad, pk=ad_id)

    return render(request, "ad_details.html", context=dict(ad=ad))