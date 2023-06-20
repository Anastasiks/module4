# a = input()
# for i in a:
#     if i == a[len(a)-1]:

def strcounter(s):
    for i in set(s):
        counter = 0
        for y in s:
            if i == y:
                counter += 1
        print(i, "-", counter)
strcounter("abbcd")

# Множество (set) - это структкра данных, которая содержит в себе уникальные элементы в неупорядоченом виде

def stronger2(s):
    syms_counter = {}
    for i in s:
        syms_counter[i] = syms_counter.get(i, 0) + 1
    for i, count in syms_counter.items():
        print(i, count)
stronger2("abbs")

            # ДЗ
# a = input("Напишите строку: ")
# c = "".join(reversed(a))
# if a == c:
#     print("True")
# else:
#     print("False")

