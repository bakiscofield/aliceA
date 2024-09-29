def build_request_message(id, 
                          type_transction, 
                          payment_method,
                          bookmaker, 
                          username, 
                          bookmaker_identifiant, 
                          montant,
                          reference_id, 
                          contact):
    reference_libelle = "REFERENCE" if type_transction=="DEPOT" else "CODE"
    return f"""
<b>NUMERO COMMANDE</b> : {id} \n
<b>TYPE OPERATION</b> : {type_transction}\n
<b>PAYEMENT_METHOD</b> : {payment_method}\n
<b>BOOKMAKER</b> : {bookmaker}\n
<b>CAISSIER</b> : {username}\n
<b>ID</b> : <code>{bookmaker_identifiant}</code>\n
<b>MONTANT</b> : {montant} \n
<b>{reference_libelle}</b> : {reference_id}\n
<b>TELEPHONE</b> : <code>{contact}</code> \n
"""


def build_client_confirm_transaction_message(type_operation= "", numero="", client="", **kwargs):
    return f"""
🤖👩🏾‍🦱👩🏾❤️
Cher  client ,
Votre demande de {type_operation}  N°: {numero} à été traitée avec succès  🥂✅✅✅🥳!!!
Code promo d'ALICE pour des bonus et avantages est : ALICE 

Bonne chance à vous cher client {client} 🤩🥳🤑 !!!
"""

def build_client_cancel_transaction_message(type_operation="", numero="", **kwargs):
    return f"""
Ai 🤖🤖👾😲 !!!

❗❗ Nous avons un problème avec votre demande de {type_operation} N°{numero} ❗❗

Veillez contacter le service clientèle pour plus d'informations . 🤖

WhatsApp :wa.me/+22890563620

Télégramme :@ALICE_bot_Togo

"""

def build_admin_status_transaction_message(emoji="", numero="", state="", employee="", **kwargs):
    return f"""
La commande N°{numero} a été {state} par le caissier {employee} {emoji}
"""

def build_client_confirmation_attempt_message(id, type_transction, **kwargs):
    return f""" 
Cher client 👩🏾❤️👩🏾‍🦱
Merci de patienter un moment,🤖 votre demande de {type_transction} N°{id} est en cours de traitement svp  .💹💱
"""





