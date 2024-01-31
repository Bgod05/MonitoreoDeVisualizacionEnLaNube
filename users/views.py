import firebase_admin
from firebase_admin import credentials, firestore
from django.shortcuts import render

# from django.http import HttpResponse

cred = credentials.Certificate('museoapp-882a5-firebase-adminsdk-32k4t-01c9de6830.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def get_user_data():
    users_ref = db.collection('users')
    docs = users_ref.stream()

    user_data = []
    for doc in docs:
        user_data.append(doc.to_dict())
    return user_data


def show_user_data(request):
    user_data = get_user_data()
    return render(request, 'users.html', {'user_data': user_data})
