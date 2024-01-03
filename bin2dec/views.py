from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        
        if "binary" not in request.POST:
            return render(request, "bin2dec/index.html", {
                "error": "Por favor, insira um número binário válido."
            })
        binary = request.POST["binary"]
        if len(binary) == 0:
            return render(request, "bin2dec/index.html", {
                "error": "Por favor, insira um número binário válido."
            })
        if len(binary) == 0 or binary[0].isdigit() == False or is_binary(binary) == False:
            return render(request, "bin2dec/index.html", {
                "error": "Por favor, insira um número binário válido."
            })
        decimal = 0
        for index, digit in enumerate(reversed(binary)):
            decimal += int(digit) * (2 ** index)
        return render(request, "bin2dec/index.html", {
            "binary": binary,
            "decimal": decimal,
        })
    else:
        return render(request, "bin2dec/index.html")
    
def is_binary(s):
    return all(char in '01' for char in s)