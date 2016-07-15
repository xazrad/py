## Решения тестовых задач.

Решения реализованы на языке `python 2.7`.

Используемые зависимости:

* flake8

* pytest

flake8 используется для проверки соответствия кода стандартам PEP8.

pytest для реализации автотестов.

Команда для записка тестов:

``` python
py.test pytests
```

###  Задание 1. 

Решения задания 1 представлено в скрипте `task_1.py`.

Данный скрипт можно запускать с параметром, где указываем строку, необходимую для парсинга.

``` python
python task_1.py esdfd((esdf)(esdf
```


### Задание 2. Django ORM

## 2.a

``` python
Category.objects.filter(product__price__gte=100).annotate(Count('product'))

```


## 2.b

``` python
Category.objects.filter(product__price__gte=100).annotate(count_c=Count('product')).filter(count_c__gt=10)

```

## 2.c

``` python
Product.objects.values_list('category__name', 'name', 'price')

```


### Задание 3. Additional questions

## 3.a

``` python
iv. Abstract base classes

```

## 3.b

``` python
class CustomQuerySet(QuerySet):
    def delete(self):
        self.update(active=False)

    def delete_real(self):
        super(CustomQuerySet, self).delete()

```

## 3.c

``` python
birthday = models.DateField(null=True, blank=False)

```


### Задание 4. Проектирование

Структура хранения представлена в рисунке.
  
Каждый пользователь имеет "личный" дисконт. Храним этот дисконт в таблице  `User` в поле `percent_discont`.

Товары представлены в таблице `Goods`. Каждый товар имеет цену `Price`. А также ссылки на `Brand`, `Group`.

Логика работы системы скидок представлена в табл `Discont`. 
 
Каждая "акция" представляет собой запись в данной таблице.

Акция имеет срок действия `date_in` и `date_out`. Процент скидки `Percent_discont`. Тип скидки, представляющий 
выбор из значений: "На бренд", "На группу" или "На контректный товар".

Поле `Value` хранит значение идентификатора значения, исходя из выбора предыдущиего значения - Тип ссылки.
(Если это скидка "на бренд", то идентификатор бренда)


![ Решение ](data/discont.png)

django-приложения, решающие подобную задачу не встречал. Но посмотрел бы решения или плагины для django-shop или
 django-oscar, как они решают текущую проблему, и подогнал под текущие нужды. 

### Задание 5. SQL

Вариант 1:

``` sql
SELECT 
    phones.phone,
    count(items.id) 
FROM phones
LEFT OUTER JOIN 
items
ON items.user_id = ANY(phones.users)
AND items.status = 7 AND phones.phone IN ('9656261100', '9991570101', '9991570102')
GROUP BY phones.phone;

```


Вариант 2:

``` sql
SELECT 
    phones.phone, 
    sum(case when items.status = 7 then 1 else 0 end) as saled,
    sum(case when items.status = 3 then 1 else 0 end) as not_saled
FROM phones
LEFT OUTER JOIN 
items
ON items.user_id = ANY(phones.users)
GROUP BY phones.phone;

```

###  Задание 6. GIT.
 
``` bash
$ git init
$ echo first_commit_master > README.md
$ git add .
$ git commit -m 'FIRST'

```

``` bash
$ git branch feature_1
$ git checkout feature_1

```

**OR**

``` bash
$ git branch -b feature_1

```

``` bash
$ echo commit_feature_1_first >> README.md
$ git commit -a -m 'commit_feature_1_first'
$ echo commit_feature_1_second >> README.md
$ git commit -a -m 'commit_feature_1_second'

$ git log
commit 141bc206db3bd7f9b2c0ff7ae03d6ad9a8d68359
Author: xazrad 
Date:   Mon Jul 11 20:58:09 2016 +0300

    commit_feature_1_second

commit 33ee43abc4af94a49b54c4d6740abf7cb25f420e
Author: xazrad 
Date:   Mon Jul 11 20:42:40 2016 +0300

    commit_feature_1_first

commit 5132debb1e846e40201d0f093edeef2288338766
Author: xazrad 
Date:   Mon Jul 11 20:40:23 2016 +0300

    FIRST

$ git reset --hard 33ee43abc4af94a49b54c4d6740abf7cb25f420e
$ git checkout master
$ git merge feature_1

```