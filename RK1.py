#!/usr/bin/env python
from operator import itemgetter
class emps:
    """Разделы"""
    def __init__(self, id, name, stra, empa_id):
        self.id = id
        self.name = name
        self.stra = stra
        self.empa_id = empa_id
class Dep:
    """Документы"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
class EmpDep:
    """'Разделы документов' для реализации связи многие-ко-многим"""
    def __init__(self, emps_id, empa_id):
        self.emps_id = emps_id
        self.empa_id = empa_id

if __name__ == "__main__":
    Dep = [
    Dep(0, 'Отчет'),
    Dep(1, 'Курсовая'),
    Dep(2, 'Акт'),
    Dep(3, 'Автобиография'),
    Dep(4, 'Договор'),
    Dep(5, 'Реферат'),
    ]
    emps = [
    emps(0, 'Начало', 2, 0),
    emps(1, 'Начало', 2, 1),
    emps(2, 'Введение', 2, 2),
    emps(3, 'Начало', 2, 3),
    emps(4, 'Начало', 2, 4),
    emps(5, 'Начало', 2, 5),
    emps(6, 'Констатирующая часть', 11, 2),
    emps(7, 'История', 9, 3),
    emps(8, 'Выводы', 13, 2),
    emps(9, 'Подписи', 18, 2),
    emps(10, 'Заключение', 50, 5),
    emps(11, 'Ведение', 1, 1),
    ]
    emps_empa = [
    EmpDep(1,1),
    EmpDep(2,2),
    EmpDep(3,3),
    EmpDep(3,4),
    EmpDep(3,5),
    EmpDep(11,1),
    EmpDep(22,2),
    EmpDep(33,3),
    EmpDep(33,4),
    EmpDep(33,5),
    ]

# Соединение данных один-ко-многим
    one_to_many = [(d.name, d.stra, s.name)
        for s in Dep
        for d in emps
        if d.empa_id==s.id]
# Соединение данных многие-ко-многим
    many_to_many_temp = [(s.name, ds.empa_id, ds.emps_id)
        for s in Dep
        for ds in emps_empa
        if s.id==ds.empa_id]

    many_to_many = [(d.name, d.stra, empa_name)
        for empa_name, empa_id, emps_id in many_to_many_temp
        for d in emps if d.id==emps_id]
    print("Задание Г1")
    res_11 = {}
    selected_empa = [one_book[2] for one_book in one_to_many if
    one_book[2].startswith('а') or one_book[2].startswith('А')]
    for empa_name in selected_empa:
        emps_for_book = [(one_emps[0],one_emps[1]) for one_emps in one_to_many if
    one_emps[2]==empa_name]
        res_11.update({empa_name:emps_for_book})
    print(res_11)
    print()

    print("Задание Г2")
    res_12_unsorted = []
    for s in Dep:
        s_emps = list(filter(lambda i: i[2]==s.name, one_to_many))
        if len(s_emps) > 0:
            s_stras = [stra for _,stra,_ in s_emps]
            s_stra_max = max(s_stras)
            res_12_unsorted.append((s.name, s_stra_max))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
    print()

    print("Задание Г3")
    res_13 = {}
    Dep.sort(key=lambda one_empa: one_empa.name)
    for s in Dep:
        s_emps = list(filter(lambda i: i[2]==s.name, many_to_many))
        s_emps_names = [x for x,_,_ in s_emps]
        res_13[s.name] = s_emps_names
    print(res_13)
