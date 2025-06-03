# -*- coding: utf-8 -*-


def check_numbers(cargo_weight_list, number_of_all_cargo, number_of_tracks, maximum_weight):
    """check the numbers that are loadable in tracks
    
    Args:
        cargo_weight_list: cargo weight list
        number_of_tracks: the number of tracks
        
    Returns:
        the number of cargos that are loadable in tracks
    """
    counter = 0
    number_of_loaded_cargo = 0

    while counter < number_of_tracks:
        current_track_weight = 0

        while current_track_weight + cargo_weight_list[number_of_loaded_cargo] <= maximum_weight:
            current_track_weight += cargo_weight_list[number_of_loaded_cargo]
            number_of_loaded_cargo += 1
            if number_of_loaded_cargo == number_of_all_cargo:
                return number_of_all_cargo

        counter += 1

    return number_of_loaded_cargo


def find_the_minimum_of_maximum_weihgt(cargo_weight_list, number_of_all_cargo, number_of_tracks):
    """find the minimum of maximum weight s.t all of the cargos can be loaded into tracks.
    (binary search is used. the number of loadable cargos monotonicaly increases as the maximum weight increases)


    Args:
        cargo_weight_list: cargo weight list
        numbef of all cargo: the number of all cargos
        number of tracks: the number of tracks

    Returns:
        minumim number of maximum track weight that are needed to load all of the cargos
    """
    left = max(cargo_weight_list)
    right = sum(cargo_weight_list)
    while (right - left) > 0:
        middle = (right + left) / 2
        the_number_of_loadable_cagos = check_numbers(cargo_weight_list, number_of_all_cargo, number_of_tracks, middle)
        if the_number_of_loadable_cagos >= number_of_all_cargo:
            right = middle
        else:
            left = middle + 1

    return right

def main():
    number_of_all_cargo, number_of_tracks = [int(x) for x in raw_input().split(' ')]
    cargo_weight_list = [int(raw_input()) for _ in xrange(number_of_all_cargo)]
    
    print find_the_minimum_of_maximum_weihgt(cargo_weight_list, number_of_all_cargo, number_of_tracks)


if __name__ == '__main__':
    main()