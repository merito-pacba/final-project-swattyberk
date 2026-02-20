from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html_content = """
    <html>
        <head>
            <title>Scout Project - Home</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin-top: 100px; background-color: #f4f7f6; }
                .container { background: white; padding: 50px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display: inline-block; }
                h1 { color: #2c3e50; }
                p { color: #7f8c8d; font-size: 1.2em; }
                .btn { display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #3498db; color: white; text-decoration: none; border-radius: 5px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Scout Project!</h1>
                <p>Your Django application is now running perfectly on Azure.</p>
                <a href="/admin/" class="btn">Access Admin Panel</a>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html_content)