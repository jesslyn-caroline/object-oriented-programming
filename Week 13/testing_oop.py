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
    assert mhs.nim == '231111665' # Cause
    # assert mhs.nim == '231111664' # The correct one
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
    assert added == True # Cause 
    # assert added == False # The correct one

def test_lst_3():  # Passed
    lst = Lst()
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    found = lst.searchByNim('231111664')
    assert found == False
    
    added = lst.addMhs(mhs)
    assert added == True
    
    found = lst.searchByNim('231111664') 
    assert found != True 

def test_lst_4(): # Passed
    lst = Lst()
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111665', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111666', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111667', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    dsn = Dsn('231111112', 'Ello', '-', '+12312312312', 'P')
    added = lst.addDsn(dsn)
    
    total = lst.totalMhs()
    assert total == 5

def test_lst_4(): # Passed
    lst = Lst()
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111666', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111667', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111667', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    dsn = Dsn('231111112', 'Ello', '-', '+12312312312', 'P')
    added = lst.addDsn(dsn)
    
    total = lst.totalMhs()
    mhs = lst.mhsLength()
    dsn = lst.dsnLength()

    assert total == 4
    assert mhs == 3
    assert dsn == 1

def test_lst_4(): # Not Passed
    lst = Lst()
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111666', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111667', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111667', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    dsn = Dsn('231111112', 'Ello', '-', '+12312312312', 'P')
    added = lst.addDsn(dsn)
    
    total = lst.totalLength()
    mhs = lst.mhsLength()
    dsn = lst.dsnLength()

    assert total == 6 # Cause
    # assert total == 4 # The correct one
    assert mhs == 5 # Cause
    # assert mhs == 3 # The correct one
    assert dsn == 1

def test_lst_5(): # Passed
    lst = Lst()
    mhs = Mhs('231111664', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111665', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111666', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111667', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    mhs = Mhs('231111667', 'Jess', 'C', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    dsn = Dsn('231111112', 'Ello', '-', '+12312312312', 'P')
    added = lst.addDsn(dsn)

    assert len(lst.searchByNameMhs('Jess')) == 4

def test_lst_5(): # Passed
    lst = Lst()
    mhs = Mhs('231111664', 'Jess', 'B', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    assert added == True

    updated = lst.updateMhs('231111664', 'C')
    assert updated == True

    found = lst.searchByNim('231111664')
    assert found.kelas == 'C'

    removed = lst.removeMhs('231111664')
    assert removed == True

    removed = lst.removeMhs('231111664')
    total = lst.mhsLength()
    assert total == 0

def test_crud(): # Not Passed
    lst = Lst()
    mhs = Mhs('231111664', 'Jess', 'B', 'Sore', '+123123123123', 'P')
    added = lst.addMhs(mhs)
    assert added == True

    updated = lst.updateMhs('231111664', 'C')
    assert updated == True 

    found = lst.searchByNim('231111664')
    assert found.kelas == 'B' # Cause
    # assert found.kelas == 'C' # The correct one

    removed = lst.removeMhs('231111665')
    assert removed == True # Cause
    # assert removed == False # The correct one

    total = lst.mhsLength()
    assert total == 1
