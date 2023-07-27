from django.shortcuts import render
from .models import Student

# Create your views here.


def home(request):
    students = Student.objects.all()
    # students = Student.objects.filter(city="Manchester")
    # students = Student.objects.filter(name="Yogi").delete()
    # students = Student.objects.order_by("tour_place")
    # students = Student.objects.order_by("?")
    # student = Student.objects.filter(name="Virat").first()
    # student = Student.objects.get(id=6)
    
    #student = Student.objects.filter(id=9).update(name="Amit")
    #student = Student.objects.filter(id=10).update(name="Alpesh")
    

    # student = Student.objects.create(name="Yogi", roll=105, marks=99, city="Alhabad", tour_place="pakistan", dream="PM", college="sanatan",ideology="hindu" )
    # student = Student.objects.create(name="Yogi", roll=105, marks=99, city="Alhabad", tour_place="pakistan", dream="PM", college="sanatan",ideology="hindu" )
    #students = Student.objects.all()
    #students = Student.objects.filter(id=12)
    #students = Student.objects.exclude(dream="PM")
    #students = Student.objects.filter(id=14).delete()
    
    #student = Student.objects.create(name="Ansh", roll=115, marks=78, city="Tokyo", tour_place="India", dream="US president", college="IIT Bombay", ideology="Capatalism", occupation="computer science")
    #student = Student.objects.create(name="Oppenheimer", roll=116, marks=89, city="Newyork", tour_place="New Mexico", dream="Nuclear bomb", college="Harvard", ideology="Communist", occupation="Scientist")
    
    #students = Student.objects.all().filter(college="Harvard")
    #students = Student.objects.all()[:5]
    #students = Student.objects.all()[1:16]
    
    #students = Student.objects.order_by("?")
    #students = Student.objects.order_by("city")
    
    #students = Student.objects.all()
    
    #student = Student.objects.create(name="Robert", roll=117, marks=65, city="Andhari", tour_place="Polo forest", dream="Proud son", college="KJIT", ideology="Socialism", occupation="BA In wiser")
    #student = Student.objects.get(id=22)
                
    return render(request, "home.html", {"students": students})
