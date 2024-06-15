from unit_testing.logging.config import get_logger

log = get_logger()


def pengurangan(x: int, y: int) -> int:
    if x < y:
        log.warning('Nilai x lebih kecil dari nilai y!')
    log.info('Modul Pengurangan')
    log.info('%s - %s = %s', x, y, x-y)
    return x - y
