<<<<<<< HEAD
def handel_uploaded_file(f):
    with open('API/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
=======
def handel_uploaded_file(f):
    with open('API/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
>>>>>>> fd9dbff22677b5c80eefd39d985aef4ffc2683f5
