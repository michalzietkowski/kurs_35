from flask import Blueprint, render_template, request, flash, redirect, url_for
from ksiegozbior import get_bookstore_state, change_saldo, create_new_book, borrow_book
from file_handler import file_handler

ksiegarnia_blueprint = Blueprint('ksiegarnia', __name__)

@ksiegarnia_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        try:
            match form_type:
                case 'add_book':
                    create_new_book(request.form)
                    flash("Książka została dodana pomyślnie!", "success")
                case 'borrow_book':
                    borrow_book(request.form)
                    flash("Książka została wypożyczona pomyślnie!", "success")
                case 'change_balance':
                    change_saldo(float(request.form.get('saldo')))
                    flash("Saldo zostało zmienione pomyślnie!", "success")
                case _:
                    pass
        except ValueError as e:
            flash(str(e), "error")
        except Exception as e:
            flash(f"Wystąpił błąd: {str(e)}", "error")
        
        return redirect(url_for('ksiegarnia.index'))
    
    stan = get_bookstore_state()
    return render_template('ksiegarnia.html', **stan)

@ksiegarnia_blueprint.route('/historia')
def historia():
    """Displays the history of transactions."""
    stan = get_bookstore_state()
    return render_template('historia.html', historia=stan.get('historia'))