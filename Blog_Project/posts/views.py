from django.http import HttpResponse
from django.shortcuts import render
posts=[
    {
        "id":1,
        "title":'let\s expl;ore python',
        "content":'pthron is asndjklasnsdjklnasdojnsda'
     },
     {
        "id":2,
        "title":'lts\ expl;ore python',
        "content":'pthron is asndjklasnsdjklnasdojnsda'
     },
]
# Create your views here.
def home(request):
    html =""
    for post in posts:
        html += f'''
            <div>
                <h1>{post['id']} - {post['title']}</h1>
                <p>{post['content']}</p>
            </div>
''' 
    return HttpResponse(html)
