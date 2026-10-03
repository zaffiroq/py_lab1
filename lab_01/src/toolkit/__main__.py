import argparse
import sys

from toolkit.calculator import calculate
from toolkit.converter import convert
from toolkit.errors import Error

parser = argparse.ArgumentParser(
    prog="toolkit",
    description="Калькулятор с функцией конвертации величин"
)
subparsers = parser.add_subparsers(dest="command", required=True)

calc_parser = subparsers.add_parser("calc", help="Вычисляет арифметическое выражение")
calc_parser.add_argument("expression", help='Выражение, например "2 + 3 * 4"')

convert_parser = subparsers.add_parser("convert", help="Конвертирует из одной величины в другую. Поддерживает метрическую систему длин, массу(кг и г) и температуру (C,F,K)")
convert_parser.add_argument("value", type=float, help="Числовое значение")
convert_parser.add_argument("--from", dest="unit_1", required=True, help="Исходная единица")
convert_parser.add_argument("--to", dest="unit_2", required=True, help="Конечная единица")

def main(argv: list[str] | None = None) -> int:

    args = parser.parse_args(argv)

    try:
        if args.command == "calc":
            result = calculate(args.expression)
        if args.command == "convert":
            result = convert(args.value, args.unit_1, args.unit_2)
    except Error:
        print(f"error: {Error}", file=sys.stderr)
        return 2

    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
