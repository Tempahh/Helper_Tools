import random


""" 
This is an implementation of a scheduling app
"""
# Define available time slots
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'sat', 'sun']
time_slots = ['8:00 AM', '9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM']

weeks_in_month = {f"Week {i + 1}" for i in range(4)}

# Define classes with their frequencies and levels
classes = {
    'MATH': {'frequency': 'weekly', 'level': 100},
    'Science_M': {'frequency': 'monthly', 'level': 200},
    'ENGLISH': {'frequency': 'weekly', 'level': 100},
    'History_M': {'frequency': 'monthly', 'level': 300},
    'ART': {'frequency': 'weekly', 'level': 100},
    'Biology': {'frequency': 'weekly', 'level': 200},
    'Physics_M': {'frequency': 'monthly', 'level': 200},
    'Chemistry': {'frequency': 'semesterly', 'level': 200},
    'Literature_M': {'frequency': 'monthly', 'level': 300},
    'Geography': {'frequency': 'weekly', 'level': 300},
    'COMP SCI': {'frequency': 'weekly', 'level': 100},
    'Music_M': {'frequency': 'monthly', 'level': 200},
    'PHY ED': {'frequency': 'semesterly', 'level': 100},
    'Economics_M': {'frequency': 'monthly', 'level': 300},
    'Drama': {'frequency': 'weekly', 'level': 200},
    'Chemical Engineering': {'frequency': 'weekly', 'level': 200},
    'Psychology_M': {'frequency': 'monthly', 'level': 200},
    'Sociology': {'frequency': 'semesterly', 'level': 200},
    'Anthropology_M': {'frequency': 'monthly', 'level': 300},
    'Political Science': {'frequency': 'weekly', 'level': 300},
    'STATS': {'frequency': 'weekly', 'level': 100},
    'Business Administration': {'frequency': 'monthly', 'level': 200},
    'MARKETING': {'frequency': 'weekly', 'level': 100},
    'Finance_M': {'frequency': 'monthly', 'level': 300},
    'Management': {'frequency': 'weekly', 'level': 200},
    'Accounting': {'frequency': 'weekly', 'level': 200},
    'Human Resources_M': {'frequency': 'monthly', 'level': 200},
    'INFORMATION TECHNOLOGY': {'frequency': 'semesterly', 'level': 100},
    'Environmental Science_M': {'frequency': 'monthly', 'level': 300},
    'Civil Engineering': {'frequency': 'weekly', 'level': 300},
    'Electrical Engineering': {'frequency': 'weekly', 'level': 200},
    'Mechanical Engineering_M': {'frequency': 'monthly', 'level': 200},
    'ARCHITECTURE': {'frequency': 'weekly', 'level': 100},
    'Law_M': {'frequency': 'monthly', 'level': 300},
    'Medicine': {'frequency': 'weekly', 'level': 300},
    'Nursing': {'frequency': 'weekly', 'level': 300},
    'Dentistry_M': {'frequency': 'monthly', 'level': 200},
    'Pharmacy': {'frequency': 'semesterly', 'level': 200}
}

level_100_classes = [subject for subject, info in classes.items() if info['level'] == 100]

# Function to generate a random schedule based on certain criterias
def generate_random_schedule():
    schedule = []
    monthly_classes_remaining = [subject for subject, info in classes.items() if info['level'] != 100 and info['frequency'] == 'monthly']
    random.shuffle(monthly_classes_remaining)
    scheduled_subjects = set()

    for week in weeks_in_month:
        week_schedule = []
        for day in days:
            # List of 100-level classes (randomly selected)
            level_100_classes = random.sample([subject for subject, info in classes.items() if info['level'] == 100], k=4)
            
            # List of remaining weekly classes (200-400 level)
            remaining_weekly_classes = [subject for subject in classes.keys() if subject not in level_100_classes]
            random.shuffle(remaining_weekly_classes)
            
            # Calculate available time slots for the day
            day_schedule = []
            used_slots = 0

            # Assign monthly class if needed
            if monthly_classes_remaining and used_slots < len(time_slots):
                monthly_class = monthly_classes_remaining.pop()
                day_schedule.append((time_slots[used_slots], monthly_class))
                used_slots += 1
                scheduled_subjects.add(monthly_class)
            
            # Fill remaining slots with level 100 and other classes
            for class_name in level_100_classes + remaining_weekly_classes:
                if used_slots >= len(time_slots):
                    break
                day_schedule.append((time_slots[used_slots], class_name))
                used_slots += 1

            week_schedule.append((day, day_schedule))
        
        schedule.append((week, week_schedule))
    
    return schedule

# Generate and print the schedule
random_schedule = generate_random_schedule()
for week, week_schedule in sorted(random_schedule):
    print(f"{week}:")
    for day, daily_schedule in sorted(week_schedule):
        print(f"  {day}")
        for time_slot, subject in sorted(daily_schedule):
            print(f"    {time_slot} - {subject}")