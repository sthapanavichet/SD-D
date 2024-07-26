numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
colors = {"red", "blue", "green", "yellow", "purple"}
scores = {
    "Alice": 85,
    "Bob": 70,
    "Charlie": 90,
    "David": 75,
    "Eva": 95
}


#Use a list comprehension to create a new list containing the squares of each number in the numbers list
squared_numbers = [number ** 2 for number in numbers]
print(list(squared_numbers))

#Use a dictionary comprehension to create a new dictionary where each student's score is increased by 5
new_scores = {key: values+5 for key, values in scores.items()}
print(dict(new_scores))

#Use a set comprehension to create a new set containing all colors in uppercase
new_colors = {color.upper() for color in colors}
print(new_colors)

#Use a list comprehension to filter out even numbers from the numbers list
even_numbers = [number for number in numbers if number % 2 != 0]
print(list(even_numbers))

#Use a dictionary comprehension to filter out students with scores less than 80 from thescores dictionary
above_80_scores = {key : values for key, values in scores.items() if values >= 80}
print(dict(above_80_scores))