import datetime

hoy=datetime.date.today()

# -*- coding: utf-8 -*-
db.define_table('curso',   
   Field('nombre'),
   Field('descripcion','text'))
db.define_table('diagnostico',   
   Field('nombre'),
   Field('descripcion','text'))

db.define_table('alumno',
        Field('nombre'),
        Field('rut'),
        Field('diagnostico', 'list:string'),
        Field('curso', 'reference curso', format='%(nombre)s'),
        Field('fecha_nacimiento', 'date'),
        Field('direccion'),
        Field('telefono'),
        Field('apoderado'),
        Field('telefono_apoderado'),                
        Field('notas', 'text'),
        Field('encargado', 'reference auth_user', format='%(first_name)s' '%(last_name)s'))
#db.alumno.encargado.requires = IS_NULL_OR(IS_IN_DB(db, db.auth_user.id, '%(first_name)s'  ' %(last_name)s'))
db.alumno.diagnostico.requires = IS_NULL_OR(IS_IN_DB(db, db.diagnostico.id, '%(nombre)s', multiple=True))


status=["contestada","no contestada"]
db.define_table('registro',
   Field('descripcion', 'text'),
   Field('alumno_id', 'reference alumno', writable=False,readable=False),
   Field('estado', requires=IS_IN_SET(status)),
   Field('fecha', 'date', default=hoy),
   Field('encargado', 'reference auth_user', format='%(first_name)s' '%(last_name)s',writable=False,readable=False))

db.registro.descripcion.requires = IS_NOT_EMPTY()
#db.registro.encargado.requires = IS_IN_DB(db, db.auth_user.id, '%(first_name)s'  ' %(last_name)s')
