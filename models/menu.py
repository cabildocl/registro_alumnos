# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------
response.title = "Registro Alumnos"

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]
response.menu+= [ [ 'Alumnos', False, None,[( 'Listado', False ,URL('alumnos','index')),( 'Agregar', False ,URL('alumnos','insertar'))] ],[ 'Registros', False, URL('alumnos','registro') ]]
response.menu+= [ [ 'Cursos', False, None,[( 'Listado', False ,URL('cursos','index')),( 'Agregar', False ,URL('cursos','insertar'))] ]]
response.menu+= [ [ 'Diagnostico', False, None,[( 'Listado', False ,URL('diagnosticos','index')),( 'Agregar', False ,URL('diagnosticos','insertar'))] ]]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------
