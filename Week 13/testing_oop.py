import pytest
from Task_1 import Dsn, Mhs, Lst

def test_mhs_1():  # Passed
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    assert mhs.nim == '231111664'
    assert mhs.nama == 'Jess'
    assert mhs.kelas == 'C'
    assert mhs.jam == 'Sore'
    assert mhs.nomorHp == '+123123123123'
    assert mhs.jenisKelamin == 'P'
    
def test_mhs_2():  # Not passed
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    assert mhs.nim == '231111665' 
    assert mhs.nama == 'Jess'
    assert mhs.kelas == 'C'
    assert mhs.jam == 'Sore'
    assert mhs.nomorHp == '+123123123123'
    assert mhs.jenisKelamin == 'P'

def test_dsn_1(): # Passed
    dsn = Dsn('231111112', 'Ello', '-', '+12312312312', 'P')
    assert dsn.nip == '231111112'
    assert dsn.nama == 'Ello'
    assert dsn.jabatan == '-'
    assert dsn.nomorHp == '+12312312312'
    assert dsn.jenisKelamin == 'P'

def test_lst_1():  # Passed
    lst = Lst()
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    assert added == True
    
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    assert added == False
    
def test_lst_2():  # Not passed
    lst = Lst()
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    assert added == True
    
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    assert added == True  

def test_lst_3():  # Passed
    lst = Lst()
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    found = lst.searchByNim('231111664')
    assert found == False
    
    added = lst.addMhs(mhs)
    assert added == True
    
    found = lst.searchByNim('231111664') 
    assert found == True
