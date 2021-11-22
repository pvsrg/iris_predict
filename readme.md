# python-flask-docker
Итоговый проект (пример) курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy
API: flask
Данные: dataset iris из sklearn

Задача: предсказать по размерам цветка вид ириса

Используемые признаки:

- sepal_length (float)
- sepal_width (float)
- petal_length  (float)
- petal_width (float)

Модель: KNeighborsClassifier

### Клонируем репозиторий и запускаем контейнер
```
$ git clone https://github.com/pvsrg/iris_predict.git
$ cd iris_predict
$ docker-compose up --build 
```

### Переходим на localhost:5000/form
интерактивная форма, которая после задания размеров цветка выводит вид и фотографию


### API - интерфейс с POST-запросом на localhost:5000/api
передается json c одним или несколькими параметрами цветков.

Примеры

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"sepal_length": ["1","2","3"], "sepal_width":["4","5","6"], "petal_length":["3","4","5"],"petal_width":["4","5","6"]}' \
  http://localhost:5000/api

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"sepal_length": "1", "sepal_width": "4", "petal_length": "3","petal_width":"4"}' \
  http://localhost:5000/api
