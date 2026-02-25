from collections import deque

def stable_matching(students_prefs, hospitals_prefs, capacities):
    free_students = deque(students_prefs.keys())
    hospital_matches = {h: [] for h in hospitals_prefs}
    
    hospital_rank = {}
    for h, prefs in hospitals_prefs.items():
        hospital_rank[h] = {student: rank for rank, student in enumerate(prefs)}

    # Индекс следующей больницы, которой студент сделает предложение
    next_proposal_index = {s: 0 for s in students_prefs}
    

    while free_students:
        
        student = free_students.popleft()
        print(student)
        # Если студент предложил всем больницам — пропускаем
        if next_proposal_index[student] >= len(students_prefs[student]):
            continue

        hospital = students_prefs[student][next_proposal_index[student]]
        next_proposal_index[student] += 1

        hospital_matches[hospital].append(student)

        # Если превышена вместимость — удалить худшего
        if len(hospital_matches[hospital]) > capacities[hospital]:
            # Сортируем по предпочтению больницы
            hospital_matches[hospital].sort(
                key=lambda s: hospital_rank[hospital][s]
            )

            # Худший — последний
            worst_student = hospital_matches[hospital].pop()

            if worst_student != student:
                free_students.append(worst_student)
            else:
                free_students.append(student)

    return hospital_matches


students_prefs = {
    "S1": ["H1", "H2"],
    "S2": ["H1", "H2"],
    "S3": ["H2", "H1"],
    "S4": ["H2"]
}

hospitals_prefs = {
    "H1": ["S2", "S1", "S3", "S4"],
    "H2": ["S3", "S1", "S2", "S4"]
}

capacities = {
    "H1": 1,
    "H2": 2
}

result = stable_matching(students_prefs, hospitals_prefs, capacities)

print("Устойчивое распределение:")
for h, students in result.items():
    print(h, ":", students)
