import mainentry

def test_calc_min_max_temperature():
    # arrange
    input_list = [1,4,10]
    test_list = [1,10]

    result = mainentry.calc_min_max_temperature(input_list)

    assert result == test_list

def test_calc_average():

    #arrange
    input_list=[10,20,30]
    test_list=20

    result =mainentry.calc_average_temperature(input_list)
    assert result == test_list

def test_median_even_temperature():

    #arrange
  

    input_even_list=[10,20,30,40]
    test_even_list=25

    result =mainentry.calc_median_temperature(input_even_list)
    assert result == test_even_list

def test_median_odd_temperature():
    
    input_odd_list=[10,20,30]
    test_odd_list=20

    result =mainentry.calc_median_temperature(input_odd_list)
    assert result == test_odd_list





