def validate_csv(file):
    if not file:
        return False
    if(not file.filename.lower().endswith('.csv')):
        return False
    if(file.mimetype != 'text/csv'):
        return False
    return True