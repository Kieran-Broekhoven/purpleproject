import os
import smtplib
import socket
import time
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# from django.templates.exceptions import TemplateDeosNotExist
from django.views.generic.base import TemplateView
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pprint import pprint

from api.getwlist import get_wishlist

cached_wishlist = []
last_cache = None


gmail_user = os.environ.get('gmail_user', 'thepurpleprojectmail@gmail.com')
gmail_password = os.environ.get('gmail_pwd')
svc_user = ' purpleproject@my-project-1470695517651.iam.gserviceaccount.com'
svc_key = '51ff364b976acadd86c31ca93ce455c06a2c2318'


def sendMail(request):
    # Log into server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    # Compose message
    data = request.POST
    fromAddr = data['email']
    name = data['name']
    subject = data['subject']
    msg = '<br>'.join(data['message'].splitlines())

    mime = MIMEMultipart()
    mime['From'] = fromAddr
    mime['To'] = 'info@thepurplepurpose.org'
 
    mime['Subject'] = 'Message from the Purple Project website'
    body = f"""<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Express Mail</title></head><body>
    <table style='width: 100%'>
    <thead style='text-align: center'><tr><td style='border:none' colspan='2'>
    </td></tr></thead><tbody><tr>
    <td style='border:none'><strong>Name:</strong> {name}</td>
    <td style='border:none'><strong>Email:</strong> {fromAddr}</td>
    </tr>
    <tr><td style='border:none'><strong>Subject:</strong> {subject}</td></tr>
    <tr><td></td></tr>
    <tr><td colspan='2' style='border:none'>{msg}</td></tr>
    </tbody></table>
    </body></html>"""
    mime.attach(MIMEText(body, 'html'))

    # Send message
    server.send_message(mime)
    
    return JsonResponse({'success': True})


def wishlist(request):
    global last_cache, cached_wishlist
    if last_cache is not None:
        if (last_cache+(60*60*24)) > time.time() and cached_wishlist:
            return JsonResponse({'wishlist': cached_wishlist})
    wishlist_id = '2ZHXUYP0TYC5E'
    wishlist = get_wishlist(wishlist_id)
    last_cache = time.time()
    cached_wishlist = wishlist
    return JsonResponse({'wishlist': wishlist})


def htmlPage(request, file):
    print("User: %s" % os.environ.get('gmail_user'))
    print("Debug: %s" % os.environ.get('DEBUG'))
    if not (file.endswith('.js') or file.endswith('.css') or file.endswith('.img') or file.endswith('.ico')):
        file += '.html'
    try:
        if not socket.gethostname().lower().startswith('Friday'):
            file = '/var/www/html/' + file
        return render(request, file)
    except Exception as e:
        print("E: %s" % str(e))
        return HttpResponse('Not found', status=404)


# temp_views = {}

# pages = ['info', 'impact', 'funding', 'events', 'wishlist']
# for page in pages:
#     temp_views[page] = TemplateView()
#     temp_views[page].template_name = page + '.html'
