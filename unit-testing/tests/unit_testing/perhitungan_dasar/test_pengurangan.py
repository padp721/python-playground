from unit_testing.perhitungan_dasar.pengurangan import pengurangan


def test_pengurangan(constant: int):
    assert pengurangan(10, constant) == 5
    assert pengurangan(constant, 10) == -5
