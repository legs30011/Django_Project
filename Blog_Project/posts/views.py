from django.http import HttpResponse, HttpResponseNotFound
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
            <a href="/post/{post['id']}/">
                <h1>{post['id']} - {post['title']}</h1></a>
                <p>{post['content']}</p>
            </div>
''' 
    return HttpResponse(html)

def post(request,id):
    valid_id=False
    for post in posts:
        if post['id']== id:
            post_dict= post
            valid_id=True
            break
    if valid_id:
        html  = f'''
            <h1>{post_dict['title']}</h1>
            <p>{post_dict['content']}</p>
        '''
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("Post Not Available")
    
