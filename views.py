from django.shortcuts import render

# Create your views here.
def index(request):
    # Render the homepage
    return render(request, 'index.html')

# Create Submission Backend.
def submission(request):
    # Render the backend (submitted)
    if request.method == "POST":
        # Process form data here
        category = request.POST.get('category')
        priority = request.POST.get('priority')
        feedback = request.POST.get('feedback')
    return render(request, 'submission.html')