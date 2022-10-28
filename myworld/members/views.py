from multiprocessing import context
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from django.db.models import Q

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
            'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))
"""
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'firstname': 'Linus',
  }
  
  return HttpResponse(template.render(context, request))    

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
# part 10 Training
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting' : 1,
  }
  return HttpResponse(template.render(context,request))

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers' : mymembers,
  }
  return HttpResponse(template.render(context,request))

# part 11 Training
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting' : 1,
  }
  return HttpResponse(template.render(context,request))

#Part 11 Traning step 10 and step 11 and step 12
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting' : 5,
    'day' : 'Friday',
  }
  return HttpResponse(template.render(context,request))

#Part 11 Traning step 13 and step 14 
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'], 
  }
  return HttpResponse(template.render(context,request))

Part 11 Traning step 15 and step 16 and step 17 and step 18
Work with conditions

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context,request))

# Part 12 Training 
# step 1
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],     
  }
  return HttpResponse(template.render(context, request))

# Part 12 Training
# Step 2
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'cars': [
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
      },
      {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970',
      },
      {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964',
      }]
  }
  return HttpResponse(template.render(context, request))
  
# Part 12 Training 
# Step 3 and Step 4
def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))

# Part 12 Training
# Step 5
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'empytestobject': [],
  }
  return HttpResponse(template.render(context, request))
  
# Part 12 Training
# Step 6
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

# Part 12 Training
# Step 7, 8, 9, 10, 11
def testing(request):
  template = loader.get_template('template.html')
  context = {
      'fruits': ['Apple', 'Banana', 'Cherry', 'Oranges', 'Kiwi'],
  }
  return HttpResponse(template.render(context, request))

#Part 13 Training
# Step 1, 2, 3, 4, 5
def testing(request):
  template = loader.get_template('template.html')
  #context = {
  #  'var1': 'John',
  #}
  return HttpResponse(template.render())

# Part 14 Training
# Step 1, 2, 3, 4
def testing(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'members' : mymembers,
    }
    return HttpResponse(template.render(context, request))

#Part 15 Training
#Step 1
def testing(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())

#Part 15 Trainng
#Step 2
def testing(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'members': mymembers,
    }
    return HttpResponse(template.render(context, request))

#Part 16 Training
#Step 1, 2  
def testing(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())

#Part 17 Training
#Step 1, 2
def testing(request):
    template = loader.get_template('template.html')
    context = {
        'firstname': 'Emil',
    }
    return HttpResponse(template.render(context, request))

#Part 17 Training 
#Step 3, 4
def testing(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())

#Part 18 Training 
#Step 1
def testing(request):
    mydata = Members.objects.all()
    template = loader.get_template('template.html')
    context = {
                'mymembers' : mydata,
            }
    return HttpResponse(template.render(context, request))

# Part 18 Training 
#Step 2
def testing(request):
    mydata = Members.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.   

# Part 18 Training
#Step 3
def testing(request):
    mydata = Members.objects.values_list('firstname')
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.


# Part 18 Training
#Step 4
def testing(request):
    mydata = Members.objects.filter(firstname='Emil').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.


# Part 19 Training
# Step 1
 
def testing(request):
    mydata = Members.objects.filter(firstname='Emil').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.   

# Part 19 Training
# Step 2

def testing(request):
    mydata = Members.objects.filter(lastname='Refsnes', id=2).values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.


# Part 19 Training
# Step 3
# Or
def testing(request):
    mydata = Members.objects.filter(firstname='Emil').values() | Members.objects.filter(firstname='Tobias').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.


# Part 19 Training
# Step 4
# Or use models
def testing(request):
    mydata = Members.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.


# Part 19 Training
# Step 5

def testing(request):
    mydata = Members.objects.filter(firstname__startswith='L').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.


# Part 20 Training 
# Step 1

def testing(request):
    mydata = Members.objects.all().order_by('firstname').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers':mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.


# Part 20 Training
# Step 2

def testing(request):
    mydata = Members.objects.all().order_by('-firstname').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers':mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.


# Part 20 Training
# Step 3

def testing(request):
    mydata = Members.objects.all().order_by('lastname', '-id').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers':mydata,
    }
    return HttpResponse(template.render(context, request))

# Check out template.html to see how the mymembers object
# was used in the HTML code.


# Part 21 Training 
# Step 1.1, 1.2

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
        'heading2': 'Hello <i>my</i> World!',
    }
    print(context)
    return HttpResponse(template.render(context, request))


# Part 21 Training 
# Step 2.1, 2.2

def testing(request):
    template = loader.get_template('childtemplate.html')
    return HttpResponse(template.render())


# Part 21 Training
# Step 3.1, 3.2

def testing(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())


# Part 21 Training
# Step 4.1, 4.2

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry', 'Orange'],
        }
    return HttpResponse(template.render(context, request))


# Part 21 Training
# Step 5.1

def testing(request):
    template = loader.get_template('childtemplate.html')
    return HttpResponse(template.render())


# Part 21 Training 
# Step 6

def testing(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())


# Part 21 Training
# Step 7.1

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'x': 'Volvo',
        'y': 'Ford',
        'z': 'BMW',
    } 
    return HttpResponse(template.render(context, request))

# Part 21 Training
# Step 7.2

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'x': '',
        'y': 'Ford',
        'z': 'BMW',
    } 
    return HttpResponse(template.render(context, request))


# Part 21 Training
# Step 8.1

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
    }
    return HttpResponse(template.render(context, request))

# Part 21 Training
# Step 8.2

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'mycar': {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
        }
    }
    return HttpResponse(template.render(context, request))

# Part 21 Training
# Step 8.3, 8.4

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
    }
    return HttpResponse(template.render(context, request))


# Part 21 Training
# Step 9.1

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'myvar': 1
    }
    return HttpResponse(template.render(context, request))


# Part 21 Training
# Step 8.5, 8.6

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
    }
    return HttpResponse(template.render(context, request))

# Part 21 Training
# Step 8.7

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'cars': ['Ford', 'Volvo', 'BMW'],
        'colors': ['Red', 'Green', 'Blue']
    }
    return HttpResponse(template.render(context, request))
"""

# Part 21 Training
# Step 8.8, 8.9

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
    }
    return HttpResponse(template.render(context, request))

