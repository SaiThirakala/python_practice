required_skills = {
    'python',
    'github',
    'linux',
}

candidates = {
    'anna': {'java', 'python', 'linux', 'windows', 'github', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linus', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'linux', 'github', 'python'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'}
}

interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills):
    if skills > set(required_skills):
        interviewees.add(candidate)

print(interviewees)