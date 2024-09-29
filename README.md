# alice_bot_new_version

# Dépôt
Pour faire un dépot : 

- Dépôt Endpoint : POST http://127.0.0.1:8000/api/orders/create
- Data: 
{
    "client": client_id,
    "employee_payment_methode": employee_payment_id,
    "is_depot": True,
    "transaction_id": transaction_id,
    "montant": montant,
    "code_parainage": null,
    "bookmaker_identifiant": null
}

* Récupérer ou créer le client en fonction de son chat_id.
    - Endpoint : POST http://127.0.0.1:8000/api/clients/get_or_create/<chat_id:str>
    - Data :
    {
        "id_chat" : "56982588",
        "nom" : "kondi",
        "prenom" : "Abdoul Malik",
        "contact" : "+228 93561240"
    }

* Récupérer l'employee_payment_methode :
    - Endpoint : GET http://127.0.0.1:8000/api/employee_payement_methode_by_employee_and_bookmaker_and_payement_methode/<int:employee_id>/<int:bookmaker_id>/<int:payement_methode_id>'

    * Pour récupérer les payement_methodes.
        - Endpoint : GET http://127.0.0.1:8000/api/payment_methods
        - Response : [

        ]

    * Pour récupérer les bookmakers.
        - Endpoint : GET http://127.0.0.1:8000/api/bookmakers
        - Response : [
            
        ]

    * Pour récupérer les caissier (employees) en fonction du bookmaker et du payment_method.
        - Endpoint : GET http://127.0.0.1:8000/api/employees/filter/<int:bookmaker_id>/<int:payment_method_id>
        - Response : [
            
        ]
        


