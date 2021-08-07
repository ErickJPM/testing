import pytest
import aplicacion as ap

def test_orden():
    assert ap.orden_ascendente([1,5,4,8,6,3,2,7])==[1,2,3,4,5,6,7,8]
    assert ap.orden_ascendente([2,-2,5,4,3])==[-2,2,3,4,5]

def test_personas():
    arregloDiccionarios=[
    {"name":"Juan","edad":50},
    {"name":"Pedro","edad":40},
    {"name":"Maria","edad":30},
    {"name":"Sonia","edad":20},
    {"name":"Silvino","edad":10},
    {"name":"Arturo","edad":10},
    {"name":"Eva","edad":20},
    {"name":"Erick","edad":20},
    {"name":"Antonio","edad":30},
    {"name":"Andrea","edad":40},
    {"name":"Jesus","edad":40}
    ]
    assert ap.personas_mayores(arregloDiccionarios)==9