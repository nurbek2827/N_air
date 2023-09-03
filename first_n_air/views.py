import random

from django.shortcuts import render, redirect

from first_n_air.forms import ChoisesForm
from first_n_air.models import Category, Sneakers, Buy, Advertising
import numpy

# Create your views here.

def home(requests):
    ctg = Category.objects.all()
    advertising = Advertising.objects.all()
    sneaker = Sneakers.objects.all()
    random_adv = random.choice(advertising)
    ctx = {
        "ctg": ctg,
        "sneaker": sneaker,
        "random_adv": random_adv,

    }
    return render(requests, "blog/index.html", ctx)


def contact(requests):
    ctx = {

    }
    return render(requests, "blog/contact.html", ctx)


def product(requests, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    sneaker = Sneakers.objects.all().filter(type_id=category.id)

    ctx = {
        "ctg": ctg,
        "category": category,
        "sneaker": sneaker
    }
    return render(requests, "blog/products.html", ctx)


def register(requests):
    ctx = {

    }
    return render(requests, "blog/register.html", ctx)


def single(requests, pk=None):
    ctg = Category.objects.all()
    products_pk = Sneakers.objects.get(pk=pk)
    sneakers = Sneakers.objects.all()
    random_sneak = numpy.random.choice(sneakers, size=3, replace=False)
    form = ChoisesForm()
    if requests.POST:
        forms = ChoisesForm(requests.POST or None,
                           requests.FILES or None)

        if forms.is_valid():
            root = forms.save()
            root= Buy.objects.get(pk=root.id)
            root.product = products_pk
            root.save()
            return redirect("home")
        else:
            print(forms.errors)
    ctx = {
        "ctg": ctg,
        "product_pk": products_pk,
        "form": form,
        "random_sneak": random_sneak,
        "sneakers": sneakers
    }
    return render(requests, "blog/single.html", ctx)
