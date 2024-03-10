from django.shortcuts import render

from calculator import km_to_miles,calculate
from .forms import ArithmeticOperationForm, ConversionForm


def index(request):
    # Змінні для форми конвертації
    conversion_form = ConversionForm()

    # Змінні для арифметичної форми
    arithmetic_operation_form = ArithmeticOperationForm()

    result_dict = dict()

    if request.method == 'POST':
        arithmetic_operation_form = ArithmeticOperationForm(request.POST)
        conversion_form = ConversionForm(request.POST)
        if arithmetic_operation_form.is_valid():
            number1 = arithmetic_operation_form.cleaned_data['number1']
            number2 = arithmetic_operation_form.cleaned_data['number2']
            operation = request.POST['operation']

            arithmetic_operation_result, arithmetic_operation_error = calculate(number1, number2, operation)
            result_dict.update({'arithmetic_operation_result': arithmetic_operation_result,
                  'arithmetic_operation_error': arithmetic_operation_error,
                  'number1': number1,
                  'number2': number2,
                  'operation':operation})
        if conversion_form.is_valid():
            kilometers = conversion_form.cleaned_data['kilometers']
            conversion_result, conversion_error =  km_to_miles(kilometers)
            result_dict.update({'conversion_result':conversion_result,
                          'conversion_error':conversion_error,
                          'kilometers':kilometers})

    return render(request, 'main/index.html', result_dict)
