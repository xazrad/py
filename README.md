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


### Задание SQL

Вариант 1:

``` sql
SELECT 
    phones.phone, 
    "sum"(q.count) 
FROM phones
LEFT OUTER JOIN 
(SELECT 
    user_id, 
    "count"("id") AS count 
 FROM items WHERE status = 7  GROUP BY user_id
) AS q 
ON q.user_id = ANY(phones.users)
GROUP BY phones.phone;

```


Вариант 2:

``` sql
SELECT 
    phones.phone, 
    "sum"(q.saled) as saled, 
    "sum"(q.not_saled) as not_saled 
FROM phones
LEFT OUTER JOIN 
(SELECT 
	user_id, 
	sum(case when status = 7 then 1 else 0 end) as saled,
	sum(case when status = 3 then 1 else 0 end) as not_saled
	FROM items GROUP BY user_id
) AS q 
ON q.user_id = ANY(phones.users)
GROUP BY phones.phone;

```

###  Задание GIT.
 
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