import os
import datetime
import hashlib
 
def chunk_reader(fobj, chunk_size=2048):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk


def get_hash(_file, chunk_size=2048, hash=hashlib.sha512):
    hashobj = hash()
    with open(_file, 'rb') as file_object:
        hashobj.update(file_object.read(chunk_size))
        ##for chunk in chunk_reader(file_object, chunk_size=chunk_size):
        ##    hashobj.update(chunk)
    _hash = hashobj.digest()
    return _hash


def get_ctime(_file):
    return os.path.getctime(_file)


def get_size(_file):
    return os.path.getsize(_file)


def collect_files(path, delete=False):
    unique = {}
    for root, dirs, files in os.walk(path):
        for _file in files:

            file_path = os.path.join(root, _file)

            if os.path.isfile(file_path):
                _sz = get_size(file_path)
                _ct = get_ctime(file_path)
                _hd = get_hash(file_path)
                key = '%s_%s' % (_hd, _sz)
                if key not in unique:
                    unique[key] = file_path
                    yield 'Unique,"%s","%s",%s,"%s"\n' % (_file, datetime.datetime.fromtimestamp(_ct), _sz, root)
                else:
                    if delete:
                        os.remove(file_path)
                    yield 'Removed,"%s","%s",%s,"%s"\n' % (_file, datetime.datetime.fromtimestamp(_ct), _sz, root)


if __name__ == '__main__':

    # ===================================
    # Config
    # ===================================
    '''
    Examples:
        dir = r'C:\Music'
        dir = 'C:/Music'
        dir = '/Music'
    '''

    dir = r'C:\Users\sss\Desktop\pics'  # Set the path to the folder you wish to check.

    do_deletes = False  # False will let you review the log before committing to removal.

    log_name = 'dupe_kill'

    # ====================================
    # No changes needed below this line.
    # ====================================
    log_file = '%s_%s.csv' % (log_name, datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))

    with open(log_file, 'w') as log:
        log.write('Stat,File,Created,Size,Path\n')
        for dupe in collect_files(dir, delete=do_deletes):
            log.write(dupe)