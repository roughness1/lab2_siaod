# lab2_siaod

## Описание

В рамках лабораторной работы реализована система хранения истории браузера.  
Каждая запись содержит:
- URL
- время посещения
- флаг "закладка"

Система поддерживает навигацию по истории, поиск записей, сохранение данных и анализ переходов между сайтами.

---

## Функциональность

### Обязательная часть:
- Навигация назад / вперед
- Очистка истории
- Поиск по домену

### Дополнительно:
- Сохранение истории в файл (в формате Base64)
- Анализ переходов между доменами (топ-N переходов)

---

## Структура проекта
  `BrowserHistoryRecord` - модель данных (одна запись истории)
  `BrowserHistory` - основная логика работы с историей
  Методы ввода/вывода:
  `print_all()` - вывод истории
  `save_to_file()` - сохранение в файл

---

## Выбор структуры данных

Для реализации был выбран динамический массив (`list`), так как он:
  обеспечивает быстрый доступ по индексу (O(1)), что важно для навигации назад и вперёд
  позволяет эффективно хранить последовательность записей
  прост в реализации

Недостатки:
  вставка и удаление в середине имеют сложность O(n), однако в данной задаче это не критично

---

##  Обработка граничных случаев

В программе предусмотрена обработка:
  пустой истории (возврат `None`)
  выхода за границы при навигации
  запроса топ-N при недостаточном количестве данных
  игнорирования переходов внутри одного домена

---

## Пример использования

```python
browser = BrowserHistory()

browser.add_record("https://google.com", "12:00", False)
browser.add_record("https://youtube.com", "12:02", False)
browser.add_record("https://google.com", "12:03", False)
browser.add_record("https://google.com", "12:04", False)
browser.add_record("https://youtube.com", "12:05", False)
browser.add_record("https://google.com", "12:10", False)
browser.add_record("https://github.com", "12:15", False)
browser.add_record("https://youtube.com", "12:20", False)
browser.add_record("https://yandex.ru", "13:00", True)
browser.add_record("https://youtube.com", "14:00", False)

browser.save_to_file("history")
browser.print_all()

print(browser._current_index)
browser.back()
browser.back()
browser.back()
browser.forward()
print(browser._current_index)
print(browser.top_n_transitions(3))
