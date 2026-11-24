
# Take input from user
screen_time = float(input("Daily screen time (hours): "))
social_media = float(input("Social media hours: "))
gaming = float(input("Gaming hours: "))
sleep = float(input("Sleep hours: "))
pickups = float(input("Daily phone pickups: "))
study = float(input("Study/work hours: "))
notifications = float(input("Daily notifications: "))

# Validate input
if not (0 <= screen_time <= 24):
    print("Invalid screen time!")
elif not (0 <= sleep <= 24):
    print("Invalid sleep hours!")
elif social_media < 0 or gaming < 0:
    print("Usage hours cannot be negative!")
elif social_media + gaming > screen_time:
    print("Social media and gaming hours exceed total screen time!")
elif pickups < 0 or notifications < 0 or study < 0:
    print("Values cannot be negative!")
elif study > 24:
    print("Invalid study/work hours!")
else:
    new_person = [[
        screen_time, social_media, gaming,
        sleep, pickups, study, notifications
    ]]

    result = model.predict(new_person)

    print("\nYour Screen Addiction Risk Level:", result[0])

