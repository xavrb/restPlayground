- [ ] No se validan los datos que entran en el POST de una Movie mas que con min y max del tipo de dato

- [ ] No se puede Registrar un usuario

- [ ] No se pueden Buscar películas por datos específicos como id, titulo, etc

- [ ] No hay tests aunque incluyo un archivo pero esta vacío  es preferible borrarlo si no se van a contemplar los test's

- [ ] No hay un diseño REST todo entra por /api/movie tanto GETS como POSTS lo cual debería ser

    - [ ] api/movie/:id [GET]

    - [ ] api/movie/:id [PUT] <— update

    - [ ] api/movie/:id [DELETE]

    - [ ] api/movie/:id/comments [GET]

    - [ ] api/movie/:id/rating [GET]

    - [ ] api/movie/:id/rating [POST] <- Asignarle a la película una calificación del 1 al 5

    - [ ] api/movie/:id/rating [PUT] <- Asignarle a la película una calificación del 1 al 5 (update)

    - [ ] api/movie/ [POST]

    - [ ] api/movie [GET]  <— get all movies

    - [ ] api/movie/user [POST]

    - [ ] api/movie/user/:id [GET]

    - [ ] api/movie/user/:id [POST]

    - [ ] api/movie/user/:id [PUT]

    - [ ] api/movie/user [GET] <- get all users (only admin role can do it)

- [ ] Se valoraria que estuvieran separadas las urls en lugar de usar ` path('api/` para mejor legibilidad

- [ ] Falto bastante código para contemplar la logica de la parte de comentarios, se hubiera valorado una relación one to many en lugar de tener un atributo comment

- [ ] Una cosa importante es que al no tener código aparte del de `MetaResoure` para servir un endpoint no se pudieron ver los skills al resolver problemas como las validaciones, manejo de auth, los tests
