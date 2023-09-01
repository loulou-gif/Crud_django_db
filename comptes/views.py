from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .forms import registreForm
from django.contrib.auth.models import User
from .models import Person, spirit, scolaire, professionnal
from .decorators import only_admin, match, new, genre

# Create your views here.

# formulaire de connexion

def connexion(request):
    request.user
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user =authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)   
            if request.user.last_login is not None:
                return redirect('home')
            else:
                return redirect('update', id=request.user.id)
        else:
            messages.info(request, "Mots de passe ou Username incorrecte")
        
    return render(request,'connexion.html')

# formulaire de création de compte
def registre(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = registreForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('connexion')
        else:
            messages.info(request, "Mots de passe ou Username incorrecte")
    
    form = registreForm()
    context = {
        'form': form
    }         
    return render(request, 'registre.html',context)

# vue de modification de parametre



# déconnexion d'un compte

def deconnexion(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    logout(request)
    return redirect('connexion')


# page de connexion
# 
@match
def index(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    
    membres = Person.objects.all()
    context={
        'membres': membres,
    }
    return render(request, 'pages/index.html', context)
# @new
@only_admin
def other_user(request):
    user = request.user    
    if request.method == "POST":
        numero = request.POST.get('numero')
        date = request.POST.get('date')
        location = request.POST.get('location')
        commune = request.POST.get('commune')
        status = request.POST.get('status')
        genre = request.POST.get('genre')      
        baptism_water = request.POST.get('water')
        baptism_spirit = request.POST.get('spirit')
        community = request.POST.get('community')
        jeunesse = request.POST.get('crue')
        niveau = request.POST.get('level')
        diplomes = request.POST.get('diplomes')
        series = request.POST.get('type')
        filieres = request.POST.get('description')
        domaines = request.POST.get("domaines")
        travail = request.POST.get("travail")
        metier = request.POST.get("metier")
        description = request.POST.get('description')
        cv = request.FILES.get("cv")
        image = request.FILES.get('image')
        
        person = Person(user=request.user,number=numero, birthday=date, living_town=location, commune=commune, status=status, domaines=domaines, genre=genre)
        spirituel = spirit(user=request.user, water_baptem=baptism_water, spirit_baptem=baptism_spirit, young_crue=community, department=jeunesse)
        school = scolaire(user=request.user, school_level=niveau, last_diplom=diplomes, type_bac=series, fields=filieres)
        pro = professionnal(user=request.user, working=travail, jobs=metier, jobs_description=description, cv=cv , image_de_profil=image)
        
        person.save()
        spirituel.save()
        school.save()
        pro.save()
        
        return redirect('update', id=request.user.id - 1)
        
    context ={
        'user': user
    }
    
    return render(request, 'pages/other_user.html', context)
@genre
@only_admin
def update_info(request, id):
        
    info_persons = Person.objects.filter(user=request.user)
    info_spirits = spirit.objects.filter(user=request.user)
    info_scolaires = scolaire.objects.filter(user=request.user)
    info_professionnals = professionnal.objects.filter(user=request.user)
    
    info_person = Person.objects.get(id=id)
    info_spirit = spirit.objects.get(id=id)
    info_scolaire = scolaire.objects.get(id=id)
    info_professionnal = professionnal.objects.get(id=id)
    
    
    if request.method == "POST":
        numero = request.POST.get('numero')
        date = request.POST.get('date')
        location = request.POST.get('location')
        commune = request.POST.get('commune')
        status = request.POST.get('status')
        genre = request.POST.get('genre')      
        baptism_water = request.POST.get('water')
        baptism_spirit = request.POST.get('spirit')
        community = request.POST.get('community')
        jeunesse = request.POST.get('crue')
        niveau = request.POST.get('level')
        diplomes = request.POST.get('diplomes')
        series = request.POST.get('type')
        filieres = request.POST.get('description')
        domaines = request.POST.get("domaines")
        travail = request.POST.get("travail")
        metier = request.POST.get("metier")
        description = request.POST.get('description')
        cv = request.FILES.get("cv")
        image = request.FILES.get('image')
        
        info_person.number = numero
        info_person.birthday = date
        info_person.living_town = location
        info_person.commune = commune
        info_person.status = status
        info_person.domaines = domaines
        info_person.genre =genre
        info_spirit.water_baptem = baptism_water
        info_spirit.spirit_baptem = baptism_spirit
        info_spirit.department = community
        info_spirit.young_crue = jeunesse
        info_scolaire.school_level = niveau
        info_scolaire.last_diplom = diplomes
        info_scolaire.type_bac = series
        info_scolaire.fields = filieres
        info_professionnal.working = travail
        info_professionnal.jobs = metier
        info_professionnal.jobs_description = description
        info_professionnal.cv = cv
        info_professionnal.image_de_profil = image
        
        info_person.save()
        info_professionnal.save()
        info_scolaire.save()
        info_spirit.save()
        
    context = {
        'info_persons': info_persons,
        'info_spirits': info_spirits,
        'info_scolaires': info_scolaires,
        'info_professionnals': info_professionnals,
        'info_person': info_person,
        'info_spirit': info_spirit,
        'info_scolaire': info_scolaire,
        'info_professionnal': info_professionnal
    }
    return render(request, 'pages/update.html',context)
@only_admin
# w
def detail(request):
    user = request.user
    info_persons = Person.objects.filter(user=request.user)
    info_spirits = spirit.objects.filter(user=request.user)
    info_scolaires = scolaire.objects.filter(user=request.user)
    info_professionnals = professionnal.objects.filter(user=request.user)
    context ={
        'info_persons': info_persons,
        'info_spirits': info_spirits,
        'info_scolaires': info_scolaires,
        'info_professionnals': info_professionnals,
        'user': user
    }
    return render(request, 'pages/detail.html',context)

def details(request, user_id):
    if not request.user.is_authenticated:
        return redirect('connexion')
    context = {
        'person': get_object_or_404(Person, pk=user_id),
        'spirit': get_object_or_404(spirit, pk=user_id),
        'scolaire': get_object_or_404(scolaire, pk=user_id),
        'professionnal': get_object_or_404(professionnal, pk=user_id),
    }
    return render(request, 'pages/details.html', context)

# page profil et de modification de mail ou de nom

def profil(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    
    # obj = get_object_or_404(User, pk=pk)
    # if request.method == 'POST':
    #     nom = request.POST.get("Nom")
    #     prenoms = request.POST.get("Prenoms")
    #     description = request.POST.get("Description")
    #     email = request.POST.get("email")
        
    #     obj.last_name = nom
    #     obj.first_name = prenoms
    #     obj.email = email
        
    
    user = request.user
    context = {
        'user': user,
        # 'obj': obj
    }
    
        
    return render(request, 'pages/profil.html', context)



# change le mot de passe
# def change(request):
#     return render(request, 'pages/change.html')

# page graph

def graph(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    hommes = Person.objects.filter(genre="masculin")
    femmes = Person.objects.filter(genre="feminin")
    employer = professionnal.objects.filter(working="oui")
    chomeur = professionnal.objects.filter(working="non")
    number_employer = employer.count()
    number_chomeur = chomeur.count()
    number_hommes = hommes.count()
    number_femmes = femmes.count()
    total = number_hommes + number_femmes
    pour_employer = (number_employer / total )* 100
    pour_chomeur = (number_chomeur / total )* 100 
    pour_hommes = (number_hommes / total )* 100
    pour_femmes = (number_femmes / total )* 100
    context={
        'hommes': hommes,
        'femmes': femmes,
        'Nbrehommes': number_hommes,
        'Nbrefemmes': number_femmes,
        'pour_hommes': pour_hommes,
        'pour_femmes': pour_femmes,
        'total': total,
        'pour_employer': pour_employer,
        'pour_chomeur': pour_chomeur,
        'Nbremployer': number_employer,
        'Nbrechomeur': number_chomeur,
        'employer' : employer,
        'chomeur' : chomeur
    }
    return render(request, 'pages/graph.html', context)


def stat2(request):
    men = Person.objects.filter(genre="masculin")
    women = Person.objects.filter(genre="feminin")
    baptised = spirit.objects.filter(spirit_baptem="oui")
    not_baptised = spirit.objects.filter(spirit_baptem="non")  
    born_again = spirit.objects.filter(water_baptem="oui")
    not_born_again = spirit.objects.filter(water_baptem="non")
    number_baptised = baptised.count()
    number_not_baptised = not_baptised.count()
    number_born_again = born_again.count()
    number_not_born_again = not_born_again.count()
    number_men = men.count()
    number_women = women.count()
    total = number_men + number_women
    pourcent_baptised = (number_baptised / total )* 100
    pourcent_not_baptised = (number_not_baptised / total )* 100
    pourcent_born_again = (number_born_again / total )* 100
    pourcent_not_born_again = (number_not_born_again / total )* 100
    context = {
        'number_men': number_men,
        'number_women': number_women,
        'number_baptised': number_baptised,
        'number_not_baptised': number_not_baptised,
        'number_born_again': number_born_again,
        'number_not_born_again': number_not_born_again,
        'pourcent_baptised': pourcent_baptised,
        'pourcent_not_baptised': pourcent_not_baptised,
        'pourcent_born_again': pourcent_born_again,
        'pourcent_not_born_again': pourcent_not_born_again,
        'total': total
    }
    return render(request, 'pages/stat2.html', context)

def stat3(request):
    men = Person.objects.filter(genre="masculin")
    women = Person.objects.filter(genre="feminin")
    not_diplomed = scolaire.objects.filter(type_bac="Aucun")
    number_men = men.count()
    number_women = women.count()
    total = number_men + number_women
    number_not_diplomed = not_diplomed.count()
    number_diplomed = total - number_not_diplomed
    pourcent_diplomed = (number_not_diplomed / total )* 100
    pourcent_not_diplomed = (number_diplomed / total )* 100
    context = {
        'number_men': number_men,
        'number_women': number_women,
        'number_diplomed': number_diplomed,
        'number_not_diplomed': number_not_diplomed,
        'pourcent_diplomed': pourcent_diplomed,
        'pourcent_not_diplomed': pourcent_not_diplomed,
        'total': total
    }
    return render(request, 'pages/stat3.html', context)

def stat4(request):
    men = Person.objects.filter(genre="masculin")
    women = Person.objects.filter(genre="feminin")
    maried = Person.objects.filter(status="Marié")
    fianced = Person.objects.filter(status="Fiancé")
    widow = Person.objects.filter(status="Veuf")
    celibataire = Person.objects.filter(status="Celibataire")
    number_men = men.count()
    number_women = women.count()
    total = number_men + number_women
    number_maried = maried.count()
    number_celibataire = celibataire.count()
    number_fianced = fianced.count()
    number_widow = widow.count()
    pourcent_maried = (number_maried / total )* 100
    pourcent_celibataire = (number_celibataire / total )* 100
    pourcent_fianced = (number_fianced / total )* 100
    pourcent_widow = (number_widow / total )* 100
    context = {
        'number_men': number_men,
        'number_women': number_women,
        'number_maried': number_maried,
        'number_celibataire': number_celibataire,
        'number_fianced': number_fianced,
        'number_widow': number_widow,
        'pourcent_maried': pourcent_maried,
        'pourcent_celibataire': pourcent_celibataire,
        'pourcent_fianced': pourcent_fianced,
        'pourcent_widow': pourcent_widow,
        'total': total
    }    
    return render(request, 'pages/stat4.html', context)