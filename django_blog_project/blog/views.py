from django.shortcuts import render
# from django.http import HttpResponse




def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    posts = [
        {
            "title" : "First Post",
            "description" : "This is just a random post.",
            "author" : "IamANi",
            "date" : "17Feb2024"
        },
        {
            "title" : "Second Post",
            "description" : "I don't know what I am writing.",
            "author" : "IamANi",
            "date" : "17Feb2024"
        }
    ]
    context = {"posts" : posts, "title" : "Posts"}
    return render(request, 'blog/posts.html', context)

def about(request):
    # return HttpResponse("<h1>About Page.</h1>")
    return render(request, 'blog/about.html', context={"title" : "About"})
