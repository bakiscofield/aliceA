# Instances pour le modèle Bookmaker
from api.models import Bookmaker, PayementMethod, Employee, EmployeePayementMethod, Client
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from faker import Faker

def create_groups():
    Group.objects.all().delete()
    content_type = ContentType.objects.get(app_label='api', model='order')

    permissions_data = [
        {
            "name": 'Can view dashboard',
            "codename": "view_dashboard",
            "content_type": content_type,
        },
    ]

    for permission_data in permissions_data:
        permission = Permission.objects.filter(codename=permission_data["codename"])
        if permission:
            permission.delete()
        
        Permission.objects.create(**permission_data).codename
    
    groups_data = [
        {
            'name' : "admin",
            'permissions_names' : [
               "view_employee",
            ],
        },
        {
            'name' : "superadmin",
            'permissions_names' : [
                "print_ticket",
            ],
        },
        {
            'name' : "caissier",
            'permissions_names' : [],
        },
        {
            'name' : "personnel",
            'permissions_names' : [],
        },
    ]
    
    for group_data in groups_data:
        group = Group.objects.create(name=group_data['name'])
        permissions = Permission.objects.filter(codename__in=group_data['permissions_names'])
        group.permissions.set(permissions)

def run():
    print("::::::::::::::::::::::: DELETE ALL INSTANCE FOR ALL MODELS ::::::::::::::::::::::::::")
    User.objects.all().exclude(username="aziz").delete()
    Client.objects.all().delete()
    # Role.objects.all().delete()
    Bookmaker.objects.all().delete()
    PayementMethod.objects.all().delete()
    Employee.objects.all().delete()
    EmployeePayementMethod.objects.all().delete()
    create_groups()
    
    print("::::::::::::::::::::::: CREATE Client INSTANCES ::::::::::::::::::::::::::")
    fake = Faker()    

    for i in range(10):
        Client.objects.create(
            id_chat=i+1000,
            nom=fake.last_name(),
            prenom=fake.first_name(),
            contact=i+1000,
            username=i+1000,
            create_at=fake.date_time_this_decade(),
        )
    
    print("::::::::::::::::::::::: CREATE BOOKMAKERS INSTANCES ::::::::::::::::::::::::::")
    bookmakers = ['1xbet', 'betwiner', '1win', 'melbet', '888starz']
    for bookmaker_name in bookmakers:
        Bookmaker.objects.create(nom_bookmaker=bookmaker_name)

    print("::::::::::::::::::::::: CREATE PAYEMENT METHOD INSTANCES ::::::::::::::::::::::::::")
    payements = [
        ('T-money', '*145*2*{montant}*{code_agent}#', 'recharge', 'retrait'), 
        ('Flooz', '*155*2*2*{code_agent}*{code_agent}*{montant}#', 'frecharge', 'fretrait'), 
        ('Virement bancaire', 'bank', 'bank', 'bank'), 
        ('Western union, moneygram, ria, etc.. ', 'bank', 'bank', 'bank')
        ]
    
    for nom_moyen, code_operation, mot_recharge, mot_retrait  in payements:
        PayementMethod.objects.create(nom_moyen=nom_moyen, code_operation=code_operation, mot_recharge=mot_recharge, mot_retrait=mot_retrait)

    print("::::::::::::::::::::::: CREATE EMPLOYE INSTANCES ::::::::::::::::::::::::::")
    # 5909365746
    donnees_employes = [
        {'id_chat': 5909365746, 'nom': 'Emile', 'prenom': 'Emile', 'contact': "90", "username": "1"},
        {'id_chat': 5197301257, 'nom': '', 'prenom': '', 'contact': "10", "username": "2"},
        {'id_chat': 1, 'nom': '', 'prenom': '', 'contact': "11", "username": "3"},
        {'id_chat': 2, 'nom': '', 'prenom': '', 'contact': "12", "username": "4"},
        {'id_chat': 3, 'nom': 'chardi', 'prenom': 'sanguera', 'contact': "+2289562727", "username": "5"},
        # {'id_chat': 4, 'nom': 'traore', 'prenom': 'savadogo', 'contact': "68", "username": "6"},
        # {'id_chat': 5, 'nom': 'k', 'prenom': 'k', 'contact': "69", "username": "7"},
        {'id_chat': 1830533719, 'nom': 'traore', 'prenom': 'savadogo', 'contact': "68", "username": "6"},
        {'id_chat': 5284977867, 'nom': 'k', 'prenom': 'k', 'contact': "69", "username": "7"},
    ]

    # Création des instances de Employe à partir de la liste
    for donnees_employe in donnees_employes:
        Employee.objects.create(**donnees_employe)

    employes = Employee.objects.all()
    sup_admin = employes[0]
    caissier1 = employes[1]
    caissier2 = employes[2]
    caissier3 = employes[3]
    caissier4 = employes[4]
    admin = employes[5]
    admin2 = employes[6]
    
    groups = Group.objects.all()
    sup_admin.user.groups.set([groups[1]])
    caissier1.user.groups.set([groups[2]])
    caissier2.user.groups.set([groups[2]])
    caissier3.user.groups.set([groups[2]])
    caissier4.user.groups.set([groups[2]])
    admin.user.groups.set([groups[0]])
    admin2.user.groups.set([groups[0]])
    
    
    bookmakers = Bookmaker.objects.all()
    xbet = bookmakers[0]
    betwiner = bookmakers[1]
    onewin = bookmakers[2]
    melbet = bookmakers[3]
    h888straz = bookmakers[4]
    
    payements = PayementMethod.objects.all()
    t_money = payements[0]
    flooz = payements[1]
    
    print("::::::::::::::::::::::: CREATE EmployeePayementMethod INSTANCES ::::::::::::::::::::::::::")
    # Instance pour le modèle Employe_payement_methode
    EmployeePayementMethod.objects.create(
        code_agent=37731,
        frais_depot=50,
        frais_retrait=0,
        etablissement='LIGDICASH TOGO',
        rue='Emile business',
        ville='Lomé martime',
        employee=sup_admin,
        payment_method=t_money,
        bookmaker=xbet,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=79321168,
        frais_depot=50,
        frais_retrait=0,
        etablissement='CAREIDABUSSINESS',
        rue='Emile business',
        ville='Lomé martime',
        employee=sup_admin,
        payment_method=flooz,
        bookmaker=xbet,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=37731,
        frais_depot=50,
        frais_retrait=0,
        etablissement='',
        rue='CMS sanguera',
        ville='Lomé martime',
        employee=caissier1,
        payment_method=t_money,
        bookmaker=xbet,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=79321168,
        frais_depot=50,
        frais_retrait=0,
        etablissement='',
        rue='CMS sanguera',
        ville='Lomé martime',
        employee=caissier1,
        payment_method=flooz,
        bookmaker=xbet,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=37731,
        frais_depot=50,
        frais_retrait=0,
        etablissement='',
        rue='Emile 01',
        ville='Lomé martime',
        employee=caissier2,
        payment_method=t_money,
        bookmaker=xbet,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=79321168,
        frais_depot=50,
        frais_retrait=0,
        etablissement='',
        rue='Emile 01',
        ville='Lomé martime',
        employee=caissier2,
        payment_method=flooz,
        bookmaker=xbet,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=37731,
        frais_depot=50,
        frais_retrait=0,
        etablissement='',
        rue='Emile 3',
        ville='Lomé martime',
        employee=caissier3,
        payment_method=t_money,
        bookmaker=xbet,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=79321168,
        frais_depot=50,
        frais_retrait=0,
        etablissement='',
        rue='Emile 3',
        ville='Lomé martime',
        employee=caissier3,
        payment_method=flooz,
        bookmaker=xbet,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=37731,
        frais_depot=50,
        frais_retrait=0,
        etablissement='LIGDICASH TOGO',
        rue='agoe-cacaveli',
        ville='Lomé martime',
        employee=sup_admin,
        payment_method=t_money,
        bookmaker=betwiner,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=79321168,
        frais_depot=50,
        frais_retrait=0,
        etablissement='CAREIDABUSSINESS',
        rue='agoe-cacaveli ',
        ville='Lomé martime',
        employee=sup_admin,
        payment_method=flooz,
        bookmaker=betwiner
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=37731,
        frais_depot=50,
        frais_retrait=0,
        etablissement='CAREIDABUSSINESS',
        rue='Emile business',
        ville='Lomé martime',
        employee=sup_admin,
        payment_method=t_money,
        bookmaker=melbet
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=79321168,
        frais_depot=50,
        frais_retrait=0,
        etablissement='CAREIDABUSSINESS',
        rue='Emile business',
        ville='Lomé martime',
        employee=sup_admin,
        payment_method=flooz,
        bookmaker=melbet,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=37731,
        frais_depot=50,
        frais_retrait=0,
        etablissement='CAREIDABUSSINESS',
        rue='',
        ville='Lomé',
        employee=sup_admin,
        payment_method=t_money,
        bookmaker=onewin
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=79321168,
        frais_depot=50,
        frais_retrait=0,
        etablissement='CAREIDABUSSINESS',
        rue='',
        ville='Lomé',
        employee=sup_admin,
        payment_method=flooz,
        bookmaker=onewin,
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=37731,
        frais_depot=50,
        frais_retrait=0,
        etablissement='LIGDICASH TOGO',
        rue='Emile business',
        ville='Lomé martime',
        employee=sup_admin,
        payment_method=t_money,
        bookmaker=h888straz
    )
    
    EmployeePayementMethod.objects.create(
        code_agent=79321168,
        frais_depot=50,
        frais_retrait=0,
        etablissement='CAREIDABUSSINESS',
        rue='Emile business',
        ville='Lomé martime',
        employee=sup_admin,
        payment_method=flooz,
        bookmaker=h888straz,
    )




