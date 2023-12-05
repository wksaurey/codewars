def growing_plant(up_speed, down_speed, desired_height):
    day_no, plant_height = 0, 0
    while(True):
        day_no += 1
        plant_height += up_speed

        # day
        print(f'After day   {day_no} --> {plant_height}')
        if plant_height >= desired_height:
            return day_no

        plant_height -= down_speed
        #night
        print(f'After night {day_no} --> {plant_height}')
        if plant_height >= desired_height:
            return day_no

growing_plant(100, 10, 910)