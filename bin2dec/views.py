from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print('fui chamado')
    if request.method == "POST":
        print("chamado dentro do post")
        binary = request.POST["binary"]
        decimal = 0
        for index, digit in enumerate(reversed(binary)):
            decimal += int(digit) * (2 ** index)
        print(decimal)
        return render(request, "bin2dec/index.html", {
            "binary": binary,
            "decimal": decimal,
        })
    else:
        return render(request, "bin2dec/index.html")