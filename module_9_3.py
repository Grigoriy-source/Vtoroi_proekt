first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (l1 - l2 for (s1, s2) in zip(first, second)
                if (l1 := len(s1)) != (l2 := len(s2)))

second_result = (len(first[i]) == len(second[i])
                 for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))