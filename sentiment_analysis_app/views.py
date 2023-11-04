from django.shortcuts import render
from .analysis import analysis as a
from .models import Review
def index(request):
    return render(request, "index.html")


def text_analysis(request):
    if "submit-button" in request.POST:
        user_input = str(request.POST.get("entered"))
        
        #minimum charcter limit BERT
        if len(user_input) < 3:
            return render(request, "text_analysis.html", {"error": "Please enter atleast 3 characters!"})
        
        result = a.calculating(user_input)
        sentence = "The sentiment is "
        return render(request, "text_analysis.html",{"result": result, "sentence": sentence})
    
    return render(request, "text_analysis.html")


def yelp(request):
    if "yelp-submit-button" in request.POST:
        user_input = "jfdhkj568748972398bhjgcdqEFKJDSBVJDJK"
        result = a.yelp(user_input)
        chart, reviews, sentiments = result
        
        if request.POST.get("table-option", "") == "on":
            return render(request, "yelp.html", {"chart": chart, "reviews": reviews, "sentiments": sentiments, "table": " "})
        
        return render(request, "yelp.html", {"chart": chart, "reviews": reviews, "sentiments": sentiments, "no_table": " "})
    
    return render(request, "yelp.html")

def insert(request):
    if request.method == "POST":
        data = request.POST.get("entered")
        print(data)
        review = Review(review=data)
        review.save()
        return render(request, "index.html")
    return render(request, "insert.html")