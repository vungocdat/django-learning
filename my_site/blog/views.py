from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Dat',
        'date': date(2021, 7, 21),
        'title': 'Mountain hiking',
        'excert': 'kjfdlk lfkdjslk wekjw ekljwe',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
    {
        'slug': 'bike-downhill',
        'image': 'bike.jpg',
        'author': 'Ngoc',
        'date': date(2023, 4, 11),
        'title': 'Biking',
        'excert': 'kjfdlk lfkdjslk wekjw ekljwe',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
    {
        'slug': 'deep-ocean',
        'image': 'ocean.jpg',
        'author': 'Vu',
        'date': date(2020, 8, 2),
        'title': 'Deep ocean',
        'excert': 'kjfdlk lfkdjslk wekjw ekljwe',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
]

# Create your views here.


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_post = sorted_post[-3:]
    return render(request, "blog/index.html", {
        'posts': latest_post
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        'post': identified_post
    })
