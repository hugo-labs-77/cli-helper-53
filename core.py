import sys
import json

class InputError(Exception):
    pass

class NegativeNumberError(InputError):
    def __init__(self, value):
        self.value = value
        super().__init__(f'Negative number error: {value}')

class DivisionByZeroError(InputError):
    def __init__(self):
        super().__init__('Division by zero error')

def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InputError('Both inputs must be numbers.')
    if b == 0:
        raise DivisionByZeroError()
    return a / b

def process_input(data):
    try:
        a = float(data.get('a'))
        b = float(data.get('b'))
        if a < 0 or b < 0:
            raise NegativeNumberError(a if a < 0 else b)
        result = safe_divide(a, b)
        return json.dumps({'result': result})
    except InputError as e:
        return json.dumps({'error': str(e)})
    except Exception as e:
        return json.dumps({'error': 'An unexpected error occurred.'})

if __name__ == '__main__':
    input_data = json.loads(sys.stdin.read())
    print(process_input(input_data))
