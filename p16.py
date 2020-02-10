students={'1': {'name': 'Bob', 'grade': 2.5},
          '2': {'name': 'Bob', 'grade': 3.5},
          '3': {'name': 'Bob', 'grade': 4.8},
          '4': {'name': 'Bob', 'grade': 2.2},
          '5': {'name': 'Bob', 'grade': 3.5}}
def avgGrade(students):
	sum=0.0
	for key in students:
		sum=sum+students[key]['grade']
	avg=sum/len(students)
	return avg
