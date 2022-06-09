<h1>Guess the color</h1><br>
<li>
  <strong>Initialize Docker</strong><br><br>
  <ul><em>Make sure that Docker is installed on your machine, and you are in the directory where docker-compose.yml is.</em></ul>
<pre>$ docker-compose up --build</pre>
  <ul><em>After Docker finishes the build, it will deploy the application on port 8000, if you haven't changed them in docker files configuration.</em></ul>
</li><br>


<h2>Interactive API docs</h2><br>
<li><strong>Go to</strong> <a href="http://localhost:8000/docs" rel="nofollow">localhost:8000/docs</a></li><br>
<ul><em>You will see the automatic interactive API documentation.</em></ul><br>


<h2>Available API's </h2><br>
<li>Создадим 100 рандомных предметов, для того чтобы в дальнейшем попытаться угадать их ---> <a href="http://localhost:8000/docs#/%D0%A1reate%20random%20items/post_fillingdb_post"><strong>[POST]</strong> /fillingdb</a></li>
<li>Попытаемся угадать по номеру предмета его цвет ---> <a href="http://localhost:8000/docs#/Trying%20to%20guess/get_try_get"><strong>[GET]</strong> /try</a></li>
<li>Перемешаем предметы, либо очистим базу данных ---> <a href="http://localhost:8000/docs#/Clear/delete_delete_all__delete"><strong>[DELETE]</strong> /delete_all</a></li>
