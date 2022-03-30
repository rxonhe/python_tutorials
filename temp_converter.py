# farenheit limits -> 32,212
# celsius limits -> 0, 100
# kelvin limits -> 273, 373

fahrenheit_lim = {"min": 32, "max": 212}
celsius_lim = {"min": 0, "max": 100}
kelvin_lim = {"min": 273, "max": 373}

lim_choser = {
    "fahrenheit": fahrenheit_lim,
    "celsius": celsius_lim,
    "kelvin": kelvin_lim
}


def three_rule(limits_a, limits_b, b0):
    return round((limits_a['max'] - limits_a['min'])\
                 * (b0 - limits_b['min']) /\
                 (limits_b['max'] - limits_b['min']) + limits_a['min'])


def converter(tt_1, to_type):
    from_type = tt_1[0]
    value = tt_1[1]
    return three_rule(lim_choser[to_type], lim_choser[from_type], value)


print(converter(["fahrenheit", 3], "kelvin"))
print(converter(["celsius", 10], "fahrenheit"))
print(converter(["celsius", 20], "kelvin"))