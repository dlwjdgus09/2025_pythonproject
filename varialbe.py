# x = "안녕"
# print(x)
# print(type(x))
#
# x = 3
# print(x)
# print(type(x))
#
# x = 3 + 5
# print(x)
# print(type(x))
#
# x = 3 == 5
# print(x)
# print(type(x))
#
# x = True
# print(x)
# print(type(x))

# x = [1,2,3,4,5,5,6,"good morning",66,7] #list
# print(x)
# print(type(x))
#
# x = {'a' : 1, 'b' : 5} #dictionary  key : value
# print(x)
# print(x['a'])
# print(type(x))
example = {
    'python': [True, False, True, True, True, True, True, False, False, True],
    'java': [True, False, False, True, True, True, False, False, False, True],
    'git': [False, False, True, True, False, True, True, True, True, True],
}

print(example)
print(example['python'])
print(example['python'][1])

python_description = [
    {
        'answer': 1,
        'description': 'python에 대한 설명은 1번이 맞습니다.'
    },
    {
        'answer': "list",
        'description': 'python의 열거형 데이터 타입은 list입니다.'
    },
    {
        'answer': True,
        'description': 'python의 LIST 안에 Dictionary를 사용할 수 있습니다.'
    },
]

print(python_description[0])

list_example = [1, "+", 2, "="]

print(list_example)
print(list_example[1])

# 변할 수 있는 데이터는 key 값으로 사용 불가
dict_example = {
    1: 'value 1',
    'a': 'value a'
    # x: 'asdf' # 변수는 사용 불가능
    # [1, 2] 리스트도 사용 불가
}

print(dict_example)