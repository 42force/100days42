courses = ['History', 'Math', 'Physics', 'Chemistry']


nums = [12, 18, 19, 25, 42, 13, 11, 7]


#there is also a sorted version sorted(courses)
nums.sort()
#reverse
courses.reverse()


#sorting

courses.sort()
#list within a list
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)


# for index, course in enumerate(courses, start=1):
#     print(index, courses)

courselist = ['Art', 'Science', 'Physics,', 'Language', 'CompSci']

course_str = ' , '.join(courselist)

new_list = course_str.split(' - ')

#print(course_str)
#print(new_list)


#tuples - similar to list, we cant modify immutable


# list_1 = ['French', 'Russian', 'German', 'Danish', 'Mandarin']
# list_2 = list_1

# print(list_1)
# print(list_2)

#difference with tuple is instead of [] it is ()



tuple_1 = ['French', 'Russian', 'German', 'Danish', 'Mandarin']
tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# sets uses {} - order changes every execution

lang_course = {'French', 'Russian', 'German', 'Danish', 'Mandarin'}


#difference() and union()
print(lang_course)

