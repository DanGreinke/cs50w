from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def article(request, entry):
    entry_markdown = util.get_entry(entry)
    if entry_markdown:
        return render(request, f"encyclopedia/article.html", {
            "entry_html":markdown.markdown(entry_markdown)
        })
    else:
        return HttpResponse("Entry not found :(")


def random_page(request):
    random_entry = util.get_entry(random.choice(util.list_entries()))
    return render(request, f"encyclopedia/article.html", {
        "entry_html":markdown.markdown(random_entry)
    })



def search(request):
    query = request.GET.get('q',"")
    filtered_entries = list()
    all_entries = util.list_entries()

    for i in all_entries:
        if query.lower() == i.lower():
            return render(request, f"encyclopedia/article.html", {
                "entry_html":markdown.markdown(util.get_entry(i))
            })
        elif query in i:
            filtered_entries.append(i)
        else:
            continue

    if filtered_entries:
        return render(request, "encyclopedia/index.html", {
            "entries": filtered_entries
        })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })