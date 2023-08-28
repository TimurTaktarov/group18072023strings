def car_description(*, time: int | float, speed: int | float, weight: int | float, distance: int | float) -> str:
    if time < 0:
        raise ValueError('Values must be absolute')
    elif speed < 0:
        raise ValueError('Values must be absolute')
    elif weight < 0:
        raise ValueError('Values must be absolute')
    elif distance < 0:
        raise ValueError('Values must be absolute')

    result = f"A vehicle weighing {weight} kg moved for {time} seconds at a speed of {speed} m/s and covered a distance of {distance} meters"
    return result
