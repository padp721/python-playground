from unit_testing.perhitungan_dasar.pengurangan import pengurangan


def test_pengurangan():
    assert pengurangan(10, 5) == 5
    assert pengurangan(5, 10) == -5
