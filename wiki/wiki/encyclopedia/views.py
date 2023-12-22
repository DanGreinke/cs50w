from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown


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