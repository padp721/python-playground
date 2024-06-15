import argparse
import logging

from unit_testing.logging.config import get_logger, setup_logging
from unit_testing.perhitungan_dasar.pengurangan import pengurangan
from unit_testing.perhitungan_dasar.penjumlahan import penjumlahan


def main():
    log = get_logger()
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--debug',
        help='Tampilkan log saat aplikasi berjalan (menjadikan level logging ke DEBUG)',
        action=argparse.BooleanOptionalAction
    )
    parser.add_argument(
        '--log-file',
        help='Buat file log. Diisi dengan lokasi file log',
        type=str,
        default=''
    )
    parser.add_argument(
        '--tipe',
        '-T',
        help='Tipe perhitungan dasar yang akan dilakukan. Contoh: "penjumlahan", "pengurangan"',
        type=str
    )
    parser.add_argument(
        '--angka-pertama',
        '-X',
        help='Angka pertama',
        type=int,
        default=0
    )
    parser.add_argument(
        '--angka-kedua',
        '-Y',
        help='Angka kedua',
        type=int,
        default=0
    )

    args = parser.parse_args()
    if args.debug:
        setup_logging(
            logger_level=logging.DEBUG,
            logger_file=args.log_file
        )

    if args.tipe == 'penjumlahan':
        hasil = penjumlahan(
            args.angka_pertama,
            args.angka_kedua
        )
        print(f'Hasil Perhitungan : {hasil}')
    elif args.tipe == 'pengurangan':
        hasil = pengurangan(
            args.angka_pertama,
            args.angka_kedua
        )
        print(f'Hasil Perhitungan : {hasil}')
    else:
        log.warning('Harap untuk mengisi tipe perhitungan dengan benar!')


if __name__ == '__main__':
    main()
