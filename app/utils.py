import csv
import io

def validate_csv(file):
    if not file:
        return False
    
    stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    try:
        csv.reader(stream)
    except:
        return False
    return True