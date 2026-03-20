import csv

game_list = [
    {
        'name': 'Grand Theft Auto IV',
        'gender': 'Action',
        'developer':'Rockstar',
        'ESRB Clasification': 'M',


},{
        'name': 'The Elder Scrolls IV: Oblivion',
        'gender': 'RPG',
        'developer':'Bethesda',
        'ESRB Clasification': 'M',

},{
        'name': 'Tony Hawks Pro Skater 2',
        'gender': 'Sports',
        'developer':'Activision',
        'ESRB Clasification': 'T',
}
]

header_list=(
    'name',
    'gender',
    'developer',
    'ESRB Clasification'
)

def enter_info_csv (path_file,data,headers):
    with open (path_file,'w', encoding='utf-8') as file:
     writer = csv.DictWriter(file,headers, delimiter='\t')
     writer.writeheader() 
     writer.writerows(data)


enter_info_csv ('games2.csv',game_list,header_list)