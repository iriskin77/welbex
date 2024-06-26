


## Описание

См. описание здесь: https://faint-adasaurus-4bc.notion.site/web-Python-3682ad009f2a43589f7fdb1d2e0ed312

Использованные технологии:

![](https://img.shields.io/badge/FastApi-coral) ![](https://img.shields.io/badge/PostgreSql-lightblue) ![](https://img.shields.io/badge/TortoiseORM-0.20.0-crimson) ![](https://img.shields.io/badge/Docker-blue) ![](https://img.shields.io/badge/DockerCompose-blue)

## Выполненные задачи

### Уровень 1

Сервис должен поддерживать следующие базовые функции:

+ [x] Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);

+ [x] Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль));

+ [x] Получение информации о конкретном грузе по ID (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза);

+ [x] Получение информации о конкретном грузе по ID (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза);

+ [x] Редактирование груза по ID (вес, описание);

+ [x] Удаление груза по ID.

### Уровень 2

+ [x] Удаление груза по ID.

+ [x] Автоматическое обновление локаций всех машин раз в 3 минуты (локация меняется на другую случайную).

## Как установить и запустить

+ Клонировать репозиторий: git clone https://github.com/iriskin77/welbex.git

+ Запустить приложение из Docker:
  + docker-compose build
  + docker-compose up

### **Важно!!** 
+ После запуска необходимо наполнить БД машинами и локациями.
Для этого нужно сделать два get запроса (upload_cars, upload_uszips):

![](https://github.com/iriskin77/welbex/blob/master/images/handlers.png)

1) **Сначало** наполнить БД локациями из таблицы uszips.csv : http://0.0.0.0:8000/load/load_uszips

```json
    {
      "id": 365,
      "zip": 1746,
      "state": "Massachusetts",
      "latitude": 42.19775,
      "longitude": -71.44499,
      "city": "Holliston",
      "created_at": "2024-03-28T08:53:41.084517Z"
    }
```

2) **Затем** наполнить БД машинами (200 машин будет добавлено): http://0.0.0.0:8000/car/upload_cars

```json
   {
     "id": 1,
     "car_name": "car_name7866",
     "car_location_id": 3186,
     "load_capacity": 479,
     "unique_number": "8743E"
   }
```

После этого можно создавать грузы, тестировать API

Схема БД:

![](https://github.com/iriskin77/welbex/blob/master/images/db_schema.png)
