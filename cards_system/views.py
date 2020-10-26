from django.shortcuts import render, get_object_or_404, redirect
from cloudinary.forms import cl_init_js_callbacks
from .models import Child, Stage_content
from project_site.settings import get_secret

MAX_STAGES = 3 #First stage: 0
CHILD_FOR_DEMO_SLUG = 'cary-krell' #slug

def set_language(request, lang):
    #Handle language changes
    try:
        #print("--------------------------")
        if not hasattr(request, 'session') or not request.session['lang']:
            #print("no request.session OR no request.session['lang'], so set to 'en'")
            request.session['lang'] = 'en'
        else:
            #print("current request.session['lang'] = ", request.session['lang'])
            if request.session['lang'] != lang:
                #print("set request.session['lang'] = ", lang)
                request.session['lang'] = lang
    except:
        #print("Error - exception -  so set session.lang to 'en'")
        request.session['lang'] = 'en'

    return redirect(request.META['HTTP_REFERER'])

#Home page / landing page
def home(request):
    #Reset demo card to the first stage
    child = get_object_or_404(Child, slug=CHILD_FOR_DEMO_SLUG)
    child.current_stage = 0
    child.save()
    #Get url for film fragment on gdrive (in English / Spanish)
    film_fragment_on_gdrive = get_secret('FILM_FRAGMENT_ON_GDRIVE')
    fragmento_pelicula_en_gdrive = get_secret('FRAGMENTO_PELICULA_EN_GDRIVE')

    return render(request, 'index.html', {'child_for_demo_slug': CHILD_FOR_DEMO_SLUG, 'film_fragment_on_gdrive': film_fragment_on_gdrive, 'fragmento_pelicula_en_gdrive': fragmento_pelicula_en_gdrive})

#Returns a child current stage
def stage(request, slug=None):
    child = get_object_or_404(Child, slug=slug)
    stage_content = get_object_or_404(Stage_content, child=child, stage_number = child.current_stage)
    
    if child.current_stage < 3:
        child.current_stage += 1
        send_to_printer = False
    else: 
        #last stage. Reset stage, and send to printer.
        child.current_stage = 0
        send_to_printer = True
    child.save()

    return render(request, 'cards_system/stage.html', {'child': child, 'stage_content': stage_content, 'send_to_printer': send_to_printer})
