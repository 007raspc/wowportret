# -*- coding: utf-8 -*-
from django.shortcuts import render,  get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import HttpResponse, HttpResponse, HttpResponseRedirect, Http404
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect, render
from django.template import loader, Context
from django.db.models import Q

from wowportret.forms import ContactForm, ItemForm


def main_page(request):
    # form_class, sended = get_form(request)
    # if sended:
    #     return redirect('thank_page')

    # return render(request, 'wowportret/index.html', {'form': form_class})
    return redirect('http://wowportret24.ru/')


def art_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/art.html', {'form': form_class})


def classic_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/classic.html', {'form': form_class})


def holst_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/holst.html', {'form': form_class})


def maslo_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/maslo.html', {'form': form_class})


def maslo2_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/pmaslo.html', {'form': form_class})


def popart_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/popart.html', {'form': form_class})


def portret_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/portret.html', {'form': form_class})


def baget_page(request):
        return redirect('thank_page')
  

def thank_page(request):
    return render(request, 'wowportret/components/thank.html', {})


def item_page(request, pk):
        return redirect('thank_page')

def gallery_page(request):
        return redirect('thank_page')

def gallery_detail(request, pk):
        return redirect('thank_page')

def get_form(request):
    form_class = ContactForm
    sended = False
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_phone = form.cleaned_data['contact_phone']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            # template of mail
            content = "name: " + contact_name + "\n"
            content = "phone " + contact_phone + "\n"
            content += "email " + contact_email + "\n"
            content += "text " + form_content + "\n"

            email = EmailMessage(
                "kateart@wowportret.ru",
                content,
                "kateart@wowportret.ru" + '',
                ['kateart222@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            if request.FILES:
                image = request.FILES['docfile']
                newdoc = Document(docfile=image)
                newdoc.save()
                email.attach_file(newdoc.docfile.path)

            email.send()
            sended = True
    return form_class, sended


def get_item_form(request):
    form_class = ItemForm
    sended = False
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_phone = form.cleaned_data['contact_phone']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']
            contact_item = form.cleaned_data['contact_item']

            # template of mail
            content = "name: " + contact_name + "\n"
            content = "phone " + contact_phone + "\n"
            content += "email " + contact_email + "\n"
            content += "text " + form_content + "\n"
            content += "extra:  " + contact_item + "\n"

            email = EmailMessage(
                "kateart@wowportret.ru",
                content,
                "kateart@wowportret.ru" + '',
                ['kateart222@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            if request.FILES:
                image = request.FILES['docfile']
                newdoc = Document(docfile=image)
                newdoc.save()
                email.attach_file(newdoc.docfile.path)

            email.send()
            sended = True
    return form_class, sended


def post_list(request):
        return redirect('thank_page')

def post_detail(request, pk):
        return redirect('thank_page')

    

    
    
def price_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/price.html', {'form': form_class})

def delivery_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/delivery.html', {'form': form_class})

def payment_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/payment.html', {'form': form_class})

def contacts_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/contacts.html', {'form': form_class})