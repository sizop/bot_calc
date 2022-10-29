import user_interface as ui
# import logger as log
import complex as cn
import rational as rn

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_menu = ui.load_menu_main()
    operations_menu = ui.load_menu_operation()
    select_main_menu = 1
    while select_main_menu != 0:
        ui.print_menu('ГЛАВНОЕ МЕНЮ', main_menu)
        select_main_menu = ui.get_select_menu(main_menu)
        if select_main_menu == 0:
            break

        ui.print_menu('Меню операций', operations_menu)
        select_operation_menu = ui.get_select_menu(operations_menu)
        if select_operation_menu == 0:
            continue

        operator = ''
        if select_operation_menu == 4:
            operator = 'div'
            if select_main_menu != 2:
                operations_menu_div = ui.load_menu_operation_div()
                ui.print_menu('Деление', operations_menu_div)
                select_operation_menu_div = ui.get_select_menu(operations_menu_div)
                operator = operations_menu_div[select_operation_menu_div][1]
        else:
            operator = operations_menu[select_operation_menu][1]

        if select_main_menu == 1:
            data = ui.input_operation_data(operator, 'rational')
            res = rn.calc(operator, data)
        else:
            res = cn.calc(operator, ui.input_operation_data(operator, 'complex'))
        print(f'Результат: {res}')
