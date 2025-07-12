# webtienganh/views.py

#import os
#from django.views.generic import View
#from django.http import HttpResponse

#class FrontendAppView(View):
   # def get(self, request):
      #  try:
        #    with open(os.path.join('front_end', 'build', 'index.html')) as f:
             #   return HttpResponse(f.read())
      #  except FileNotFoundError:
          # return HttpResponse("index.html not found!", status=501)

import os
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

class FrontendAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.BASE_DIR, 'front_end', 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(
                "index.html not found. Have you built the React app?", status=501
            )

