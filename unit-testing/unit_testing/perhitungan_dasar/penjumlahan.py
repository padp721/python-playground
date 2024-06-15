from unit_testing.logging.config import get_logger

log = get_logger()


def penjumlahan(x: int, y: int) -> int:
    log.info('Modul Penjumlahan')
    log.info('%s + %s = %s', x, y, x+y)
    return x + y
