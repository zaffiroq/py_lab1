from toolkit.errors import (
    BelowAbsoluteZeroValueError,
    InvalidNumberError,
    UncombinedUnitsError,
    UnknownUnitError,
)

length = {'mm' : 0.001, 'cm' : 0.01, 'm' : 1, 'km' : 1000}
mass = {'g' : 0.001, 'kg' : 1}
temperature = {'c' : [1, 0],'f' : [9/5, 32], 'k' : [1, 273.15]}

def convert_length(value, unit_1, unit_2):
    return float(value) * length[unit_1] / length[unit_2]

def convert_mass(value, unit_1, unit_2):
    return float(value) * mass[unit_1] / mass[unit_2]

def convert_temperature(value, unit_1, unit_2):
    celsius = (float(value) - temperature[unit_1][1]) / temperature[unit_1][0]
    if celsius < -273.15:
        raise BelowAbsoluteZeroValueError()
    else:
        return celsius * temperature[unit_2][0] + temperature[unit_2][1]

def convert(value, unit_1, unit_2):

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InvalidNumberError(value)

    unit_1 = str(unit_1).lower()
    unit_2 = str(unit_2).lower()

    if unit_1 in length and unit_2 in length:
        return convert_length(value, unit_1, unit_2)
    if unit_1 in mass and unit_2 in mass:
        return convert_mass(value, unit_1, unit_2)
    if unit_1 in temperature and unit_2 in temperature:
        return convert_temperature(value, unit_1, unit_2)

    if unit_1 in length and (unit_2 in mass or unit_2 in temperature):
        raise UncombinedUnitsError(unit_1,unit_2)
    if unit_1 in mass and (unit_2 in length or unit_2 in temperature):
        raise UncombinedUnitsError(unit_1,unit_2)
    if unit_1 in temperature and (unit_2 in mass or unit_2 in length):
        raise UncombinedUnitsError(unit_1,unit_2)

    if unit_1 not in length and unit_1 not in mass and unit_1 not in temperature:
        raise UnknownUnitError(unit_1)
    if unit_2 not in length and unit_2 not in mass and unit_2 not in temperature:
        raise UnknownUnitError(unit_2)


