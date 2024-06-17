from unit_testing.perhitungan_dasar.penjumlahan import penjumlahan


def test_penjumlahan(constant: int):
    assert penjumlahan(8, constant) == 13
