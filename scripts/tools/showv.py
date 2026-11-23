import json,sys
vols={}
for f in ['old-testament','new-testament','book-of-mormon','doctrine-and-covenants','pearl-of-great-price']:
    import pathlib; d=json.load(open(pathlib.Path(__file__).resolve().parents[2]/'.cache'/'src'/(f+'.json')))
    if 'sections' in d: vols['D&C']={s['section']:s for s in d['sections']}
    else:
        for b in d['books']: vols[b['book']]={c['chapter']:c for c in b['chapters']}
for arg in sys.argv[1:]:
    book,_,cv=arg.rpartition(' '); ch,_,vs=cv.partition(':')
    a,_,b=vs.partition('-'); a=int(a); b=int(b or a)
    for v in vols[book][int(ch)]['verses']:
        if a<=v['verse']<=b: print(v['reference'],'|',v['text'][:260])
