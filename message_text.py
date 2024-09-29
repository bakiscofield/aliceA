from module import get_user_data

def welcome_message(user):
    full_name, first_name, last_name, username = get_user_data(user)    
    
    return f""" 
👩🏾 Salut {full_name}

Je m'appelle ALICE, je suis un BOT 🤖. Je suis là pour vous assister dans tous vos opérations de dépôt et retrait 1xbet, betwiner, 1win, melbet et 888starz je suis là également pour vos opérations achat et vente des cryptomonnaies .

👩🏾 svp ALICE vous demande de sélectionner un des services que vous désirez actuellement 

1- Pour recharger votre compte de paris sportifs ,
2- Pour faire un retrait sur votre compte de paris sportifs ,
3- Pour acheter ou vendre les cryptomonnaies ,
4- Pour  Integrer la communauté d'ALICE 
5- Contacter le service client

👩🏾 (Pour sélectionner l'élément souhaité, envoyez-moi simplement le numéro (1, 2, 3, 4 ou 5) dans le message de réponse)

Le code Code promo d'ALICE sur 1xbet , betwinner,1win, melbet et 888starz pour bénéficier des bonus et avantages est : ALICE
"""

def pyament_method_choice_message(menu, operation, enumerate_choice):
    return f"""🤖👩🏾‍🦱💁🏾‍♀️ cher client , 
Svp Veillez  choisir votre  moyen de payement avec le quel vous voulez  effectuer votre {operation} en sélectionnant un numéro({",".join([ str(i+1) for i in range(len(enumerate_choice))])})👩🏾‍🦱💹🤖:
{menu}
\n
"""

def bookmekers_list_message(menu, operation):
    return f"""
🤖👩🏾‍🦱💁🏾‍♀️ cher client , 

Svp Veillez  choisir votre bookmaker chez qui vous voulez  effectuer votre {operation} en sélectionnant un numéro(1,2,3,4,5 )👩🏾‍🦱💹🤖:\n
{menu}\n
NB d'ALiCE 💁🏾‍♀️❤️🤖 : veillez noter que pour le retrait veillez choisir le caissier chez qui vous faites les dépôts d'habitude .

nous serons ravis de vous assister en cas de soucis de retrait .💹💁🏾‍♀️

Code promo :ALICE 🤑🤑🤑
"""

def operation_id_amount_message(payement_method, bookmaker, key_word):
    return f"""
💳 👩🏾‍🦱 Cher client Pour <b>recharger</b> votre compte <b>{bookmaker.upper()}</b> par <b>{payement_method.upper()}</b>, envoyer "{key_word.title()}" suivit de votre ID de compte de paris sportifs puis du montant que vous voulez <b>recharger</b> . 

Exemple: pour <b>recharger</b> 5000 FCFA sur le compte d'ID 123456789 : 

Faites cette syntaxe : 

"<b>{key_word} 123456789 5000"</b>

NB D'ALICE : Nos prestations de services sont sans frais au dépôt et au retrait et veuillez suivre nos instructions pour bien recevoir vos transactions sur votre compte de jeu

"""

def operation_id_amount_message_retrait(payement_method, bookmaker, key_word):
    return f"""
💳 👩🏾‍🦱 Cher client Pour faire un <b>retrait</b> de votre compte <b>{bookmaker.upper()}</b> par <b>{payement_method.upper()}</b>, envoyer "{key_word.title()}" suivit de votre ID de compte de paris sportifs puis du montant que vous voulez <b>retirer</b> . 

Exemple: pour <b>retirer</b> 5000 FCFA sur le compte d'ID 123456789 : 

Faites cette syntaxe : 

"<b>{key_word.title()} 123456789 5000"</b>

NB D'ALICE : Nos prestations de services sont sans frais au dépôt et au retrait et veuillez suivre nos instructions pour bien recevoir vos transactions sur votre compte de jeu

"""


def wait_for_searching_caissiers_message(payement_method, bookmaker):
    return f"""
👩🏾‍🦱👩🏾cher client Un instant S'il vous plaît 🕚 , je vérifie la disponibilité des caissiers💱 et je vous envoie les instructions pour éffectuer votre paiement 
par  <b>{payement_method.upper()}</b> sur votre compte <b>{bookmaker.upper()}</b>.
NB d'ALICE 💙: veuillez respecter les syntaxes qui vous seront envoyées pour payer sans faire d'erreur .

"""

def build_caissier_choice_message(menu):
    return f"""
👩🏾❤️ cher client j'ai trouvé les caissiers disponibles 💰 pour vous servir .

Voici les caissiers Disponibles 💰 : \n
{menu} \n 
NB d'ALICE 👩🏾‍🦱❤️ :
S'il vous plaît cher client les retraits ne sont traités  qu' avec le caissier qui vous sert  d'habitude .Au moment du retrait si  vous avez  des difficultés veillez  écrire à l'assistance .❇️❇️
"""

def show_caissier_payement_info(caissier, code_transaction, montant, numero_agent, etablissement, method):
    return f"""
Cher client 👩🏾 Voici les informations du caissier : {caissier} 💰 💹

Syntaxe {method} 👩🏾‍🦱❤️

{code_transaction}*{montant}*{ numero_agent }#

Nom du marchand : { etablissement }

NB d'ALICE 👩🏾‍🦱❤️: vérifiez le nom du marchand avant de valider la transaction avec votre code secret.

Veillez toujours à envoyer la référence de la transaction  après l'envoi envoi 

Numéro agent : { numero_agent } ({ etablissement })

<b>NB d'ALICE 👩🏾‍🦱💙: Une fois le paiement fait, envoyez la référence en réponse suivant cette syntaxe : Ref XXXXXXXXX </b>

"""

def build_collect_screen_short_message(payement_method):
    return f"""
Merci, soumettez maintenant la capture d'écran du paiement {payement_method}
"""

def build_confirmation_attempt_message(operation="dépôt", numero="0"):
    return f""" 
Cher client 👩🏾❤️👩🏾‍🦱
Merci de patienter un moment,🤖 votre demande de {operation} N°{numero} est en cours de traitement svp  .💹💱
"""

def build_success_message(numero=""):
    return f""" 
Votre opétation N°{numero} à été éffectuer avec success 🥳🤩🥳✅🥳🤩🥳✅🥳🤩🥳✅✅
"""

def build_caissier_retrait_info(caissier, ville, rue, montant):
    return f""" 
Voici les informations de retrait pour le caissier {caissier}

Faites votre retrait sur 👇🏿👇

Ville : { ville }

Rue : { rue }

Montant : { montant }

Une fois que vous avez le code du retrait, écrivez le mot CODE suivi du code à 4 caractères et votre identifiant puis soumettez au robot !

Exemple : Code A1B2 123456789, (code=A1B2, ID=123456789)
"""

def build_social_link_message():
    return f"""
👩🏾‍🦱🤖👩🏾❤️ cher client ( le nom du client  ), 

Voulez-vous intégrez notre communauté ? 💁🏾‍♀️
Si oui cher client , vous êtes là bienvenue . 

Veuillez cliquer sur ces deux liens ci-dessous pour intégrer la communauté : 

Lien du groupe WhatsApp👩🏾‍🦱👩🏾‍🦱 : 

https://chat.whatsapp.com/LmSgrbW4QOi3Mp8hoRyifi

Lien du groupe télégramme 💁🏾‍♀️💹 :

https://t.me/+q-X8Tp2aX7o1MjQ0
 
Les objectifs  de la communauté cherche client : 

- Nous passerons des informations générales ❤️ ,

- Nos offres de promotions seront partagées aussi dans notre communauté 💱, 

- Partages des coupons 🤖💁🏾‍♀️ , 

- Partages des offres de promotions des bookmakers. 🤑🤑 ,

-Partages des astuces sur les jeux  🤩🤩.

NB d'ALICe 🤖👩🏾‍🦱💁🏾‍♀️ :  veillez noter que notre communauté est créer pour vous aider sur les applications de paris sportifs et l'achat et ventes des actifs numériques (cryptomonnaies etc ..)

Code promo : ALICE
"""

def build_service_client_link_message():
    return f"""
👩🏾👩🏾‍🦱🤖❤️ Cher client ,

svp cliquez sur l'un des liens pour écrire au service clientèle:

WhatsApp :wa.me/+22890563620

Télégramme :@ALICE_bot_Togo

🤖👩🏾‍🦱👩🏾 Cher client n'hésitez pas à nous écrire pour ces opérations de virement , nous serons ravis de vous assister 💰💰.🥳🥳
"""

def build_request_message(data):
    return f"""
<b>NUMERO COMMANDE</b> : {data['NUMERO']}\n
<b>TYPE OPERATION</b> : {data['TYPE_OPERATION']}\n
<b>PAYEMENT_METHOD</b> : {data['PAYEMENT_METHOD']['nom_moyen'].capitalize()}\n
<b>BOOKMAKER</b> : {data['BOOKMAKER']}\n
<b>CAISSIER</b> : {data['CAISSIER']['username']}\n
<b>ID</b> : <code>{data['ID']}</code>\n
<b>MONTANT</b> : {data['MONTANT']}\n
<b>REFERENCE</b> : {data['REFERENCE'][1]}\n
<b>TELEPHONE</b> : <code>{data['CONTACT']}</code>\n
"""

def build_request_message_retrait(data):
    return f"""
<b>NUMERO COMMANDE</b> : {data['NUMERO']}\n
<b>TYPE OPERATION</b> : {data['TYPE_OPERATION']}\n
<b>PAYEMENT_METHOD</b> : {data['PAYEMENT_METHOD']['nom_moyen'].capitalize()}\n
<b>BOOKMAKER</b> : {data['BOOKMAKER']}\n
<b>CAISSIER</b> : {data['CAISSIER']['username']}\n
<b>ID</b> : <code>{data['ID']}</code>\n
<b>CODE</b> : <code>{data['CODE']}</code>\n
<b>MONTANT</b> : {data['MONTANT']}\n
<b>TELEPHONE</b> : <code>{data['CONTACT']}</code>\n
"""

def build_error_message():
    return f""" 
Aïe 🤖😓 ! !

Je ne comprend pas ce que vous voulez dire !

Tapez <code>Bonjour</code> pour commencer ! 

Pour recharger 5000 FCFA sur le compte ID 123456789  Tapez

Recharge 123456789 5000 => T-money
Frecharge 123456789 5000 => Flooz

Ou pour retirer 5000 FCFA avec le numéro de téléphone 123456789 

Retrait 123456789 5000 => T-money
Fretrait 123456789 5000 => Flooz
"""

def build_confirm_transaction(type_operation= "", numero="", user=""):
    return f"""
🤖👩🏾‍🦱👩🏾❤️
Cher  client ,
Votre demande de {type_operation}  N°: {numero} à été traitée avec succès  🥂✅✅✅🥳!!!
Code promo d'ALICE pour des bonus et avantages est : ALICE 

Bonne chance à vous cher client {user} 🤩🥳🤑 !!!
"""

def build_transaction_for_admin(emoji="", numero="", etat="", caissier=""):
    return f"""
La commande N°{numero} a été {etat} par le caissier {caissier} {emoji}
"""

def build_reject_transaction(type_operation="", numero=""):
    return f"""
Ai 🤖🤖👾😲 !!!

❗❗ Nous avons un problème avec votre demande de {type_operation} N°{numero} ❗❗

Veillez contacter le service clientèle pour plus d'informations . 🤖

WhatsApp :wa.me/+22890563620

Télégramme :@ALICE_bot_Togo

"""

def build_virement_bancaire_message(moyen):
    return f"""
👩🏾👩🏾‍🦱🤖❤️ cher client ,

Pour le {moyen} 💰🤑 veillez contacter le service clientèle pour les instructions . 🤖

Cher client svp cliquez sur l'un des liens pour écrire au service clientèle:

WhatsApp :wa.me/+22890563620

Télégramme :@ALICE_bot_Togo

🤖👩🏾‍🦱👩🏾 Cher client n'hésitez pas à nous écrire pour ces opérations de virement , nous serons ravis de vous assister 💰💰.🥳🥳
"""

def build_ask_phone_number():
    return f""" 
cher client , 

Quel est le numéro de téléphone  avec le quelle vous avez effectué  la transaction   💹❇️? 

NB d'ALICE ❤️ ❤️ : veillez bien indiqué le numéro utilisé pour la transaction pour qu'un problème ne se pose pas à la vérification.

Code promo : ALICE 

👩🏾‍🦱 💁🏾‍♀️ 🤖
"""

