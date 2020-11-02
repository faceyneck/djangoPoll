# djangoPoll
This is the django poll app from the django documentation tutorial.

I'm putting this together to learn Django and GitHub workflow better.

11.02.2020.14.25 - Most of the project is put together. After running `python manage.py runserver` from the root directory of the project, these are some
notable URLs for using the app:

localhost:8000/polls/
localhost:8000/admin/
localhost:8000/polls/<question:pk>/results/
localhost:8000/ <-- I believe that will throw an error. The app at present requires either /polls/ or /admin/
~~(...and I'm trying to get /polls/<question:pk>/potato/ to work, but alas, that is currently above and beyond the scope of my Django knowledge.) :-(~~
Potato now works! Wonderful help from the #django IRC, in particular mekhami. Thank you for helping me out with /polls/<int:question_id>/potato/
localhost:8000/polls/int:question_id>/potato/
