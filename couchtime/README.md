# restPlayground
![ct-logo](./assets/imgs/branding/ct-logo-banner.png)  


A proof of concept 

| Index |  
|----|  
| [Documentation](#documentation) |  
| [REST framework](#rest-framework) |  
| [Using the api]($using-the-api)|  
| [Database Model](#database-model)|  
| [What is couchtime](#what-is-couch-time)|  
| [What can I do on CT](#what-can-i-do-on-ct) |  
| [To do](#to-do) |  
| [Will I be hired](#will-i-be-hired) |  
| [Taking into account](#taking-into-account)  
| [Licence](#licence)|  

## Documentation  
![docs](../assets/docs.png)  

[Wiki -- Api documentation](https://github.com/xavrb/restPlayground/wiki)  
Quick Overview  

|Method|  
|----|  
|[GET](https://github.com/xavrb/restPlayground/wiki/Show-movie)|  
|[POST](https://github.com/xavrb/restPlayground/wiki/Post-a-movie)|  
  

## REST framework  
![tools](../assets/tools.png)  



We are using [Django Rest Framework](http://www.django-rest-framework.org/)  

## Using the api

The easiest way to use the api is through `curl`. An example is shown as follows:  
```bash 
curl http://localhost:8000/api/movie/

```
Which will return:  
```bash 
{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 9}, "objects": [{"cast": "Chris Pratt, Bryce Dallas Howard, Rafe Spall", "comment": "no comment", "country": "US", "created_at": "2018-06-17T05:20:06.595643", "director": "J.A. Bayona ", "genre": "Action", "id": 1, "rating": 0, "resource_uri": "/api/movie/1/", "title": "Jurassic World", "year": "2018"}, {"cast": "sadjksadasd", "comment": "sldjlasasda", "country": "aspodasdasa", "created_at": "2018-06-19T03:03:08.167285", "director": "kldlsa", "genre": "action", "id": 2, "rating": 2, "resource_uri": "/api/movie/2/", "title": "test", "year": "3838"}, {"cast": "sadjksadasd", "comment": "sldjlasasda", "country": "aspodasdasa", "created_at": "2018-06-19T03:06:21.388922", "director": "kldlsa", "genre": "action", "id": 3, "rating": 2, "resource_uri": "/api/movie/3/", "title": "test", "year": "3838"}, {"cast": "sadjksadasd", "comment": "sldjlasasda", "country": "aspodasdasa", "created_at": "2018-06-19T03:12:15.761063", "director": "kldlsa", "genre": "action", "id": 4, "rating": 2, "resource_uri": "/api/movie/4/", "title": "test", "year": "3838"}, {"cast": "sadjksadasd", "comment": "sldjlasasda", "country": "aspodasdasa", "created_at": "2018-06-19T03:17:52.232553", "director": "kldlsa", "genre": "action", "id": 5, "rating": 2, "resource_uri": "/api/movie/5/", "title": "test", "year": "3838"}, {"cast": "sadjksadasd", "comment": "sldjlasasda", "country": "aspodasdasa", "created_at": "2018-06-19T03:18:18.999236", "director": "kldlsa", "genre": "action", "id": 6, "rating": 2, "resource_uri": "/api/movie/6/", "title": "test", "year": "3838"}, {"cast": "sadjksadasd", "comment": "sldjlasasda", "country": "aspodasdasa", "created_at": "2018-06-19T03:22:32.693211", "director": "kldlsa", "genre": "action", "id": 7, "rating": 2, "resource_uri": "/api/movie/7/", "title": "test", "year": "3838"}, {"cast": "Chris Pratt2, Bryce Dallas 2Howard2, Rafe Spall2", "comment": "no comment2", "country": "US", "created_at": "2018-06-19T03:38:16.983378", "director": "J.A. Bayona 2", "genre": "Action2", "id": 8, "rating": 2, "resource_uri": "/api/movie/8/", "title": "Jurassic World2", "year": "2028"}, {"cast": "Chris Pratt2, Bryce Dallas 2Howard2, Rafe Spall2", "comment": "no comment2", "country": "US", "created_at": "2018-06-19T03:38:18.768205", "director": "J.A. Bayona 2", "genre": "Action2", "id": 9, "rating": 2, "resource_uri": "/api/movie/9/", "title": "Jurassic World2", "year": "2028"}]}
```
You can read more on the [documentation](#documentation). Also you can use your browser and point it to the same address (only for retrieval) or [Postman](https://app.getpostman.com/app/download/linux64) for a nicer looking way to visualize th data.  
  

## Database (model)  
![database](../assets/data.png)  


Using the default SQLITE django model.  

## What is couch Time  
![whatisit](../assets/man-thinking.png)  


We all at some point ever wanted to log every movie we liked -- wether you are a fan of Back to the future or maybe Silence of the lambs, even Twilight (no judgement here), it doesn't matter -- so we can talk to our friends on the next party or just to collect watched movies. Enter Couch Time.  
It’s a simple API and implementation developed in Python Django as a proof of concept  — a technical test, where an user can log their fav movies.  

## What can I do on CT
![whatICANDO](../assets/man-thinking.png)  

You can:  

- [ ] Register with a name and mail.  
- [ ] Save movies (name, genre, cast, director, year, etc) in a imdb-ish way.  
- [ ] Comment on a saved movie.  
- [ ] Rate a movie `1-5`  
- [ ] Delete movies  
- [ ] Search for movies  


Operations are available through a developed API.  



## To do  
![TODO](../assets/to-do.png)  


- [ ] Authentication method  
- [ ] Validations  
- [x] Guidelines and good practices 
- [x] A [git repo](https://github.com/xavrb/restPlayground)  
- [ ] TDD  
- [x] Use of a dbms 


## Will I be hired?  
![hired](../assets/resume.png)  


Yes.  


### Taking into account  

[This](./toTakeIntoAccount.md)


## Licence

This is licensed under GPL3.  



<div>Icons made by <a href="https://www.flaticon.com/authors/zlatko-najdenovski" title="Zlatko Najdenovski">Zlatko Najdenovski</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
