"""
Написать тесты(pytest) к предыдущим 3 заданиям, запустив которые, я бы смог бы проверить их корректность
"""

import pytest
import os.path
import os
import task1
import task2
import task3


@pytest.fixture
def task1_resource():
    content = {} 
    curr_dir = os.getcwd()
    name_of_base_dir = os.path.basename(curr_dir)

    for (dirpath, dirnames, filenames) in os.walk(curr_dir):
        name_of_dir = os.path.basename(dirpath)
        content.update({name_of_dir: filenames})

    return name_of_base_dir, content


def test_task1(task1_resource):
    name_of_base_dir, content = task1_resource
    folder_to_check = task1.PrintableFolder(name_of_base_dir, content)
    file_to_check = task1.PrintableFile('task4.py')
    result = 'V tests\n' \
            '|-> task1.py\n' \
            '|-> task2.py\n' \
            '|-> task3.py\n' \
            '|-> task4.py\n' 

    assert str(folder_to_check) == result
    assert file_to_check in folder_to_check


@pytest.fixture
def task2_resource():
    E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
    graph = task2.Graph(E)
    return graph


def test_task2(task2_resource):
    test_res = []
    right_res = ['A', 'B', 'C', 'D']
    for vertice in task2_resource:
        test_res.append(vertice)
    
    assert right_res == test_res


@pytest.fixture
def task3_resource():
    a = task3.CeasarSipher()
    a.message = 'abc'
    a.another_message = 'hello'
    return a


def test_task3(task3_resource):
    obj = task3_resource
    assert obj.message == 'efg'
    assert obj.another_message == 'olssv'