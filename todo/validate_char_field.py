def task_validate(name, description, status, deadline):
    errors = {}
    if not name:
        errors['name'] = 'Поле обязательное'
    elif len(name) > 50:
        errors['name'] = 'Максимальная длина 50 символов'

    if not description:
        errors['description'] = 'Поле обязательное'
    elif len(description) > 50:
        errors['description'] = 'Максимальная длина 3000 символов'

    if not status:
        errors['status'] = 'Поле обязательное'

    if not deadline:
        errors['deadline'] = 'Поле обязательное'

    return errors
