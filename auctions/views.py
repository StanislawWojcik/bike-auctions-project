from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .forms import AuctionForm, AuctionSeachForm
from .models import Auction, Order

def index(request):
    return render(request, 'auctions/index.html')

def auction_list(request):
    template = 'auctions/auction_list.html'
    auction_list = Auction.objects.order_by('date_added')
    context = {'auction_list': auction_list}
    return render(request, template, context)

@login_required
def add_auction(request):
    template = 'auctions/add_auction.html'
    if request.method != 'POST':
        form = AuctionForm()
    else:
        form = AuctionForm(request.POST, request.FILES)
        if form.is_valid():
            add_auction = form.save(commit=False)
            add_auction.user = request.user
            add_auction.save()
            return redirect('auctions:auction_list')
    context = {'form': form}
    return render(request, template, context)

@login_required
def edit_auction(request, auction_list_id):
    auction = Auction.objects.get(id=auction_list_id)
    if request.method != 'POST':
    	form = AuctionForm(instance=auction)
    else:
        form = AuctionForm(instance=auction, data=request.POST)
        if form.is_valid():
            check_auction_owner(request, auction)
            form.save()
            return redirect('auctions:auction_list')
    context = {'form':form, 'auction':auction}
    return render(request, 'auctions/edit_auction.html', context)

@login_required
def delete_auction(request, auction_list_id):
    auction = Auction.objects.get(id=auction_list_id)
    template = 'auctions/auction_list.html'
    if request.method == "POST":
        check_auction_owner(request, auction)
        auction.delete()
        return redirect('auctions:auction_list')
    context = {'auction': auction}
    return render(request, template, context)

def check_auction_owner(request, auction):
    if auction.user != request.user:
        raise Http404

def search(request):
    context = {}
    template = "auctions/search.html"
    if request.method == 'GET':
        auction_form = AuctionSeachForm()
        context["auction_form"] = auction_form
        return render(request, template, context)
    if request.method == "POST":
        auctions = Auction.objects.select_related()
        auction_form = AuctionSeachForm(request.POST)
        if auction_form.is_valid():
            title = auction_form.cleaned_data['title']
            if title:
                auctions = auctions.filter(title=title)

            bike_type = auction_form.cleaned_data['bike_type']
            if bike_type:
                auctions = auctions.filter(bike_type=bike_type)

            color = auction_form.cleaned_data['color']
            if color:
                auctions = auctions.filter(color=color)

            size = auction_form.cleaned_data['size']
            if size:
                auctions = auctions.filter(size=size)

            gears_min = auction_form.cleaned_data['gears_min']
            gears_max = auction_form.cleaned_data['gears_max']
            if gears_min:
                auctions = auctions.filter(gears__gte=gears_min)
            if gears_max:
                auctions = auctions.filter(gears__lte=gears_max)

            price_min = auction_form.cleaned_data['price_min']
            price_max = auction_form.cleaned_data['price_max']
            if price_min:
                auctions = auctions.filter(price__gte=price_min)
            if price_max:
                auctions = auctions.filter(price__lte=price_max)

            production_date_start = auction_form.cleaned_data['production_date_start']
            production_date_end = auction_form.cleaned_data['production_date_end']
            if production_date_start:
                auctions = auctions.filter(production_date__gte=production_date_start)
            if production_date_end:
                auctions = auctions.filter(production_date__lte=production_date_end)

        context['auctions'] = auctions
        context["auction_form"] = auction_form
        return render(request, template, context)


def auction_view(request, auction_list_id):
    template="auctions/auction_view.html"
    request_user = request.user
    context={}
    if request.method == "GET":
        auction = Auction.objects.get(id=auction_list_id)
        context['auction'] = auction
        context['request_user'] = request_user
        return render(request, template, context)

def buy_view(request):
    template="auctions/buy.html"
    return render(request, template)

@login_required
def add_to_cart(request, auction_list_id):
    template = 'auctions/buy.html'
    auction = Auction.objects.get(id=auction_list_id)
    order_item, created = Order.objects.get_or_create(
        auction=auction,
        user=request.user
    )
    if request.method == 'POST':
        auction.ordered = True
        order_item.ordered = True
        auction.save()
        order_item.save()
        return redirect('auctions:buy_view')
    context = {'auction': auction}
    return render(request, template, context)

@login_required
def cart_view(request):
    template = 'auctions/my_cart.html'
    items_in_cart = Order.objects.filter(user=request.user)
    context = {'items_in_cart': items_in_cart}
    return render(request, template, context)

@login_required
def my_auctions(request):
    template ='auctions/my_auctions.html'
    my_auctions = Auction.objects.filter(user=request.user)
    context = {'my_auctions': my_auctions}
    return render(request, template, context)

@login_required
def remove_from_cart(request, items_in_cart):
    item = Order.objects.get(id=items_in_cart)

    template = 'auctions/my_cart.html'
    if request.method == "POST":
        item.delete()
        item.auction.ordered = False
        item.auction.save()
        return redirect('auctions:auction_list')
    context = {'item': item}
    return render(request, template, context)

