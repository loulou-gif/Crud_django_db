from django.shortcuts import render, redirect
from .models import Person, spirit , scolaire, professionnal

# Create your views here.

# vue d'enregistrement du formulaire d'identification
def identification(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        name = request.POST.get('name')
        prenoms = request.POST.get('prenoms')
        email = request.POST.get('email')
        numero = request.POST.get('numero')
        date = request.POST.get('date')
        location = request.POST.get('location')
        commune = request.POST.get('commune')
        status = request.POST.get('status')
        genre = request.POST.get('genre')
        
        
    
        person = Person(name=name, prenoms=prenoms, email=email, numero=numero, date=date, location=location, commune=commune, status=status, genre=genre)
        
        try:
            person.save()
            request.session['person_id'] = person.id
            return redirect('form2')
        except:
            return render(request, 'pages/identification.html')
    else:
    
        return render(request, 'pages/identification.html')

# vue d'enregistrement du formulaire spirituel
def spirituel(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        baptism_water = request.POST.get('water')
        date = request.POST.get('date')
        baptism_spirit = request.POST.get('spirit')
        community = request.POST.get('community')
        jeunesse = request.POST.get('crue')
        
        Id = request.session.get('id')
        print(Id)
        print(baptism_water)
        print(date)
        print(baptism_spirit)
        print(community)
        print(jeunesse)
        person_id = request.session.get('person_id')
        if person_id:
            spirituel = spirit(person_id=person_id, baptism_water=baptism_water,date=date, baptism_spirit=baptism_spirit, community=community, jeunesse=jeunesse)
            try:
                spirituel.save()
                request.session['spirit_id'] = spirituel.id
                return redirect('form3')
            except:
                return render(request, 'pages/spirituel.html')
        else:
        
            return render(request, 'pages/spirituel.html')
        
    return render(request, 'pages/spirituel.html')

# # vue d'enregistrement du formulaire d'education
def education(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        niveau = request.POST.get('level')
        diplomes = request.POST.get('diplomes')
        series = request.POST.get('type')
        filieres = request.POST.get('description')
        
        print(niveau)
        print(diplomes)
        print(series)
        print(filieres)
        spirit_id = request.session.get('spirit_id')
        if spirit_id:
            school = scolaire(person_id=spirit_id, niveau=niveau, diplomes=diplomes, series=series, filieres=filieres)
            try:
                school.save()
                request.session['school_id'] = school.id
                return redirect('form4')
            except:
                return render(request, 'pages/education.html')
        else:
        
            return render(request, 'pages/education.html')
        
    return render(request, 'pages/education.html')

# # vue d'enregistrement du formulaire de profession
def professionel(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        domaines = request.POST.get("domaines")
        travail = request.POST.get("travail")
        metier = request.POST.get("metier")
        description = request.POST.get('description')
        cv = request.FILES.get("cv")
        image = request.FILES.get('image')
        
        
        print(domaines)
        print(travail)
        print(metier)
        print(description)
        print(cv)
        print(image)
        
        school_id = request.session.get('school_id')
        if school_id:
            pro = professionnal(person_id=school_id, domaine=domaines, working=travail, metier=metier, description=description, cv=cv , image_de_profil=image)
            try:
                pro.save()
                return redirect('success')
            except:
                return render(request, 'pages/professionel.html')
        else:
        
            return render(request, 'pages/professionnel.html')
        
    return render(request, 'pages/professionnel.html')

# pages succes
def success(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'pages/success.html')

# page d'erreur 404
def error_404(request):
    return render(request, 'error/404.html')
