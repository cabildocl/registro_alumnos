# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# intente algo como
@auth.requires_login()
def index():
    lista=db(db.diagnostico).select()
    return dict(lista=lista)
def insertar():
    form = SQLFORM(db.diagnostico)
    if form.process().accepted:
       response.flash = 'formulario aceptado'
    return dict(form=form)
@auth.requires_login()
def editar():
    # Crea formulario para editar cursos
    form=SQLFORM(db.diagnostico, request.args(0))
    if form.process().accepted:
       response.flash = 'La informacion se cambio con exito'
    elif form.errors:
       response.flash = 'Existen errores en la informacion'
    return dict(form=form)
