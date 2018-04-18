# EnPy
EnPy is made simple to encrypt your file

### Install Requirements
```
pip install -r requirements.txt
```

## Usage
```
python encrypt.py [-f FILE] [-e ENCRYPT] [--chunksize] [--list]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to file
  -e ENCRYPT            Type to encrypt your file (must be supported by your
                        hashlib version)
  --chunksize CS        Chunk size
  --list                List supported hash types
```
 * Encrypt example usage:
```
python encrypt.py -f /path/file -e MD5
```
 * List hashlib:
```
python encrypt.py --list
```
## Listing supported encrypt types:
* MD5
* SHA1
* SHA224
* SHA256
* SHA384
* SHA512

### Screenshot
![sc](https://user-images.githubusercontent.com/35635224/38909842-a5597c3a-42f0-11e8-88c1-0d582b9024db.png)
