import git
from django.http import HttpResponse


def iam_index(request):
    return HttpResponse("Iam Index View")


def git_update(request):
    if request.method == "POST":
        repo = git.Repo("wanjohi.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")

