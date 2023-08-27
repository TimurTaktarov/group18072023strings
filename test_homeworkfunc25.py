from homeworkfunc25 import car_description


def test_car_description():
    expected = 'A vehicle weighing 1000 kg moved for 10 seconds at a speed of 3 m/s and covered a distance of 30 meters'
    actual = car_description(time=10, speed=3, weight=1000)
    assert actual == expected
