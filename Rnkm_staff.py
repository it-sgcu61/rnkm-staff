view_api = "https://drive.google.com/open?id="
magic_api = "https://www.docs.google.com/uc?id="

f = list(map(lambda _: _.strip().split(','), open('./Rnkm_staff.csv')))
l = ['{\n' + ',\n'.join(f'\t"{i}": "{j}"' for i, j in zip(f[0], ln)) + '\n}'  for ln in f[1:]]
s = '{\n' + ',\n'.join([f'"{i[3]}": {j}' for i, j in zip(f[1:], l)]) + '\n}'
print(s.replace(view_api, magic_api), file=open('Rnkm_staff.json', 'w'))

