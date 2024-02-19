morning = {'java', 'c', 'ruby', 'lisp', 'c#'}
afternoon = {'python', 'c#', 'java', 'c', 'ruby'}

# Produces courses not in both sets
possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)

possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)