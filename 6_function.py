def std_weight(height, gender): 
    std_weight = round(height /100 * height /100 * 22 if gender == 'men' else 21, 2)
    print('키 {0}cm  남자의 표준 체중은 {1}kg 입니다.'.format(height, std_weight))


std_weight(175, "men")