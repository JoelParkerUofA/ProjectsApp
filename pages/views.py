from django.shortcuts import render

# Create your views here. We define the function that will render the html page. 
# each veiw handles the logic the server processes each time the user visits a 
# different url. 
def home(request):
    return(render(request, "pages/home.html",{}))