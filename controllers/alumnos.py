# -*- coding: utf-8 -*-
# intente algo como
@auth.requires_login()
def index():
    if (auth.has_membership(group_id="administrador")):
        diagnostico=db(db.diagnostico).select()
        lista=db(db.alumno).select()
    else:
        diagnostico=db(db.diagnostico).select()
        lista=db(db.alumno.encargado==auth.user.id).select()
    return dict(lista=lista,diagnostico=diagnostico)
@auth.requires_login()
def show():
    alumno = db(db.alumno.id==request.args(0)).select().first()
    registros = db(db.registro.alumno_id==request.args(0)).select(orderby=~db.registro.fecha)
    #
    return dict(alumno=alumno,registros=registros)
@auth.requires_login()
def insertar():
    form = SQLFORM(db.alumno)
    if form.process().accepted:
       response.flash = 'formulario aceptado'
    return dict(form=form)
@auth.requires_login()
def editar():
    # Crea formulario para editar anexos
    form=SQLFORM(db.alumno, request.args(0))
    if form.process().accepted:
       response.flash = 'La informacion se cambio con exito'
       redirect(URL('show/' + str(request.args(0))))    
    elif form.errors:
       response.flash = 'Existen errores en la informacion'
    return dict(form=form)
@auth.requires_login()
def insertar_reporte():
    form = SQLFORM(db.registro)
    form.vars.alumno_id=request.args(0)
    form.vars.encargado=auth.user.id
    if form.process().accepted:
       response.flash = 'formulario aceptado'
       redirect(URL('show/' + str(request.args(0))))
    return dict(form=form)
@auth.requires_login()
def registro():
    if (auth.has_membership(group_id="administrador")):
        lista=db(db.registro).select(join=db.alumno.on(db.alumno.encargado),orderby=~db.registro.fecha)
    else:
        #lista=db(db.registro.alumno_id.encargado==auth.user.id).select(orderby=~db.registro.fecha)
        lista=db(db.registro).select(join=db.alumno.on(db.alumno.encargado==auth.user.id),orderby=~db.registro.fecha)
    return dict(lista=lista)
@auth.requires_login()
def registro1():
    lista=db(db.registro).select(join=db.alumno.on(db.alumno.encargado==auth.user.id))
    return dict(lista=lista)
