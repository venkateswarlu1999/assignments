# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import *

# @csrf_exempt
# def createauthor(reqest):
#     requestedbodytodict=json.loads(reqest.body)
#     namefrompostman=requestedbodytodict["name"]
#     savingtodb=author(name=namefrompostman)
#     savingtodb.save()
#     return JsonResponse({
#         "massage":f"{namefrompostman} added to author table successfully"
#     })
  
# @csrf_exempt  
# def createlibrary(request):
#     # authid=(json.loads(request.body))['authid']
#     # authname=author.objects.get(id=authid).name
    
#     # booksSet=lbbooks.objects.filter(author_id=authid)
#     # bookslist=[]
#     # for book in booksSet:
#     #     bookslist.append(book)
#     #     newbook=lbbooks.objects.create(tittle=book,author_id=authid)
#     authId = (json.loads(request.body))['author_id']

#     authorName = author.objects.get(id = authId).name

#     booksQuerySet = lbbooks.objects.filter(author_id=authId)

#     bookLists = []

#     for  book in booksQuerySet:
#         bookLists.append(book.title)
#         newBook = lbbooks.objects.create(title = book, author_id = authId)

#     return JsonResponse({
#         "message": f"{bookLists} of {authorName} retrieved successfully"
#     })

# def getBooknamesFromAuthor(request):
#     authId = (json.loads(request.body))['author_id']

#     authorName = author.objects.get(id = authId).name

#     booksQuerySet = lbbooks.objects.filter(author_id = authId)

#     bookLists = []

#     for  book in booksQuerySet:
#         bookLists.append(book.title)
#         newBook = lbbooks.objects.create(title = book, author_id = authId)

#     return JsonResponse({
#         "message": f"{bookLists} of {authorName} retrieved successfully"
#     })




from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

@csrf_exempt
def createauthor(request):
    try:
        requested_body = json.loads(request.body)
        name_from_postman = requested_body["name"]
        saving_to_db = author(name=name_from_postman)
        saving_to_db.save()
        return JsonResponse({
            "message": f"{name_from_postman} added to author table successfully"
        })
    except json.JSONDecodeError:
        return JsonResponse({
            "error": "Invalid JSON data in the request body"
        }, status=400)
    except KeyError as BadRequest:
        return JsonResponse({
            "error": f"Missing required field: {BadRequest}"
        }, status=400)
    except Exception as ServerErrors:
        return JsonResponse({
            "error": f"An error occurred: {ServerErrors}"
        }, status=500)
    finally:
            # return JsonResponse({
            #     "message": "thankyou for visiting library"
            # })
        pass
@csrf_exempt
def createlibrary(request):
    try:
        request_data = json.loads(request.body)
        auth_id = request_data.get("author_id")

        if auth_id is None:
            return JsonResponse({
                "error": "Missing 'author_id' in the request body"
            }, status=400)

        try:
            author_instance = author.objects.get(id=auth_id)
            author_name = author_instance.name

            books_query_set = lbbooks.objects.filter(author_id=auth_id)

            book_list = []
            for book in books_query_set:
                book_list.append(book.title)
                new_book = lbbooks.objects.create(title=book.title, author_id=auth_id)

            return JsonResponse({
                "message": f"{book_list} of {author_name} retrieved successfully"
            })

        except author.DoesNotExist:
            return JsonResponse({
                "error": "Author with the specified 'author_id' does not exist"
            }, status=404)

    except json.JSONDecodeError:
        return JsonResponse({
            "error": "Invalid JSON data in the request body"
        }, status=400)
    except KeyError as BadRequest:
        return JsonResponse({
            "error": f"Missing required field: {BadRequest}"
        }, status=400)
    except Exception as ServerErrors:
        return JsonResponse({
            "error": f"An error occurred: {ServerErrors}"
        }, status=500)
    finally:
      
            # return JsonResponse({
            #     "message": "thankyou for visiting library"
            # })
            pass

@csrf_exempt
def getBooknamesFromAuthor(request):
    try:
        auth_id = (json.loads(request.body))['author_id']
        author_name = author.objects.get(id=auth_id).name
        books_query_set = lbbooks.objects.filter(author_id=auth_id)
        book_list = []

        for book in books_query_set:
            book_list.append(book.title)
            new_book = lbbooks.objects.create(title=book.title, author_id=auth_id)

        return JsonResponse({
            "message": f"{book_list} of {author_name} retrieved successfully"
        })
    except json.JSONDecodeError:
        return JsonResponse({
            "error": "Invalid JSON data in the request body"
        }, status=400)
    except KeyError as BadRequest:
        return JsonResponse({
            "error": f"Missing required field: {BadRequest}"
        }, status=400)
    except Exception as ServerErrors:
        return JsonResponse({
            "error": f"An error occurred: {ServerErrors}"
        }, status=500)
    finally:
        # return JsonResponse({
        #     "message": "Thank you for visiting the library"
        # })
        pass
