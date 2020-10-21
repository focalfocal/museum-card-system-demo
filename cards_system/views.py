from django.shortcuts import render, get_object_or_404
from cloudinary.forms import cl_init_js_callbacks
from .models import Child, Stage_content
from project_site.settings import get_secret

MAX_STAGES = 3 #First stage: 0
CHILD_FOR_DEMO = 'cary-krell' #slug

#Home page / landing page
def home(request):
    #Reset demo card to the first stage
    child = get_object_or_404(Child, slug=CHILD_FOR_DEMO)
    child.current_stage = 0
    child.save()
    #Get url for film fragment on gdrive (in English)
    film_fragment_on_gdrive = get_secret('FILM_FRAGMENT_ON_GDRIVE')

    return render(request, 'index.html', {'child_for_demo': CHILD_FOR_DEMO, 'film_fragment_on_gdrive': film_fragment_on_gdrive})

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
