def normalize_whitespace(string):
    s = string.replace('<b>','')
    s = s.replace('</b>','')
    s = s.replace('<span class="summary">','')
    s = s.replace('</span>','')
    return s