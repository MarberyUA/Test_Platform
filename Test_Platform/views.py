from django.shortcuts import redirect

def main_page_redirect(request):
    return redirect('main_page_url', permanent=True)